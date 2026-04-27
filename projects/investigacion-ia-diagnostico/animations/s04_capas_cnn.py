from manim import *
import numpy as np

Text.set_default(font="Noto Sans", line_spacing=1.1)


class S04_CapasCNN(MovingCameraScene):
    """
    The digit '8' through a real CNN:
    Act 1 — Convolution: a 3x3 kernel slides over the input image
    Act 2 — Multiple kernels learn different features
    Act 3 — Max-pool + deeper conv combine features hierarchically
    Act 4 — Flatten + Dense + Softmax
    """

    # ── helpers ──────────────────────────────────────────────────────────────

    def _make_digit_8(self, size=16):
        """Anti-aliased '8' as two stacked ellipse strokes on size×size grid."""
        img = np.zeros((size, size))
        cx = (size - 1) / 2.0
        cy_top = (size - 1) * 0.27
        cy_bot = (size - 1) * 0.73
        rx = (size - 1) * 0.26
        ry = (size - 1) * 0.21
        thickness = 1.0  # pixel units, sharper strokes
        scale_perp = min(rx, ry)

        for y in range(size):
            for x in range(size):
                ft = ((x - cx) / rx) ** 2 + ((y - cy_top) / ry) ** 2
                d_top = abs(np.sqrt(ft) - 1.0) * scale_perp
                fb = ((x - cx) / rx) ** 2 + ((y - cy_bot) / ry) ** 2
                d_bot = abs(np.sqrt(fb) - 1.0) * scale_perp
                d = min(d_top, d_bot)
                v = max(0.0, 1.0 - d / thickness)
                img[y, x] = min(1.0, v)
        return img

    def _grid(self, mat, cell=0.24, fill_color=BLUE_C,
              stroke_color=GRAY_D, stroke_width=0.4):
        """VGroup of squares; fill_opacity scaled by matrix value."""
        rows, cols = mat.shape
        g = VGroup()
        for r in range(rows):
            for c in range(cols):
                v = float(mat[r, c])
                op = max(0.0, min(1.0, v))
                sq = Square(side_length=cell,
                            fill_color=fill_color, fill_opacity=op,
                            stroke_color=stroke_color, stroke_width=stroke_width)
                sq.move_to(RIGHT * c * cell + DOWN * r * cell)
                g.add(sq)
        g._rows, g._cols, g._cell = rows, cols, cell
        g.move_to(ORIGIN)
        return g

    def _gcell(self, grid, r, c):
        return grid[r * grid._cols + c]

    def _kernel_box(self, weights, cell=0.36, label_size=12):
        """Kernel display with signed weights (blue +, red -, dim 0)."""
        rows, cols = weights.shape
        g = VGroup()
        for r in range(rows):
            for c in range(cols):
                w = float(weights[r, c])
                if w > 0:
                    color, op = BLUE_C, 0.55
                elif w < 0:
                    color, op = RED_C, 0.55
                else:
                    color, op = GRAY_C, 0.18
                sq = Square(side_length=cell, fill_color=color, fill_opacity=op,
                            stroke_color=color, stroke_width=1.0)
                sq.move_to(RIGHT * c * cell + DOWN * r * cell)
                lbl = Text(f"{w:+.0f}", font_size=label_size, color=WHITE,
                           weight=BOLD)
                lbl.move_to(sq.get_center())
                g.add(VGroup(sq, lbl))
        g.move_to(ORIGIN)
        return g

    def _conv2d_abs(self, x, k):
        """2D convolution, no padding, stride 1; absolute value, normalized."""
        H, W = x.shape
        kH, kW = k.shape
        out = np.zeros((H - kH + 1, W - kW + 1))
        for r in range(out.shape[0]):
            for c in range(out.shape[1]):
                out[r, c] = float((x[r:r + kH, c:c + kW] * k).sum())
        out = np.abs(out)
        if out.max() > 0:
            out = out / out.max()
        # Light gamma to enhance edges
        out = out ** 0.85
        return out

    def _maxpool(self, x, k=2):
        H, W = x.shape
        oH, oW = H // k, W // k
        out = np.zeros((oH, oW))
        for r in range(oH):
            for c in range(oW):
                out[r, c] = x[r * k:(r + 1) * k, c * k:(c + 1) * k].max()
        return out

    def _light_cell(self, grid, r, c, val, color):
        cell = self._gcell(grid, r, c)
        return cell.animate.set_fill(color, opacity=max(0.0, min(1.0, val)))

    # ── construct ────────────────────────────────────────────────────────────

    def construct(self):
        digit = self._make_digit_8(size=12)

        K_HORIZ = np.array([[-1, -1, -1],
                            [ 0,  0,  0],
                            [ 1,  1,  1]], dtype=float)
        K_VERT  = np.array([[-1,  0,  1],
                            [-1,  0,  1],
                            [-1,  0,  1]], dtype=float)
        K_LAPL  = np.array([[ 0, -1,  0],
                            [-1,  4, -1],
                            [ 0, -1,  0]], dtype=float)

        fmap_h = self._conv2d_abs(digit, K_HORIZ)
        fmap_v = self._conv2d_abs(digit, K_VERT)
        fmap_l = self._conv2d_abs(digit, K_LAPL)

        title = Text("How a CNN Sees the '8'",
                     font_size=28, color=TEAL_C, weight=BOLD)
        title.to_edge(UP, buff=0.30)
        self.play(Write(title), run_time=0.7)

        # ═════════════════════════════════════════════════════════════════════
        # ACT 1 — Convolution mechanics
        # ═════════════════════════════════════════════════════════════════════
        act1 = Text("Act 1 -- Convolution: a kernel slides over the image",
                    font_size=14, color=GRAY_B)
        act1.next_to(title, DOWN, buff=0.10)
        self.play(FadeIn(act1), run_time=0.35)

        # Input image (left) — 12×12 anti-aliased "8"
        IN_CELL = 0.30
        img = self._grid(digit, cell=IN_CELL, fill_color=BLUE_C,
                         stroke_color="#222244", stroke_width=0.35)
        img.move_to(LEFT * 4.5 + DOWN * 0.15)
        img_lbl = Text("Input  12x12", font_size=13, color=BLUE_C)
        img_lbl.next_to(img, UP, buff=0.18)
        self.play(FadeIn(img), FadeIn(img_lbl), run_time=0.6)

        # Kernel display (top-center)
        kernel_box = self._kernel_box(K_HORIZ, cell=0.42, label_size=14)
        kernel_box.move_to(ORIGIN + UP * 1.6)
        kernel_lbl = Text("3x3 kernel\n(horizontal edges)",
                          font_size=12, color=YELLOW)
        kernel_lbl.next_to(kernel_box, UP, buff=0.12)
        self.play(FadeIn(kernel_box), FadeIn(kernel_lbl), run_time=0.5)

        # Empty feature map (right) — 10×10
        FM_CELL = IN_CELL  # match cell size for visual scale
        oH, oW = fmap_h.shape
        fmap_grid = self._grid(np.zeros_like(fmap_h),
                               cell=FM_CELL, fill_color=YELLOW)
        fmap_grid.move_to(RIGHT * 4.4 + DOWN * 0.15)
        fmap_lbl = Text(f"Feature map  {oH}x{oW}",
                        font_size=13, color=YELLOW)
        fmap_lbl.next_to(fmap_grid, UP, buff=0.18)
        self.play(FadeIn(fmap_grid), FadeIn(fmap_lbl), run_time=0.5)

        # Receptive field box on input (3×3) and output cell highlight
        rf = Rectangle(width=IN_CELL * 3, height=IN_CELL * 3,
                       stroke_color=YELLOW, stroke_width=3.5, fill_opacity=0)
        rf.move_to(self._gcell(img, 1, 1).get_center())
        out_hl = Square(side_length=FM_CELL, stroke_color=GREEN,
                        stroke_width=2.5, fill_opacity=0)
        out_hl.move_to(self._gcell(fmap_grid, 0, 0).get_center())
        self.play(FadeIn(rf), FadeIn(out_hl), run_time=0.3)

        # Slow demo: 4 well-chosen positions
        slow = [(0, 0), (1, 4), (4, 4), (7, 7)]
        for r, c in slow:
            self.play(
                rf.animate.move_to(self._gcell(img, r + 1, c + 1).get_center()),
                out_hl.animate.move_to(self._gcell(fmap_grid, r, c).get_center()),
                run_time=0.55,
            )
            self.play(self._light_cell(fmap_grid, r, c, fmap_h[r, c], YELLOW),
                      run_time=0.22)

        # Quick sweep: RF travels diagonally to bottom-right while feature map fills
        last_r, last_c = oH - 1, oW - 1
        fill_anims = [
            self._light_cell(fmap_grid, r, c, fmap_h[r, c], YELLOW)
            for r in range(oH) for c in range(oW)
            if (r, c) not in slow
        ]
        self.play(
            rf.animate.move_to(self._gcell(img, last_r + 1, last_c + 1).get_center()),
            out_hl.animate.move_to(self._gcell(fmap_grid, last_r, last_c).get_center()),
            LaggedStart(*fill_anims, lag_ratio=0.008),
            run_time=1.6,
        )
        self.play(FadeOut(rf), FadeOut(out_hl), run_time=0.3)

        cap1 = Text("Same kernel weights at every position -- spatial structure preserved",
                    font_size=14, color=GRAY_A)
        cap1.to_edge(DOWN, buff=0.30)
        self.play(FadeIn(cap1), run_time=0.4)
        self.wait(1.2)
        self.play(FadeOut(cap1), run_time=0.3)

        # ═════════════════════════════════════════════════════════════════════
        # ACT 2 — Multiple kernels = multiple feature maps
        # ═════════════════════════════════════════════════════════════════════
        self.play(FadeOut(act1), FadeOut(kernel_lbl), run_time=0.3)
        act2 = Text("Act 2 -- Each filter learns a different feature",
                    font_size=14, color=GRAY_B)
        act2.next_to(title, DOWN, buff=0.10)
        self.play(FadeIn(act2), run_time=0.35)

        # Tag the first kernel and shrink first row; input stays where it is
        k1_tag = Text("horizontal", font_size=11, color=YELLOW, weight=BOLD)
        k1_tag.next_to(kernel_box, LEFT, buff=0.18)
        self.play(FadeIn(k1_tag), run_time=0.25)

        ROW_SCALE = 0.55
        kernel_pair_1 = VGroup(kernel_box, k1_tag)
        fmap_pair_1 = VGroup(fmap_grid, fmap_lbl)
        self.play(
            kernel_pair_1.animate.scale(ROW_SCALE).move_to(LEFT * 0.2 + UP * 1.9),
            fmap_pair_1.animate.scale(ROW_SCALE).move_to(RIGHT * 3.0 + UP * 1.9),
            run_time=0.7,
        )

        # Build two more rows: vertical and Laplacian
        def build_row(K, fmap, color, name, y):
            kbox = self._kernel_box(K, cell=0.42 * ROW_SCALE, label_size=10)
            kbox.move_to(LEFT * 0.2 + UP * y)
            tag = Text(name, font_size=11, color=color, weight=BOLD)
            tag.next_to(kbox, LEFT, buff=0.18)
            fg = self._grid(fmap, cell=FM_CELL * ROW_SCALE, fill_color=color)
            fg.move_to(RIGHT * 3.0 + UP * y)
            flbl = Text(f"{name} edges", font_size=11, color=color)
            flbl.next_to(fg, UP, buff=0.10)
            return VGroup(kbox, tag), VGroup(fg, flbl)

        kpair_2, fpair_2 = build_row(K_VERT, fmap_v, ORANGE, "vertical", 0.0)
        kpair_3, fpair_3 = build_row(K_LAPL, fmap_l, "#9D7BFF", "all", -1.9)

        self.play(FadeIn(kpair_2), FadeIn(fpair_2), run_time=0.7)
        self.play(FadeIn(kpair_3), FadeIn(fpair_3), run_time=0.7)
        self.wait(0.7)

        cap2 = Text("3 kernels -> 3 channels  (each highlights a different aspect of the '8')",
                    font_size=14, color=GRAY_A)
        cap2.to_edge(DOWN, buff=0.30)
        self.play(FadeIn(cap2), run_time=0.4)
        self.wait(1.6)
        self.play(FadeOut(cap2), run_time=0.3)

        # ═════════════════════════════════════════════════════════════════════
        # ACT 3 — Max-pool + deeper conv
        # ═════════════════════════════════════════════════════════════════════
        self.play(FadeOut(act2), run_time=0.2)
        act3 = Text("Act 3 -- Max-pool shrinks; deeper conv combines features",
                    font_size=14, color=GRAY_B)
        act3.next_to(title, DOWN, buff=0.10)
        self.play(FadeIn(act3), run_time=0.35)

        # Drop the input and kernels — keep the 3 feature maps
        self.play(
            FadeOut(img), FadeOut(img_lbl),
            FadeOut(kernel_pair_1), FadeOut(kpair_2), FadeOut(kpair_3),
            run_time=0.5,
        )

        # Move 3 fmaps to a column on the left
        self.play(
            fmap_pair_1.animate.move_to(LEFT * 4.5 + UP * 1.9),
            fpair_2.animate.move_to(LEFT * 4.5 + UP * 0.0),
            fpair_3.animate.move_to(LEFT * 4.5 + DOWN * 1.9),
            run_time=0.7,
        )

        # Pool each → 5×5
        pool_h = self._maxpool(fmap_h, k=2)
        pool_v = self._maxpool(fmap_v, k=2)
        pool_l = self._maxpool(fmap_l, k=2)
        POOL_CELL = 0.26
        pg1 = self._grid(pool_h, cell=POOL_CELL, fill_color=YELLOW)
        pg2 = self._grid(pool_v, cell=POOL_CELL, fill_color=ORANGE)
        pg3 = self._grid(pool_l, cell=POOL_CELL, fill_color="#9D7BFF")
        pg1.move_to(LEFT * 1.7 + UP * 1.9)
        pg2.move_to(LEFT * 1.7 + UP * 0.0)
        pg3.move_to(LEFT * 1.7 + DOWN * 1.9)
        pa1 = Arrow(fmap_pair_1.get_right(), pg1.get_left(), buff=0.15,
                    color=GRAY_C, stroke_width=1.5, tip_length=0.13)
        pa2 = Arrow(fpair_2.get_right(), pg2.get_left(), buff=0.15,
                    color=GRAY_C, stroke_width=1.5, tip_length=0.13)
        pa3 = Arrow(fpair_3.get_right(), pg3.get_left(), buff=0.15,
                    color=GRAY_C, stroke_width=1.5, tip_length=0.13)
        pool_tag = Text("max-pool 2x2  ->  5x5", font_size=12, color=GRAY_B)
        pool_tag.move_to(LEFT * 3.05 + UP * 3.05)

        self.play(GrowArrow(pa1), GrowArrow(pa2), GrowArrow(pa3),
                  FadeIn(pool_tag), run_time=0.5)
        self.play(FadeIn(pg1), FadeIn(pg2), FadeIn(pg3), run_time=0.6)
        self.wait(0.5)

        # Second conv layer: combine 3 channels → 2 deeper feature maps (3×3)
        # Hand-crafted activations: clearly localized to upper / lower half
        deep_top = np.array([[0.20, 0.95, 0.20],
                             [0.10, 0.60, 0.10],
                             [0.00, 0.05, 0.00]])
        deep_bot = np.array([[0.00, 0.05, 0.00],
                             [0.10, 0.60, 0.10],
                             [0.20, 0.95, 0.20]])
        DEEP_CELL = 0.40
        dg1 = self._grid(deep_top, cell=DEEP_CELL, fill_color=GREEN)
        dg2 = self._grid(deep_bot, cell=DEEP_CELL, fill_color=TEAL_C)
        dg1.move_to(RIGHT * 2.0 + UP * 1.7)
        dg2.move_to(RIGHT * 2.0 + DOWN * 1.7)
        dg1_lbl = Text("upper-loop", font_size=12, color=GREEN, weight=BOLD)
        dg1_lbl.next_to(dg1, UP, buff=0.14)
        dg2_lbl = Text("lower-loop", font_size=12, color=TEAL_C, weight=BOLD)
        dg2_lbl.next_to(dg2, UP, buff=0.14)

        deep_edges = VGroup()
        for src in [pg1, pg2, pg3]:
            for dst in [dg1, dg2]:
                deep_edges.add(Line(src.get_right(), dst.get_left(),
                                    stroke_color=GRAY_C, stroke_width=0.7,
                                    stroke_opacity=0.5))
        conv2_tag = Text("Conv 2  (3 -> 2 channels)",
                         font_size=12, color=GRAY_B)
        conv2_tag.move_to(ORIGIN + DOWN * 0.15)

        self.play(Create(deep_edges), FadeIn(conv2_tag), run_time=0.6)
        self.play(FadeIn(dg1), FadeIn(dg1_lbl),
                  FadeIn(dg2), FadeIn(dg2_lbl), run_time=0.6)

        cap3 = Text("Hierarchical features:  edges -> loops -> digit",
                    font_size=14, color=GRAY_A)
        cap3.to_edge(DOWN, buff=0.30)
        self.play(FadeIn(cap3), run_time=0.4)
        self.wait(1.5)
        self.play(FadeOut(cap3), run_time=0.3)

        # ═════════════════════════════════════════════════════════════════════
        # ACT 4 — Flatten + Dense + Softmax
        # ═════════════════════════════════════════════════════════════════════
        self.play(
            FadeOut(act3),
            FadeOut(fmap_pair_1), FadeOut(fpair_2), FadeOut(fpair_3),
            FadeOut(pg1), FadeOut(pg2), FadeOut(pg3),
            FadeOut(pa1), FadeOut(pa2), FadeOut(pa3),
            FadeOut(pool_tag),
            FadeOut(deep_edges), FadeOut(conv2_tag),
            run_time=0.5,
        )
        act4 = Text("Act 4 -- Flatten -> Dense -> Softmax",
                    font_size=14, color=GRAY_B)
        act4.next_to(title, DOWN, buff=0.10)
        self.play(FadeIn(act4), run_time=0.35)

        # Reposition the deep grids to the left
        deep1_pair = VGroup(dg1, dg1_lbl)
        deep2_pair = VGroup(dg2, dg2_lbl)
        self.play(
            deep1_pair.animate.move_to(LEFT * 4.5 + UP * 1.5),
            deep2_pair.animate.move_to(LEFT * 4.5 + DOWN * 1.5),
            run_time=0.6,
        )

        # Flatten: 18 cells (2 channels × 3×3)
        flat_n = 18
        flat_col = VGroup(*[
            Circle(radius=0.10,
                   fill_color=GREEN if i < 9 else TEAL_C,
                   fill_opacity=0.65, stroke_width=1)
            for i in range(flat_n)
        ])
        flat_col.arrange(DOWN, buff=0.04).move_to(LEFT * 2.0)
        flat_lbl = Text("flatten\n(18)", font_size=11, color=GRAY_B)
        flat_lbl.next_to(flat_col, UP, buff=0.14)

        flat_arrows = VGroup(
            Arrow(dg1.get_right(), flat_col.get_left(),
                  buff=0.15, color=GRAY_C, stroke_width=1.0, tip_length=0.10),
            Arrow(dg2.get_right(), flat_col.get_left(),
                  buff=0.15, color=GRAY_C, stroke_width=1.0, tip_length=0.10),
        )
        self.play(GrowArrow(flat_arrows[0]), GrowArrow(flat_arrows[1]),
                  run_time=0.4)
        self.play(LaggedStart(*[FadeIn(c, scale=0.5) for c in flat_col],
                              lag_ratio=0.04),
                  FadeIn(flat_lbl), run_time=0.7)

        # Dense layer (8 nodes)
        dense_col = VGroup(*[
            Circle(radius=0.13, fill_color=PURPLE_B, fill_opacity=0.40,
                   stroke_color=PURPLE_B, stroke_width=1.2)
            for _ in range(8)
        ])
        dense_col.arrange(DOWN, buff=0.10).move_to(LEFT * 0.1)
        dense_lbl = Text("dense\n(8)", font_size=11, color=PURPLE_B)
        dense_lbl.next_to(dense_col, UP, buff=0.14)

        ftd = VGroup()
        for i in range(0, flat_n, 3):
            for d in dense_col[::2]:
                ftd.add(Line(flat_col[i].get_center(), d.get_center(),
                             stroke_color=GRAY_C, stroke_width=0.4,
                             stroke_opacity=0.35))
        self.play(Create(ftd), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(d, scale=0.5) for d in dense_col],
                              lag_ratio=0.05),
                  FadeIn(dense_lbl), run_time=0.6)

        # Softmax output (10 classes)
        out_col = VGroup()
        out_lbls = VGroup()
        for i in range(10):
            color = GREEN if i == 8 else GRAY_C
            n = Circle(radius=0.13, fill_color=color, fill_opacity=0.35,
                       stroke_color=color, stroke_width=1.5)
            out_col.add(n)
            l = Text(str(i), font_size=12, color=color)
            out_lbls.add(l)
        out_col.arrange(DOWN, buff=0.13).move_to(RIGHT * 2.2)
        for n, l in zip(out_col, out_lbls):
            l.next_to(n, LEFT, buff=0.07)
        out_top_lbl = Text("softmax\n(10)", font_size=11, color=GREEN)
        out_top_lbl.next_to(out_col, UP, buff=0.14)

        dto = VGroup()
        for d in dense_col:
            for o in out_col[::2]:
                dto.add(Line(d.get_center(), o.get_center(),
                             stroke_color=GRAY_C, stroke_width=0.4,
                             stroke_opacity=0.35))
        self.play(Create(dto), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(n, scale=0.5) for n in out_col],
                              lag_ratio=0.04),
                  FadeIn(out_lbls), FadeIn(out_top_lbl), run_time=0.7)

        probs = [0, 0, 1, 1, 0, 0, 0, 0, 98, 0]
        prob_nums = VGroup()
        for i, (n, p) in enumerate(zip(out_col, probs)):
            col = GREEN if i == 8 else GRAY_C
            t = Text(f"{p}%", font_size=11, color=col)
            t.next_to(n, RIGHT, buff=0.07)
            prob_nums.add(t)
        self.play(LaggedStart(*[FadeIn(t) for t in prob_nums], lag_ratio=0.04),
                  run_time=0.6)

        n8 = out_col[8]
        self.play(
            n8.animate.set_fill(GREEN, opacity=1.0).scale(1.3),
            Flash(n8, color=GREEN, flash_radius=0.4, line_length=0.10),
            run_time=0.7,
        )

        cap4 = Text("Real CNN: conv + pool extract features -> dense head classifies",
                    font_size=14, color=GREEN)
        cap4.to_edge(DOWN, buff=0.30)
        self.play(FadeIn(cap4), run_time=0.5)
        self.wait(3.0)
