from manim import *
import numpy as np

Text.set_default(font="Noto Sans", line_spacing=1.1)

class S04_CapasCNN(MovingCameraScene):
    """
    The digit '8' through a real CNN.
    Steps explicitly shown:
    1. Input layer
    2. Convolution layer
    3. Activation function (ReLU)
    4. Pooling layer
    5. Fully connected layers (Dense/Flatten)
    6. Output layer (Softmax)
    """

    # ── helpers ──────────────────────────────────────────────────────────────

    def _make_digit_8(self, size=16):
        img = np.zeros((size, size))
        cx = (size - 1) / 2.0
        cy_top = (size - 1) * 0.27
        cy_bot = (size - 1) * 0.73
        rx = (size - 1) * 0.26
        ry = (size - 1) * 0.21
        thickness = 1.0  
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

    def _grid_signed(self, mat, cell=0.24, pos_color=BLUE_C, neg_color=RED_C,
                     zero_color=GRAY_D, stroke_color=GRAY_D, stroke_width=0.4):
        rows, cols = mat.shape
        g = VGroup()
        for r in range(rows):
            for c in range(cols):
                v = float(mat[r, c])
                if v > 0:
                    color = pos_color
                elif v < 0:
                    color = neg_color
                else:
                    color = zero_color
                op = max(0.0, min(1.0, abs(v)))
                sq = Square(side_length=cell,
                            fill_color=color, fill_opacity=op,
                            stroke_color=stroke_color, stroke_width=stroke_width)
                sq.move_to(RIGHT * c * cell + DOWN * r * cell)
                g.add(sq)
        g._rows, g._cols, g._cell = rows, cols, cell
        g.move_to(ORIGIN)
        return g

    def _number_grid(self, mat, cell=0.32, fmt="{:+.2f}", text_color=WHITE,
                     stroke_color=GRAY_D, stroke_width=0.6, fill_color=BLACK,
                     fill_opacity=0.0, sign_colors=False, font_size=12):
        rows, cols = mat.shape
        g = VGroup()
        for r in range(rows):
            for c in range(cols):
                v = float(mat[r, c])
                sq = Square(side_length=cell,
                            fill_color=fill_color, fill_opacity=fill_opacity,
                            stroke_color=stroke_color, stroke_width=stroke_width)
                sq.move_to(RIGHT * c * cell + DOWN * r * cell)
                color = text_color
                if sign_colors:
                    color = GREEN if v > 0 else RED_C if v < 0 else GRAY_B
                lbl = Text(fmt.format(v), font_size=font_size, color=color)
                lbl.move_to(sq.get_center())
                g.add(VGroup(sq, lbl))
        g._rows, g._cols, g._cell = rows, cols, cell
        g.move_to(ORIGIN)
        return g

    def _set_grid_values(self, grid, mat, color=YELLOW):
        rows, cols = mat.shape
        for r in range(rows):
            for c in range(cols):
                v = float(mat[r, c])
                self._gcell(grid, r, c).set_fill(color, opacity=max(0.0, min(1.0, v)))

    def _gcell(self, grid, r, c):
        return grid[r * grid._cols + c]

    def _kernel_box(self, weights, cell=0.36, label_size=12):
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

    def _conv2d_raw(self, x, k):
        H, W = x.shape
        kH, kW = k.shape
        out = np.zeros((H - kH + 1, W - kW + 1))
        for r in range(out.shape[0]):
            for c in range(out.shape[1]):
                out[r, c] = float((x[r:r + kH, c:c + kW] * k).sum())
        return out

    def _relu(self, x):
        return np.maximum(0, x)

    def _norm(self, x):
        m = np.abs(x).max()
        if m > 0:
            return x / m
        return x

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

        fmap_h_raw = self._conv2d_raw(digit, K_HORIZ)
        fmap_v_raw = self._conv2d_raw(digit, K_VERT)
        fmap_l_raw = self._conv2d_raw(digit, K_LAPL)

        # Normalize raw values for visualization of negative values
        fmap_h_raw_norm = fmap_h_raw / (np.abs(fmap_h_raw).max() + 1e-9)

        fmap_h = self._norm(self._relu(fmap_h_raw)) ** 0.85
        fmap_v = self._norm(self._relu(fmap_v_raw)) ** 0.85
        fmap_l = self._norm(self._relu(fmap_l_raw)) ** 0.85

        title = Text("Stages of a Convolutional Neural Network (CNN)",
                     font_size=28, color=TEAL_C, weight=BOLD)
        title.to_edge(UP, buff=0.30)
        self.play(Write(title), run_time=0.7)

        # ═════════════════════════════════════════════════════════════════════
        # STEP 1 — Input Layer
        # ═════════════════════════════════════════════════════════════════════
        act1 = Text("Step 1: Input Layer",
                    font_size=18, color=YELLOW)
        act1.next_to(title, DOWN, buff=0.10)
        self.play(FadeIn(act1), run_time=0.55)

        IN_CELL = 0.30
        img = self._grid(digit, cell=IN_CELL, fill_color=BLUE_C,
                         stroke_color="#222244", stroke_width=0.35)
        img.move_to(ORIGIN)
        img_lbl = Text("Input image (12x12 pixels)", font_size=16, color=BLUE_C)
        img_lbl.next_to(img, UP, buff=0.18)
        self.play(FadeIn(img), FadeIn(img_lbl), run_time=0.7)
        self.wait(1.5)

        # ═════════════════════════════════════════════════════════════════════
        # STEP 2 — Convolution Layer
        # ═════════════════════════════════════════════════════════════════════
        self.play(FadeOut(act1), run_time=0.3)
        act2 = Text("Step 2: Convolution Layer",
                    font_size=18, color=YELLOW)
        act2.next_to(title, DOWN, buff=0.10)
        self.play(FadeIn(act2), run_time=0.55)

        img.generate_target()
        img.target.move_to(LEFT * 4.5 + DOWN * 0.15)
        img_lbl.generate_target()
        img_lbl.target.next_to(img.target, UP, buff=0.18).scale(0.85)
        self.play(MoveToTarget(img), MoveToTarget(img_lbl), run_time=0.6)

        kernel_box = self._kernel_box(K_HORIZ, cell=0.42, label_size=14)
        kernel_box.move_to(ORIGIN + UP * 1.3)
        kernel_lbl = Text("3x3 filter / kernel\n(horizontal-edge detector)",
                          font_size=12, color=YELLOW)
        kernel_lbl.next_to(kernel_box, UP, buff=0.12)
        self.play(FadeIn(kernel_box), FadeIn(kernel_lbl), run_time=0.5)

        FM_CELL = IN_CELL 
        oH, oW = fmap_h.shape
        
        # Display feature map with raw (un-ReLU'd) values first
        fmap_grid = self._grid_signed(np.zeros_like(fmap_h_raw_norm),
                                      cell=FM_CELL, pos_color=BLUE_C,
                                      neg_color=RED_C, zero_color=GRAY_D)
        fmap_grid.move_to(RIGHT * 4.4 + DOWN * 0.15)
        fmap_lbl = Text(f"Convolution map {oH}x{oW}",
                        font_size=13, color=YELLOW)
        fmap_lbl.next_to(fmap_grid, UP, buff=0.18)
        self.play(FadeIn(fmap_grid), FadeIn(fmap_lbl), run_time=0.5)

        legend_pos = VGroup(
            Square(side_length=0.18, fill_color=BLUE_C, fill_opacity=0.6,
                   stroke_color=BLUE_C, stroke_width=1.0),
            Text("positive", font_size=10, color=BLUE_C),
        ).arrange(RIGHT, buff=0.08)
        legend_neg = VGroup(
            Square(side_length=0.18, fill_color=RED_C, fill_opacity=0.6,
                   stroke_color=RED_C, stroke_width=1.0),
            Text("negative", font_size=10, color=RED_C),
        ).arrange(RIGHT, buff=0.08)
        legend = VGroup(legend_pos, legend_neg).arrange(DOWN, buff=0.12)
        legend.scale(0.9)
        legend.next_to(fmap_grid, DOWN, buff=0.20)
        legend.align_to(fmap_grid, LEFT)
        self.play(FadeIn(legend), run_time=0.3)

        rf = Rectangle(width=IN_CELL * 3, height=IN_CELL * 3,
                       stroke_color=YELLOW, stroke_width=3.5, fill_opacity=0)
        rf.move_to(self._gcell(img, 1, 1).get_center())
        out_hl = Square(side_length=FM_CELL, stroke_color=GREEN,
                        stroke_width=2.5, fill_opacity=0)
        out_hl.move_to(self._gcell(fmap_grid, 0, 0).get_center())
        self.play(FadeIn(rf), FadeIn(out_hl), run_time=0.3)

        slow = [(0, 0), (1, 4), (4, 4), (7, 7)]
        for r, c in slow:
            val = fmap_h_raw_norm[r, c]
            col = BLUE_C if val > 0 else RED_C
            self.play(
                rf.animate.move_to(self._gcell(img, r + 1, c + 1).get_center()),
                out_hl.animate.move_to(self._gcell(fmap_grid, r, c).get_center()),
                run_time=0.55,
            )
            self.play(self._light_cell(fmap_grid, r, c, abs(val), col), run_time=0.22)

        demo_r, demo_c = 4, 4
        demo_patch = digit[demo_r:demo_r + 3, demo_c:demo_c + 3]
        demo_raw = float((demo_patch * K_HORIZ).sum())
        demo_patch_grid = self._number_grid(demo_patch, cell=0.36, fmt="{:.1f}", font_size=10)
        demo_patch_lbl = Text("3x3 patch", font_size=11, color=BLUE_C)
        demo_patch_group = VGroup(demo_patch_grid, demo_patch_lbl).arrange(DOWN, buff=0.08)
        demo_kernel_grid = self._number_grid(K_HORIZ, cell=0.36, fmt="{:+.0f}", sign_colors=True, font_size=11)
        demo_kernel_lbl = Text("Kernel", font_size=11, color=YELLOW)
        demo_kernel_group = VGroup(demo_kernel_grid, demo_kernel_lbl).arrange(DOWN, buff=0.08)
        demo_sum = Text(f"Sum = {demo_raw:+.2f}", font_size=13, color=WHITE)
        demo_panel = VGroup(
            demo_patch_group,
            Text("x", font_size=16, color=GRAY_B),
            demo_kernel_group,
            Text("=", font_size=16, color=GRAY_B),
            demo_sum,
        ).arrange(RIGHT, buff=0.18)
        demo_panel.scale(0.75)
        demo_panel.to_edge(DOWN, buff=0.55).shift(LEFT * 0.3)

        self.play(
            rf.animate.move_to(self._gcell(img, demo_r + 1, demo_c + 1).get_center()),
            out_hl.animate.move_to(self._gcell(fmap_grid, demo_r, demo_c).get_center()),
            FadeOut(legend),
            run_time=0.5,
        )
        self.play(FadeIn(demo_panel), run_time=0.6)
        self.wait(2.0)
        self.play(FadeOut(demo_panel), run_time=0.4)

        # Row-by-row sweep — fills the rest in reading order.
        for r in range(oH):
            row_anims = []
            last_c_in_row = -1
            for c in range(oW):
                if (r, c) in slow:
                    continue
                val = fmap_h_raw_norm[r, c]
                col = BLUE_C if val > 0 else RED_C
                row_anims.append(self._light_cell(fmap_grid, r, c, abs(val), col))
                last_c_in_row = c
            if not row_anims:
                continue
            self.play(
                rf.animate.move_to(self._gcell(img, r + 1, last_c_in_row + 1).get_center()),
                out_hl.animate.move_to(self._gcell(fmap_grid, r, last_c_in_row).get_center()),
                LaggedStart(*row_anims, lag_ratio=0.18),
                run_time=0.32,
            )

        self.play(FadeOut(rf), FadeOut(out_hl), run_time=0.4)

        # ═════════════════════════════════════════════════════════════════════
        # STEP 3 — Activation Function (ReLU)
        # ═════════════════════════════════════════════════════════════════════
        self.play(FadeOut(act2), FadeOut(kernel_lbl), run_time=0.3)
        act3 = Text("Step 3: Activation Function (ReLU)",
                    font_size=18, color=YELLOW)
        act3.next_to(title, DOWN, buff=0.10)
        self.play(FadeIn(act3), run_time=0.55)

        relu_lbl = Text("ReLU(x) = max(0, x)   —   negatives clipped to 0",
                        font_size=14, color=WHITE)
        relu_lbl.to_edge(DOWN, buff=0.30)
        self.play(FadeIn(relu_lbl), run_time=0.5)

        relu_demo = fmap_h_raw[2:5, 2:5]
        relu_demo_out = self._relu(relu_demo)
        relu_raw_grid = self._number_grid(relu_demo, cell=0.34, fmt="{:+.1f}", sign_colors=True, font_size=10)
        relu_out_grid = self._number_grid(relu_demo_out, cell=0.34, fmt="{:+.1f}", sign_colors=True, font_size=10)
        relu_raw_lbl = Text("Before", font_size=10, color=RED_C)
        relu_out_lbl = Text("After", font_size=10, color=GREEN)
        relu_raw_group = VGroup(relu_raw_grid, relu_raw_lbl).arrange(DOWN, buff=0.08)
        relu_out_group = VGroup(relu_out_grid, relu_out_lbl).arrange(DOWN, buff=0.08)
        relu_arrow = Arrow(relu_raw_group.get_right(), relu_out_group.get_left(),
                   buff=0.12, color=GRAY_C, stroke_width=1.2, tip_length=0.12)
        relu_tag = Text("ReLU", font_size=11, color=GRAY_B)
        relu_tag.next_to(relu_arrow, UP, buff=0.06)
        relu_demo_group = VGroup(relu_raw_group, relu_arrow, relu_out_group, relu_tag)
        relu_demo_group.arrange(RIGHT, buff=0.20)
        relu_demo_group.to_edge(DOWN, buff=0.40)
        self.play(FadeOut(relu_lbl), FadeIn(relu_demo_group), run_time=0.6)
        self.wait(1.4)
        self.play(FadeOut(relu_demo_group), run_time=0.4)

        # Apply ReLU: negatives fade out, positives keep blue color-coding.
        relu_grid = self._grid(fmap_h, cell=FM_CELL, fill_color=BLUE_C,
                               stroke_color=GRAY_D, stroke_width=0.4)
        relu_grid.move_to(fmap_grid.get_center())
        self.play(Transform(fmap_grid, relu_grid), run_time=1.4)
        self.wait(0.8)

        fmap_lbl_relu = Text(f"Activated map (ReLU) {oH}x{oW}",
                             font_size=13, color=BLUE_C)
        fmap_lbl_relu.next_to(fmap_grid, UP, buff=0.18)
        self.play(Transform(fmap_lbl, fmap_lbl_relu), run_time=0.4)
        fmap_lbl = fmap_lbl_relu

        # Show multiple kernels quickly
        k1_tag = Text("horizontal\nedges", font_size=11, color=BLUE_C, weight=BOLD)
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

        def build_row(K, fmap, color, name, y):
            kbox = self._kernel_box(K, cell=0.42 * ROW_SCALE, label_size=10)
            kbox.move_to(LEFT * 0.2 + UP * y)
            tag = Text(name, font_size=11, color=color, weight=BOLD)
            tag.next_to(kbox, LEFT, buff=0.18)
            fg = self._grid(fmap, cell=FM_CELL * ROW_SCALE, fill_color=color)
            fg.move_to(RIGHT * 3.0 + UP * y)
            flbl = Text(f"{name}", font_size=11, color=color)
            flbl.next_to(fg, UP, buff=0.10)
            return VGroup(kbox, tag), VGroup(fg, flbl)

        kpair_2, fpair_2 = build_row(K_VERT, fmap_v, ORANGE, "vertical\nedges", 0.0)
        kpair_3, fpair_3 = build_row(K_LAPL, fmap_l, "#9D7BFF", "Laplacian\n(omni)", -1.9)

        self.play(FadeIn(kpair_2), FadeIn(fpair_2), run_time=0.7)
        self.play(FadeIn(kpair_3), FadeIn(fpair_3), run_time=0.7)
        self.wait(1.5)

        # ═════════════════════════════════════════════════════════════════════
        # STEP 4 — Pooling Layer (Max Pooling)
        # ═════════════════════════════════════════════════════════════════════
        self.play(FadeOut(act3), run_time=0.2)
        act4 = Text("Step 4: Pooling Layer (Max Pooling)",
                    font_size=18, color=YELLOW)
        act4.next_to(title, DOWN, buff=0.10)
        self.play(FadeIn(act4), run_time=0.55)

        self.play(
            FadeOut(img), FadeOut(img_lbl),
            FadeOut(kernel_pair_1), FadeOut(kpair_2), FadeOut(kpair_3),
            run_time=0.5,
        )

        self.play(
            fmap_pair_1.animate.move_to(LEFT * 4.5 + UP * 1.9),
            fpair_2.animate.move_to(LEFT * 4.5 + UP * 0.0),
            fpair_3.animate.move_to(LEFT * 4.5 + DOWN * 1.9),
            run_time=0.7,
        )

        pool_h = self._maxpool(fmap_h, k=2)
        pool_v = self._maxpool(fmap_v, k=2)
        pool_l = self._maxpool(fmap_l, k=2)
        POOL_CELL = 0.26
        pg1 = self._grid(pool_h, cell=POOL_CELL, fill_color=BLUE_C)
        pg2 = self._grid(pool_v, cell=POOL_CELL, fill_color=ORANGE)
        pg3 = self._grid(pool_l, cell=POOL_CELL, fill_color="#9D7BFF")
        pg1.move_to(LEFT * 1.7 + UP * 1.9)
        pg2.move_to(LEFT * 1.7 + UP * 0.0)
        pg3.move_to(LEFT * 1.7 + DOWN * 1.9)
        pa1 = Arrow(fmap_pair_1.get_right(), pg1.get_left(), buff=0.15,
                    color=GRAY_C, stroke_width=1.5, tip_length=0.13)

        # Mini-demo of max-pool 2x2 over the horizontal feature map
        demo_pr, demo_pc = 2, 4
        win_cells = VGroup(*[self._gcell(fmap_grid, demo_pr + dr, demo_pc + dc)
                             for dr in range(2) for dc in range(2)])
        pool_window = SurroundingRectangle(win_cells, color=YELLOW,
                                           stroke_width=3, buff=0.01)
        demo_patch_p = fmap_h[demo_pr:demo_pr + 2, demo_pc:demo_pc + 2]
        pmax = float(demo_patch_p.max())
        ppatch_grid = self._number_grid(demo_patch_p, cell=0.34, fmt="{:.2f}",
                                        font_size=10)
        ppatch_lbl = Text("2x2 patch", font_size=10, color=BLUE_C)
        ppatch_group = VGroup(ppatch_grid, ppatch_lbl).arrange(DOWN, buff=0.06)
        pmax_box = Square(side_length=0.34, fill_color=GREEN, fill_opacity=0.35,
                          stroke_color=GREEN, stroke_width=1.2)
        pmax_text = Text(f"{pmax:.2f}", font_size=11, color=WHITE)
        pmax_text.move_to(pmax_box.get_center())
        pmax_grp = VGroup(pmax_box, pmax_text)
        pmax_lbl = Text("max", font_size=10, color=GREEN)
        pmax_full = VGroup(pmax_grp, pmax_lbl).arrange(DOWN, buff=0.06)
        ppanel = VGroup(
            ppatch_group,
            Text("→", font_size=16, color=GRAY_B),
            pmax_full,
        ).arrange(RIGHT, buff=0.20)
        ppanel_caption = Text("Max-Pool 2x2: keep the largest of every 2x2 patch",
                              font_size=12, color=GRAY_B)
        ppanel_full = VGroup(ppanel_caption, ppanel).arrange(DOWN, buff=0.10)
        ppanel_full.scale(0.95)
        ppanel_full.to_edge(DOWN, buff=0.45)

        self.play(GrowArrow(pa1), FadeIn(pg1), run_time=0.6)
        self.play(FadeIn(pool_window), FadeIn(ppanel_full), run_time=0.6)
        self.wait(2.0)
        self.play(FadeOut(pool_window), FadeOut(ppanel_full), run_time=0.4)

        # Now the other two: same operation
        pa2 = Arrow(fpair_2.get_right(), pg2.get_left(), buff=0.15,
                    color=GRAY_C, stroke_width=1.5, tip_length=0.13)
        pa3 = Arrow(fpair_3.get_right(), pg3.get_left(), buff=0.15,
                    color=GRAY_C, stroke_width=1.5, tip_length=0.13)
        same_op_lbl = Text("(same operation applied to each map)",
                           font_size=12, color=GRAY_B)
        same_op_lbl.to_edge(DOWN, buff=0.50)
        self.play(GrowArrow(pa2), GrowArrow(pa3),
                  FadeIn(pg2), FadeIn(pg3),
                  FadeIn(same_op_lbl),
                  run_time=0.7)
        self.wait(1.5)
        self.play(FadeOut(same_op_lbl), run_time=0.3)

        # ═════════════════════════════════════════════════════════════════════
        # STEP 5 — Fully Connected Layers (Flatten -> Dense)
        # ═════════════════════════════════════════════════════════════════════
        self.play(
            FadeOut(act4),
            FadeOut(fmap_pair_1), FadeOut(fpair_2), FadeOut(fpair_3),
            FadeOut(pa1), FadeOut(pa2), FadeOut(pa3),
            run_time=0.5,
        )
        act5 = Text("Step 5: Fully Connected Layers (Dense)",
                    font_size=18, color=YELLOW)
        act5.next_to(title, DOWN, buff=0.10)
        self.play(FadeIn(act5), run_time=0.55)

        self.play(
            pg1.animate.move_to(LEFT * 4.5 + UP * 1.9),
            pg2.animate.move_to(LEFT * 4.5 + UP * 0.0),
            pg3.animate.move_to(LEFT * 4.5 + DOWN * 1.9),
            run_time=0.6,
        )

        flat_n = 24
        flat_col = VGroup(*[
            Circle(radius=0.10,
                   fill_color=BLUE_C if i < 8 else ORANGE if i < 16 else PURPLE_C,
                   fill_opacity=0.65, stroke_width=1)
            for i in range(flat_n)
        ])
        flat_col.arrange(DOWN, buff=0.04).move_to(LEFT * 2.0)
        flat_lbl = Text("Flatten\n75 values\n(compressed view)",
                        font_size=10, color=GRAY_B)
        flat_lbl.next_to(flat_col, LEFT, buff=0.18)

        # Each pooled map flows into a different third of the flatten column.
        flat_top = flat_col[3].get_center()
        flat_mid = flat_col[flat_n // 2].get_center()
        flat_bot = flat_col[flat_n - 4].get_center()
        flat_arrows = VGroup(
            Arrow(pg1.get_right(), flat_top, buff=0.15, color=GRAY_C,
                  stroke_width=2.0, tip_length=0.14),
            Arrow(pg2.get_right(), flat_mid, buff=0.15, color=GRAY_C,
                  stroke_width=2.0, tip_length=0.14),
            Arrow(pg3.get_right(), flat_bot, buff=0.15, color=GRAY_C,
                  stroke_width=2.0, tip_length=0.14),
        )
        self.play(GrowArrow(flat_arrows[0]), GrowArrow(flat_arrows[1]),
                  GrowArrow(flat_arrows[2]), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(c, scale=0.5) for c in flat_col],
                              lag_ratio=0.04),
                  FadeIn(flat_lbl), run_time=0.8)

        dense_col = VGroup(*[
            Circle(radius=0.13, fill_color=PURPLE_B, fill_opacity=0.40,
                   stroke_color=PURPLE_B, stroke_width=1.2)
            for _ in range(8)
        ])
        dense_col.arrange(DOWN, buff=0.10).move_to(LEFT * 0.1)
        dense_lbl = Text("Dense\n(Fully Connected)", font_size=11, color=PURPLE_B)
        dense_lbl.next_to(dense_col, UP, buff=0.14)
        dense_note = Text("Combines features\nfor the decision",
                          font_size=10, color=GRAY_B)
        dense_note.next_to(dense_col, DOWN, buff=0.12)

        # Truly fully-connected: every flatten cell to every dense neuron.
        ftd = VGroup()
        for f in flat_col:
            for d in dense_col:
                ftd.add(Line(f.get_center(), d.get_center(),
                             stroke_color=GRAY_C, stroke_width=0.6,
                             stroke_opacity=0.22))
        self.play(Create(ftd), run_time=0.7)
        self.play(LaggedStart(*[FadeIn(d, scale=0.5) for d in dense_col],
                              lag_ratio=0.05),
                  FadeIn(dense_lbl), FadeIn(dense_note), run_time=0.7)

        # ═════════════════════════════════════════════════════════════════════
        # STEP 6 — Output Layer (Softmax)
        # ═════════════════════════════════════════════════════════════════════
        self.play(FadeOut(act5), run_time=0.3)
        act6 = Text("Step 6: Output Layer (Softmax)", font_size=18, color=YELLOW)
        act6.next_to(title, DOWN, buff=0.10)
        self.play(FadeIn(act6), FadeOut(dense_note), run_time=0.6)

        out_col = VGroup()
        out_lbls = VGroup()
        for i in range(10):
            color = GREEN if i == 8 else GRAY_C
            n = Circle(radius=0.13, fill_color=color, fill_opacity=0.35, stroke_color=color, stroke_width=1.5)
            out_col.add(n)
            l = Text(str(i), font_size=12, color=color)
            out_lbls.add(l)
        out_col.arrange(DOWN, buff=0.13).move_to(RIGHT * 2.2)
        for n, l in zip(out_col, out_lbls):
            l.next_to(n, LEFT, buff=0.07)
        out_top_lbl = Text("Classes\n(Softmax)", font_size=11, color=GREEN)
        out_top_lbl.next_to(out_col, UP, buff=0.14)
        softmax_note = Text("Softmax: normalizes to\nprobabilities (sum to 1)",
                    font_size=10, color=GRAY_B)
        softmax_note.next_to(out_col, DOWN, buff=0.12)

        dto = VGroup()
        for d in dense_col:
            for o in out_col:
                dto.add(Line(d.get_center(), o.get_center(),
                             stroke_color=GRAY_C, stroke_width=0.6,
                             stroke_opacity=0.22))
        self.play(Create(dto), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(n, scale=0.5) for n in out_col], lag_ratio=0.04),
                                    FadeIn(out_lbls), FadeIn(out_top_lbl), FadeIn(softmax_note), run_time=0.7)

        # Softmax formula briefly displayed
        softmax_formula = MathTex(
            r"\mathrm{softmax}(z_i) = \frac{e^{z_i}}{\sum_j e^{z_j}}",
            font_size=28, color=GREEN,
        )
        softmax_formula.to_edge(DOWN, buff=0.55)
        self.play(Write(softmax_formula), run_time=1.0)
        self.wait(1.2)

        probs = [0, 0, 1, 1, 0, 0, 0, 0, 98, 0]
        prob_nums = VGroup()
        for i, (n, p) in enumerate(zip(out_col, probs)):
            col = GREEN if i == 8 else GRAY_C
            t = Text(f"{p}%", font_size=11, color=col)
            t.next_to(n, RIGHT, buff=0.07)
            prob_nums.add(t)
        self.play(
            LaggedStart(*[FadeIn(t) for t in prob_nums], lag_ratio=0.05),
            run_time=0.8,
        )
        self.wait(0.6)
        self.play(FadeOut(softmax_formula), run_time=0.4)

        n8 = out_col[8]
        prob8 = prob_nums[8]
        self.play(
            n8.animate.set_fill(GREEN, opacity=1.0).scale(1.3),
            Flash(n8, color=GREEN, flash_radius=0.4, line_length=0.10),
            run_time=0.7,
        )
        # Reposition the 98% label so it doesn't collide with the enlarged neuron.
        self.play(
            prob8.animate.next_to(n8, RIGHT, buff=0.10).scale(1.15),
            run_time=0.3,
        )

        cap6 = Text("Softmax converts outputs into classification probabilities",
                    font_size=14, color=GREEN)
        cap6.to_edge(DOWN, buff=0.30)
        self.play(FadeIn(cap6), run_time=0.6)
        self.wait(3.0)

