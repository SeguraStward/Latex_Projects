from manim import *
import numpy as np

Text.set_default(font="Noto Sans", line_spacing=1.1)


class S05_ImageNet_CAD(Scene):
    """
    Block 1 — ImageNet: the dataset that changed everything.
    Block 2 — CADe vs CADx: difference between detecting and diagnosing.
    """

    # ── internal helpers ─────────────────────────────────────────────────────

    def _image_card(self, label, color, width=0.9, height=0.75):
        """Card representing a classified ImageNet image."""
        bg = RoundedRectangle(width=width, height=height,
                              fill_color=color, fill_opacity=0.25,
                              stroke_color=color, stroke_width=1.2,
                              corner_radius=0.06)
        lbl = Text(label, font_size=9, color=color)
        lbl.move_to(bg.get_center())
        return VGroup(bg, lbl)

    def _fake_xray(self, width=2.8, height=3.2):
        """Simulated X-ray with anomalous area."""
        bg = Rectangle(width=width, height=height,
                       fill_color="#0a0a12", fill_opacity=1,
                       stroke_color="#222244", stroke_width=1.5)
        # Bones/ribs as lines
        ribs = VGroup(*[
            Arc(radius=0.9 + i * 0.28, start_angle=PI * 0.15,
                angle=PI * 0.7, stroke_color="#334455",
                stroke_width=1.2 - i * 0.1)
            for i in range(4)
        ])
        # Lung area
        lung_l = Ellipse(width=0.85, height=1.5,
                         fill_color="#152030", fill_opacity=0.8,
                         stroke_color="#1e3040", stroke_width=0.8)
        lung_r = Ellipse(width=0.85, height=1.5,
                         fill_color="#152030", fill_opacity=0.8,
                         stroke_color="#1e3040", stroke_width=0.8)
        lung_l.shift(LEFT * 0.55)
        lung_r.shift(RIGHT * 0.55)
        # Anomaly (nodule)
        nodule = Circle(radius=0.18, fill_color="#3a6080",
                        fill_opacity=0.85, stroke_color="#5090b0",
                        stroke_width=1.2)
        nodule.move_to(RIGHT * 0.45 + UP * 0.3)

        xray = VGroup(bg, ribs, lung_l, lung_r, nodule)
        return xray, nodule

    # ── construct ─────────────────────────────────────────────────────────────

    def construct(self):

        # ══════════════════════════════════════════════════════════════════════
        # BLOCK 1 — CADe vs CADx
        # ══════════════════════════════════════════════════════════════════════
        title = Text("CADe vs CADx: Detect vs Diagnose",
                     font_size=32, color=BLUE_B, weight=BOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title), run_time=0.9)

        # Central divider
        div = Line(UP * 3.2, DOWN * 3.2, stroke_color=GRAY_D,
                   stroke_width=1, stroke_opacity=0.5)
        self.play(Create(div), run_time=0.4)

        # ── LEFT SIDE — CADe ─────────────────────────────────────────────
        cade_title = Text("CADe", font_size=28, color=YELLOW, weight=BOLD)
        cade_sub = Text("Computer-Assisted\nDetection",
                        font_size=16, color=GRAY_B)
        cade_header = VGroup(cade_title, cade_sub).arrange(DOWN, buff=0.1)
        cade_header.move_to(LEFT * 3.2 + UP * 2.4)
        self.play(FadeIn(cade_header, shift=DOWN * 0.2))

        # Left X-ray
        xray_l, nodule_l = self._fake_xray(width=2.4, height=2.8)
        xray_l.scale(0.75).move_to(LEFT * 3.2 + DOWN * 0.2)
        nodule_center_l = nodule_l.get_center()
        self.play(FadeIn(xray_l), run_time=0.8)

        # Bounding box appears over the nodule
        bbox = Rectangle(width=0.55, height=0.55,
                         stroke_color=YELLOW, stroke_width=2.5, fill_opacity=0)
        bbox.move_to(nodule_center_l)
        det_lbl = Text("Nodule\ndetected", font_size=11, color=YELLOW)
        det_lbl.next_to(bbox, UP, buff=0.06)

        scan_line = Line(xray_l.get_left() + RIGHT * 0.05,
                         xray_l.get_right() + LEFT * 0.05,
                         stroke_color=YELLOW, stroke_width=1, stroke_opacity=0.6)
        scan_line.move_to(xray_l.get_top() + DOWN * 0.1)
        self.play(scan_line.animate.move_to(xray_l.get_bottom() + UP * 0.1),
                  run_time=1.0, rate_func=linear)
        self.play(Create(bbox), FadeIn(det_lbl), run_time=0.6)

        cade_obj = Text("Goal: reduce\nfalse negatives",
                        font_size=13, color=YELLOW)
        cade_obj.move_to(LEFT * 3.2 + DOWN * 2.5)
        self.play(FadeIn(cade_obj))

        # ── RIGHT SIDE — CADx ───────────────────────────────────────────
        cadx_title = Text("CADx", font_size=28, color=TEAL_C, weight=BOLD)
        cadx_sub = Text("Computer-Assisted\nDiagnosis",
                        font_size=16, color=GRAY_B)
        cadx_header = VGroup(cadx_title, cadx_sub).arrange(DOWN, buff=0.1)
        cadx_header.move_to(RIGHT * 3.2 + UP * 2.4)
        self.play(FadeIn(cadx_header, shift=DOWN * 0.2))

        # Right X-ray (same already-detected area, zoom)
        xray_r, nodule_r = self._fake_xray(width=2.4, height=2.8)
        xray_r.scale(0.75).move_to(RIGHT * 3.2 + DOWN * 0.2)
        nodule_center_r = nodule_r.get_center()

        bbox_r = Rectangle(width=0.55, height=0.55,
                            stroke_color=TEAL_C, stroke_width=2, fill_opacity=0)
        bbox_r.move_to(nodule_center_r)
        self.play(FadeIn(xray_r), Create(bbox_r), run_time=0.8)

        # Probability bars
        bar_labels = ["Benign", "Malignant"]
        bar_values = [0.15, 0.85]
        bar_colors = [GREEN, RED]
        bars_group = VGroup()
        for i, (lbl, val, col) in enumerate(zip(bar_labels, bar_values, bar_colors)):
            row_lbl = Text(lbl, font_size=12, color=col)
            bar_bg = Rectangle(width=1.8, height=0.22,
                               fill_color=GRAY_E, fill_opacity=0.3, stroke_width=0)
            bar_fill = Rectangle(width=1.8 * val, height=0.22,
                                 fill_color=col, fill_opacity=0.85, stroke_width=0)
            bar_fill.align_to(bar_bg, LEFT)
            pct = Text(f"{int(val * 100)}%", font_size=12, color=col, weight=BOLD)
            pct.next_to(bar_bg, RIGHT, buff=0.1)
            row = VGroup(row_lbl, VGroup(bar_bg, bar_fill), pct)
            row.arrange(RIGHT, buff=0.12)
            bars_group.add(row)

        bars_group.arrange(DOWN, buff=0.25)
        bars_group.move_to(RIGHT * 3.2 + DOWN * 2.0)
        self.play(LaggedStart(*[FadeIn(r) for r in bars_group], lag_ratio=0.3),
                  run_time=0.9)

        cadx_obj = Text("Goal: characterize\nthe pathology",
                        font_size=13, color=TEAL_C)
        cadx_obj.move_to(RIGHT * 3.2 + DOWN * 3.0)
        self.play(FadeIn(cadx_obj))

        # ── Final caption ─────────────────────────────────────────────────
        caption = Text(
            "CADe localizes the anomaly -- CADx evaluates its nature and severity",
            font_size=16, color=GRAY_A)
        caption_box = SurroundingRectangle(caption, color=GRAY_D,
                                           buff=0.15, corner_radius=0.1)
        caption_group = VGroup(caption_box, caption)
        caption_group.to_edge(DOWN, buff=0.25)
        self.play(FadeIn(caption_box), Write(caption), run_time=0.8)
        self.wait(2.5)

        # ══════════════════════════════════════════════════════════════════════
        # BLOCK 2 — ImageNet: the dataset that changed everything
        # ══════════════════════════════════════════════════════════════════════
        self.play(
            FadeOut(div), FadeOut(cade_header), FadeOut(xray_l),
            FadeOut(scan_line), FadeOut(bbox), FadeOut(det_lbl), FadeOut(cade_obj),
            FadeOut(cadx_header), FadeOut(xray_r), FadeOut(bbox_r),
            FadeOut(bars_group), FadeOut(cadx_obj),
            FadeOut(caption_box), FadeOut(caption),
            run_time=0.6,
        )

        title2 = Text("ImageNet: The Dataset That Changed Everything",
                      font_size=30, color=BLUE_B, weight=BOLD)
        title2.to_edge(UP, buff=0.4)
        self.play(ReplacementTransform(title, title2), run_time=0.7)

        # ── Card grid ────────────────────────────────────────────────────
        categories = [
            ("Dog",      BLUE_C),   ("Cat",    TEAL_C),
            ("Plane",    GREEN_C),  ("Chair",  YELLOW),
            ("Face",     ORANGE),   ("Car",    RED_C),
            ("Tree",     PURPLE_B), ("Bird",   BLUE_B),
            ("Flower",   PINK),     ("Boat",   TEAL_B),
            ("Mountain", GREEN_B),  ("Fish",   GOLD_C),
        ]

        cards = VGroup(*[
            self._image_card(lbl, col) for lbl, col in categories
        ])
        cards.arrange_in_grid(rows=3, cols=4, buff=0.18)
        cards.scale(0.85)
        cards.move_to(UP * 0.5)

        self.play(
            LaggedStart(*[FadeIn(c, shift=UP * 0.15) for c in cards],
                        lag_ratio=0.06),
            run_time=1.2,
        )

        # ── Centered statistics ───────────────────────────────────────────
        stat1 = Text("1.2M  images",     font_size=17, color=YELLOW, weight=BOLD)
        stat2 = Text("1000  categories", font_size=17, color=YELLOW, weight=BOLD)
        stats = VGroup(stat1, stat2)
        stats.arrange(RIGHT, buff=1.5)
        stats.move_to(DOWN * 1.55)
        self.play(FadeIn(stats, shift=UP * 0.1), run_time=0.5)

        # ── AlexNet badge ─────────────────────────────────────────────────
        alexnet_box = RoundedRectangle(
            width=4.0, height=1.05,
            fill_color="#0a1020", fill_opacity=0.9,
            stroke_color=ORANGE, stroke_width=1.8,
            corner_radius=0.12,
        )
        alexnet_box.move_to(DOWN * 2.75)

        alexnet_line1 = Text("AlexNet  --  2012", font_size=13,
                             color=ORANGE, weight=BOLD)
        alexnet_line2 = Text("Wins ImageNet with deep CNN",
                             font_size=12, color=GRAY_B)
        alexnet_txt = VGroup(alexnet_line1, alexnet_line2)
        alexnet_txt.arrange(DOWN, buff=0.12)
        alexnet_txt.move_to(alexnet_box.get_center())

        self.play(FadeIn(alexnet_box), FadeIn(alexnet_txt), run_time=0.5)
        self.wait(3.0)
