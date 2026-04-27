from manim import *

Text.set_default(font="Noto Sans", line_spacing=1.1)


class S06_Arquitecturas(Scene):
    """
    Key architectures in medical diagnosis:
    AlexNet  -- classification (tumor yes/no?)
    U-Net    -- pixel-to-pixel segmentation
    ResNet   -- deep networks with residual connections
    """

    # ── helpers ───────────────────────────────────────────────────────────────

    def _layer_block(self, label, width, height, color, fill_opacity=0.2):
        rect = Rectangle(width=width, height=height,
                         fill_color=color, fill_opacity=fill_opacity,
                         stroke_color=color, stroke_width=2)
        lbl = Text(label, font_size=10, color=color)
        lbl.move_to(rect.get_center())
        return VGroup(rect, lbl)

    def _conv_arrow(self, start, end, color=GRAY_C):
        return Arrow(start, end, buff=0.05, color=color,
                     stroke_width=1.5, tip_length=0.14)

    # ── AlexNet ───────────────────────────────────────────────────────────────

    def _build_alexnet(self, origin):
        """Linear chain of blocks: image -> conv -> pool -> FC -> class."""
        blocks_data = [
            ("Input\n224x224",  0.55, 1.8, BLUE_C),
            ("Conv\nPool",      0.55, 1.5, TEAL_C),
            ("Conv\nPool",      0.55, 1.2, TEAL_C),
            ("Conv\nConv\nPool",0.55, 1.0, TEAL_D),
            ("FC\n4096",        0.55, 0.8, PURPLE_B),
            ("FC\n4096",        0.55, 0.8, PURPLE_B),
            ("Softmax\n1000",   0.55, 0.65,GREEN_C),
        ]
        group = VGroup()
        arrows = VGroup()
        prev_block = None
        for i, (lbl, w, h, col) in enumerate(blocks_data):
            block = self._layer_block(lbl, w, h, col)
            block.move_to(origin + RIGHT * i * 0.75)
            group.add(block)
            if prev_block:
                arrows.add(self._conv_arrow(
                    prev_block.get_right(), block.get_left(), GRAY_C))
            prev_block = block
        return group, arrows

    # ── U-Net ─────────────────────────────────────────────────────────────────

    def _build_unet(self, origin):
        """
        Encoder goes down (left->center), decoder goes up (center->right),
        horizontal skip connections.
        """
        enc_data = [
            ("64",  1.4, 0.35, TEAL_C),
            ("128", 1.1, 0.35, TEAL_C),
            ("256", 0.8, 0.35, TEAL_D),
            ("512", 0.5, 0.35, BLUE_D),
        ]
        bottleneck = self._layer_block("1024", 0.4, 0.35, BLUE_C)
        dec_data = list(reversed([
            ("512", 0.5, 0.35, PURPLE_B),
            ("256", 0.8, 0.35, PURPLE_B),
            ("128", 1.1, 0.35, PURPLE_C),
            ("64",  1.4, 0.35, GREEN_C),
        ]))

        enc_blocks = VGroup()
        dec_blocks = VGroup()
        all_arrows = VGroup()
        skip_arrows = VGroup()

        # Position encoder (left column, going down)
        x_enc = -2.0
        for i, (lbl, w, h, col) in enumerate(enc_data):
            b = self._layer_block(lbl, w, h, col)
            b.move_to(origin + LEFT * x_enc * (-1) + UP * (1.2 - i * 0.7))
            enc_blocks.add(b)

        # Bottleneck (center bottom)
        bottleneck.move_to(origin + DOWN * 1.7)

        # Position decoder (right column, going up)
        x_dec = 2.0
        for i, (lbl, w, h, col) in enumerate(dec_data):
            b = self._layer_block(lbl, w, h, col)
            b.move_to(origin + RIGHT * x_dec + UP * (-1.05 + i * 0.7))
            dec_blocks.add(b)

        # Encoder arrows going down
        for i in range(len(enc_blocks) - 1):
            all_arrows.add(self._conv_arrow(
                enc_blocks[i].get_bottom(),
                enc_blocks[i + 1].get_top(), TEAL_C))
        all_arrows.add(self._conv_arrow(
            enc_blocks[-1].get_bottom(), bottleneck.get_top(), BLUE_D))

        # Decoder arrows going up
        all_arrows.add(self._conv_arrow(
            bottleneck.get_top(), dec_blocks[0].get_bottom(), PURPLE_B))
        for i in range(len(dec_blocks) - 1):
            all_arrows.add(self._conv_arrow(
                dec_blocks[i].get_top(),
                dec_blocks[i + 1].get_bottom(), PURPLE_B))

        # Skip connections (encoder -> decoder same level)
        for eb, db in zip(enc_blocks, reversed(dec_blocks)):
            sk = DashedLine(eb.get_right(), db.get_left(),
                            stroke_color=YELLOW, stroke_width=1.2,
                            dash_length=0.1, stroke_opacity=0.7)
            skip_arrows.add(sk)

        group = VGroup(enc_blocks, bottleneck, dec_blocks)
        return group, all_arrows, skip_arrows

    # ── ResNet block ──────────────────────────────────────────────────────────

    def _build_resnet_block(self, origin):
        """Residual block: x -> F(x) -> x + F(x)."""
        # Input
        inp = Circle(radius=0.22, fill_color=BLUE_C, fill_opacity=0.4,
                     stroke_color=BLUE_C, stroke_width=1.8)
        inp.move_to(origin + LEFT * 2.2)
        inp_lbl = Text("x", font_size=14, color=BLUE_C)
        inp_lbl.move_to(inp.get_center())

        # Two conv layers
        conv1 = self._layer_block("Conv\nBN\nReLU", 0.65, 0.7, TEAL_C)
        conv1.move_to(origin + LEFT * 0.6)
        conv2 = self._layer_block("Conv\nBN", 0.65, 0.7, TEAL_C)
        conv2.move_to(origin + RIGHT * 0.6)

        # Sum
        plus_circle = Circle(radius=0.2, fill_color="#111122", fill_opacity=1,
                              stroke_color=ORANGE, stroke_width=2)
        plus_circle.move_to(origin + RIGHT * 1.8)
        plus_sym = Text("+", font_size=16, color=ORANGE)
        plus_sym.move_to(plus_circle.get_center())

        # Output
        out = Circle(radius=0.22, fill_color=GREEN_C, fill_opacity=0.4,
                     stroke_color=GREEN_C, stroke_width=1.8)
        out.move_to(origin + RIGHT * 3.0)
        out_lbl = Text("y", font_size=14, color=GREEN_C)
        out_lbl.move_to(out.get_center())

        # Main arrows
        arrows = VGroup(
            Arrow(inp.get_right(), conv1.get_left(), buff=0.05,
                  color=GRAY_C, stroke_width=1.5, tip_length=0.13),
            Arrow(conv1.get_right(), conv2.get_left(), buff=0.05,
                  color=GRAY_C, stroke_width=1.5, tip_length=0.13),
            Arrow(conv2.get_right(), plus_circle.get_left(), buff=0.05,
                  color=GRAY_C, stroke_width=1.5, tip_length=0.13),
            Arrow(plus_circle.get_right(), out.get_left(), buff=0.05,
                  color=GREEN_C, stroke_width=1.5, tip_length=0.13),
        )

        # Residual connection (skip): arc over the top
        skip_path = CubicBezier(
            inp.get_top(),
            inp.get_top() + UP * 0.7,
            plus_circle.get_top() + UP * 0.7,
            plus_circle.get_top(),
            stroke_color=YELLOW, stroke_width=2,
        )
        skip_lbl = Text("x (identity)", font_size=11, color=YELLOW)
        skip_lbl.move_to(origin + UP * 0.95)

        formula = MathTex(r"y = F(x) + x", font_size=22, color=ORANGE)
        formula.move_to(origin + DOWN * 0.9)

        group = VGroup(inp, inp_lbl, conv1, conv2, plus_circle, plus_sym, out, out_lbl)
        return group, arrows, skip_path, skip_lbl, formula

    # ── construct ─────────────────────────────────────────────────────────────

    def construct(self):

        # ══════════════════════════════════════════════════════════════════════
        # AlexNet
        # ══════════════════════════════════════════════════════════════════════
        title = Text("Key Architectures in Medical Diagnosis",
                     font_size=32, color=BLUE_B, weight=BOLD)
        title.to_edge(UP, buff=0.35)
        self.play(Write(title), run_time=0.8)

        arch_lbl = Text("AlexNet -- Classification",
                        font_size=24, color=BLUE_C, weight=BOLD)
        arch_lbl.next_to(title, DOWN, buff=0.2)
        self.play(FadeIn(arch_lbl, shift=DOWN * 0.15))

        origin_alex = DOWN * 0.6 + LEFT * 2.0
        alex_blocks, alex_arrows = self._build_alexnet(origin_alex)

        # Input image (left)
        img_in = Rectangle(width=0.7, height=0.7,
                           fill_color="#152535", fill_opacity=1,
                           stroke_color=BLUE_C, stroke_width=1.5)
        img_in.next_to(alex_blocks[0], LEFT, buff=0.3)
        img_lbl = Text("Chest\nX-Ray", font_size=9, color=BLUE_C)
        img_lbl.move_to(img_in.get_center())
        img_arr = Arrow(img_in.get_right(), alex_blocks[0].get_left(),
                        buff=0.05, color=BLUE_C, stroke_width=1.5, tip_length=0.12)

        # Output (right)
        out_lbl = Text("Tumor: YES/NO\n(classification)", font_size=11, color=GREEN)
        out_lbl.next_to(alex_blocks[-1], RIGHT, buff=0.2)

        self.play(FadeIn(img_in), FadeIn(img_lbl), run_time=0.4)
        self.play(GrowArrow(img_arr), run_time=0.3)
        self.play(
            LaggedStart(*[FadeIn(b) for b in alex_blocks], lag_ratio=0.1),
            run_time=1.0,
        )
        self.play(
            LaggedStart(*[GrowArrow(a) for a in alex_arrows], lag_ratio=0.08),
            run_time=0.8,
        )
        self.play(FadeIn(out_lbl, shift=LEFT * 0.2))

        metric_alex = Text("90.2% accuracy in lung classification",
                           font_size=13, color=YELLOW)
        metric_alex.to_edge(DOWN, buff=0.35)
        self.play(FadeIn(metric_alex))
        self.wait(1.5)

        self.play(
            FadeOut(arch_lbl), FadeOut(alex_blocks), FadeOut(alex_arrows),
            FadeOut(img_in), FadeOut(img_lbl), FadeOut(img_arr),
            FadeOut(out_lbl), FadeOut(metric_alex),
            run_time=0.6,
        )

        # ══════════════════════════════════════════════════════════════════════
        # U-Net
        # ══════════════════════════════════════════════════════════════════════
        arch_lbl2 = Text("U-Net -- Segmentation", font_size=24,
                         color=TEAL_C, weight=BOLD)
        arch_lbl2.next_to(title, DOWN, buff=0.2)
        self.play(FadeIn(arch_lbl2, shift=DOWN * 0.15))

        unet_group, unet_arrows, skip_arrows = self._build_unet(DOWN * 0.3)

        self.play(
            LaggedStart(*[FadeIn(b) for b in unet_group], lag_ratio=0.06),
            run_time=1.2,
        )
        self.play(
            LaggedStart(*[GrowArrow(a) for a in unet_arrows], lag_ratio=0.06),
            run_time=0.9,
        )
        # Skip connections in yellow
        skip_lbl = Text("skip connections\n(recover spatial detail)",
                        font_size=12, color=YELLOW)
        skip_lbl.to_edge(RIGHT, buff=0.3).shift(UP * 0.5)
        self.play(
            LaggedStart(*[Create(s) for s in skip_arrows], lag_ratio=0.1),
            FadeIn(skip_lbl),
            run_time=0.9,
        )

        # Input / segmented output images
        img_in2 = Rectangle(width=0.55, height=0.55,
                             fill_color="#152535", fill_opacity=1,
                             stroke_color=TEAL_C, stroke_width=1.5)
        img_in2.next_to(unet_group, LEFT, buff=0.3).shift(UP * 1.15)
        seg_out = Rectangle(width=0.55, height=0.55,
                            fill_color="#153025", fill_opacity=1,
                            stroke_color=GREEN, stroke_width=1.5)
        # Simulated heart contour inside
        heart_contour = Circle(radius=0.18, fill_opacity=0,
                               stroke_color=GREEN, stroke_width=1.5)
        heart_contour.move_to(seg_out.get_center())
        seg_out_group = VGroup(seg_out, heart_contour)
        seg_out_group.next_to(unet_group, RIGHT, buff=0.3).shift(UP * 1.15)

        in_arr2 = Arrow(img_in2.get_right(),
                        unet_group[0][-1].get_left(), buff=0.05,
                        color=TEAL_C, stroke_width=1.2, tip_length=0.12)
        out_arr2 = Arrow(unet_group[2][-1].get_right(),
                         seg_out.get_left(), buff=0.05,
                         color=GREEN, stroke_width=1.2, tip_length=0.12)

        self.play(FadeIn(img_in2), GrowArrow(in_arr2),
                  FadeIn(seg_out_group), GrowArrow(out_arr2), run_time=0.7)

        metric_unet = Text("Pixel-to-pixel prediction -- High Dice coefficient in cardiac segmentation",
                           font_size=13, color=YELLOW)
        metric_unet.to_edge(DOWN, buff=0.35)
        self.play(FadeIn(metric_unet))
        self.wait(1.8)

        self.play(
            FadeOut(arch_lbl2), FadeOut(unet_group), FadeOut(unet_arrows),
            FadeOut(skip_arrows), FadeOut(skip_lbl),
            FadeOut(img_in2), FadeOut(in_arr2),
            FadeOut(seg_out_group), FadeOut(out_arr2),
            FadeOut(metric_unet),
            run_time=0.6,
        )

        # ══════════════════════════════════════════════════════════════════════
        # ResNet
        # ══════════════════════════════════════════════════════════════════════
        arch_lbl3 = Text("ResNet -- Residual Connections",
                         font_size=24, color=PURPLE_B, weight=BOLD)
        arch_lbl3.next_to(title, DOWN, buff=0.2)
        self.play(FadeIn(arch_lbl3, shift=DOWN * 0.15))

        res_group, res_arrows, skip_path, skip_lbl_r, formula = \
            self._build_resnet_block(DOWN * 0.3)

        self.play(
            LaggedStart(*[FadeIn(m) for m in res_group], lag_ratio=0.08),
            run_time=1.0,
        )
        self.play(
            LaggedStart(*[GrowArrow(a) for a in res_arrows], lag_ratio=0.1),
            run_time=0.8,
        )
        # Skip in yellow (the key of ResNet)
        self.play(Create(skip_path), FadeIn(skip_lbl_r), run_time=0.7)
        self.play(Write(formula), run_time=0.7)

        # Problem it solves
        problem = VGroup(
            Text("Without skip:  gradient vanishes in deep networks",
                 font_size=13, color=RED),
            Text("With skip:  50-150+ layer networks without degradation",
                 font_size=13, color=GREEN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        problem.to_edge(DOWN, buff=0.6)
        self.play(LaggedStart(*[FadeIn(p, shift=UP * 0.15) for p in problem],
                               lag_ratio=0.4), run_time=0.8)

        metric_res = Text("AUC 93.2% in glioma classification",
                          font_size=14, color=YELLOW, weight=BOLD)
        metric_res.to_edge(DOWN, buff=0.25)
        self.play(FadeIn(metric_res))
        self.wait(2.0)

        # ── Final comparison table ────────────────────────────────────────
        self.play(
            FadeOut(arch_lbl3), FadeOut(res_group), FadeOut(res_arrows),
            FadeOut(skip_path), FadeOut(skip_lbl_r), FadeOut(formula),
            FadeOut(problem), FadeOut(metric_res),
            run_time=0.6,
        )

        table_title = Text("Comparison", font_size=26, color=BLUE_B, weight=BOLD)
        table_title.next_to(title, DOWN, buff=0.2)
        self.play(FadeIn(table_title))

        rows = [
            ("Architecture", "Main task",      "Technical key",          GRAY_A),
            ("AlexNet",      "Classification", "Conv. layers + FC",       BLUE_C),
            ("U-Net",        "Segmentation",   "Encoder/Decoder + skip",  TEAL_C),
            ("ResNet",       "High accuracy",  "Residual connections",    PURPLE_B),
        ]
        col_x = [-3.0, -0.2, 2.6]
        table_group = VGroup()
        for r_idx, (arch, task, key, col) in enumerate(rows):
            y = 1.2 - r_idx * 0.72
            is_header = r_idx == 0
            fs = 14 if is_header else 15
            weight = BOLD if is_header else NORMAL
            for c_idx, text in enumerate([arch, task, key]):
                t = Text(text, font_size=fs, color=col, weight=weight)
                t.move_to(RIGHT * col_x[c_idx] + UP * y)
                table_group.add(t)

        # Header separator line
        sep = Line(LEFT * 4.5, RIGHT * 4.5, stroke_color=GRAY_D, stroke_width=1)
        sep.move_to(UP * 0.78)

        self.play(
            LaggedStart(*[FadeIn(t, shift=RIGHT * 0.1) for t in table_group],
                        lag_ratio=0.04),
            Create(sep),
            run_time=1.4,
        )
        self.wait(3.0)
