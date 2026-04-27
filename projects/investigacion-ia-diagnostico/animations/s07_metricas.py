from manim import *
import numpy as np

Text.set_default(font="Noto Sans", line_spacing=1.1)


class S07_Metricas(Scene):
    """
    Act 1 — The Accuracy Illusion
    Act 2 — The Two Scales (Sensitivity and Specificity)
    Act 3 — The ROC Curve is Born
    Act 4 — The AUC: the final score
    """

    # ── helpers ───────────────────────────────────────────────────────────────

    def _dot_grid(self, n_green, n_red, cols=10, dot_r=0.09, spacing=0.32):
        """Grid of dots: n_green green and n_red red (mixed)."""
        total = n_green + n_red
        rows = (total + cols - 1) // cols
        np.random.seed(3)
        indices = list(range(total))
        red_indices = set(np.random.choice(indices, n_red, replace=False))

        dots = VGroup()
        for idx in range(total):
            r, c = divmod(idx, cols)
            color = RED if idx in red_indices else GREEN
            d = Dot(radius=dot_r, color=color, fill_opacity=0.85)
            d.move_to(RIGHT * (c - (cols - 1) / 2) * spacing +
                      DOWN * (r - (rows - 1) / 2) * spacing)
            dots.add(d)
        return dots, red_indices

    # ── construct ─────────────────────────────────────────────────────────────

    def construct(self):

        # ══════════════════════════════════════════════════════════════════════
        # ACT 1 — The Accuracy Illusion
        # ══════════════════════════════════════════════════════════════════════
        act_lbl = Text("The Accuracy Illusion",
                       font_size=26, color=TEAL_C, weight=BOLD)
        act_lbl.to_edge(UP, buff=0.35)
        self.play(Write(act_lbl))

        # 100 dots: 99 green + 1 red
        dots, red_indices = self._dot_grid(99, 1)
        dots.move_to(UP * 0.2)
        red_dot = dots[list(red_indices)[0]]

        self.play(
            LaggedStart(*[FadeIn(d, scale=0.5) for d in dots], lag_ratio=0.01),
            run_time=1.5,
        )
        self.wait(0.4)

        # Scanner sweeps top to bottom painting everything green
        scanner = Rectangle(
            width=dots.width + 0.3, height=0.28,
            fill_color=GREEN, fill_opacity=0.18,
            stroke_color=GREEN, stroke_width=1.2,
        )
        scanner.move_to(dots.get_top() + UP * 0.15)
        self.play(FadeIn(scanner), run_time=0.3)
        self.play(
            scanner.animate.move_to(dots.get_bottom() + DOWN * 0.15),
            *[d.animate.set_color(GREEN) for d in dots],
            run_time=1.6, rate_func=linear,
        )
        self.play(FadeOut(scanner), run_time=0.2)

        # Show "Accuracy: 99%"
        acc_text = Text("Accuracy:", font_size=36, color=WHITE)
        acc_val = Text("99%", font_size=48, color=GREEN, weight=BOLD)
        acc_group = VGroup(acc_text, acc_val).arrange(RIGHT, buff=0.2)
        acc_group.to_edge(DOWN, buff=0.7)
        self.play(FadeIn(acc_group, shift=UP * 0.3), run_time=0.6)
        self.wait(0.8)

        # Zoom to the original red dot — it was painted green
        # Shift the grid to the left to leave space for the label
        self.play(dots.animate.shift(LEFT * 2.0), run_time=0.5)
        self.play(
            red_dot.animate.scale(3.5).set_color(RED),
            run_time=0.7,
        )
        fn_lbl = Text("False Negative:\nthe missed tumor",
                      font_size=16, color=RED, weight=BOLD)
        fn_lbl.move_to(RIGHT * 2.5 + UP * 0.2)
        self.play(FadeIn(fn_lbl, shift=LEFT * 0.2))
        self.wait(0.5)

        # "99%" breaks: shakes and turns red
        self.play(
            acc_val.animate.set_color(RED),
            acc_val.animate.shift(RIGHT * 0.08),
            run_time=0.15,
        )
        self.play(acc_val.animate.shift(LEFT * 0.16), run_time=0.1)
        self.play(acc_val.animate.shift(RIGHT * 0.08), run_time=0.1)

        useless = Text("High accuracy does NOT guarantee detecting sick patients",
                       font_size=15, color=RED)
        useless.to_edge(DOWN, buff=0.3)
        self.play(FadeIn(useless, shift=UP * 0.2))
        self.wait(1.5)

        self.play(
            FadeOut(dots), FadeOut(fn_lbl), FadeOut(acc_group), FadeOut(useless),
            run_time=0.5,
        )

        # ══════════════════════════════════════════════════════════════════════
        # ACT 2 — The Two Scales
        # ══════════════════════════════════════════════════════════════════════
        act2 = Text("The Two Scales",
                    font_size=26, color=YELLOW, weight=BOLD)
        act2.to_edge(UP, buff=0.35)
        self.play(ReplacementTransform(act_lbl, act2))

        # Divider
        div = Line(UP * 2.8, DOWN * 3.2, stroke_color=GRAY_D, stroke_width=1)
        self.play(Create(div), run_time=0.3)

        # ── Left: Sensitivity ─────────────────────────────────────────────
        sens_title = Text("Sensitivity", font_size=22, color=GREEN, weight=BOLD)
        sens_title.move_to(LEFT * 3.2 + UP * 2.3)
        sens_sub = Text("Detecting the sick", font_size=14, color=GRAY_B)
        sens_sub.next_to(sens_title, DOWN, buff=0.08)
        self.play(FadeIn(sens_title), FadeIn(sens_sub))

        sens_formula = MathTex(
            r"\text{Sensitivity} = \frac{TP}{TP + FN}",
            font_size=26, color=GREEN,
        )
        sens_formula.move_to(LEFT * 3.2 + UP * 1.3)
        self.play(Write(sens_formula), run_time=0.8)

        # Red dots (sick): some circled (TP), others escape (FN)
        vp_dots = VGroup(*[
            Dot(radius=0.1, color=RED, fill_opacity=0.85).move_to(
                LEFT * (4.5 - i * 0.45) + DOWN * 0.1)
            for i in range(6)
        ])
        vp_circles = VGroup(*[
            Circle(radius=0.16, stroke_color=GREEN, stroke_width=2, fill_opacity=0)
            .move_to(vp_dots[i].get_center())
            for i in range(4)           # only 4 detected (TP)
        ])
        fn_label = VGroup(*[
            Text("FN", font_size=9, color=RED).next_to(vp_dots[i], DOWN, buff=0.05)
            for i in range(4, 6)        # 2 undetected
        ])
        vp_label = Text("TP: detected", font_size=12, color=GREEN)
        vp_label.move_to(LEFT * 3.2 + DOWN * 0.55)

        self.play(
            LaggedStart(*[FadeIn(d) for d in vp_dots], lag_ratio=0.1),
            run_time=0.6,
        )
        self.play(
            LaggedStart(*[Create(c) for c in vp_circles], lag_ratio=0.12),
            FadeIn(fn_label), FadeIn(vp_label),
            run_time=0.8,
        )

        # ── Right: Specificity ────────────────────────────────────────────
        spec_title = Text("Specificity", font_size=22, color=TEAL_C, weight=BOLD)
        spec_title.move_to(RIGHT * 3.2 + UP * 2.3)
        spec_sub = Text("Ruling out healthy patients", font_size=14, color=GRAY_B)
        spec_sub.next_to(spec_title, DOWN, buff=0.08)
        self.play(FadeIn(spec_title), FadeIn(spec_sub))

        spec_formula = MathTex(
            r"\text{Specificity} = \frac{TN}{TN + FP}",
            font_size=26, color=TEAL_C,
        )
        spec_formula.move_to(RIGHT * 3.2 + UP * 1.3)
        self.play(Write(spec_formula), run_time=0.8)

        # Green dots (healthy): some correctly ignored (TN), others FP
        vn_dots = VGroup(*[
            Dot(radius=0.1, color=GREEN, fill_opacity=0.85).move_to(
                RIGHT * (2.0 + i * 0.45) + DOWN * 0.1)
            for i in range(6)
        ])
        fp_circles = VGroup(*[
            Circle(radius=0.16, stroke_color=RED, stroke_width=2, fill_opacity=0)
            .move_to(vn_dots[i].get_center())
            for i in range(4, 6)        # 2 false positives
        ])
        fp_label = VGroup(*[
            Text("FP", font_size=9, color=RED).next_to(vn_dots[i], DOWN, buff=0.05)
            for i in range(4, 6)
        ])
        vn_label = Text("TN: correctly healthy", font_size=12, color=TEAL_C)
        vn_label.move_to(RIGHT * 3.2 + DOWN * 0.55)

        self.play(
            LaggedStart(*[FadeIn(d) for d in vn_dots], lag_ratio=0.1),
            run_time=0.6,
        )
        self.play(
            LaggedStart(*[Create(c) for c in fp_circles], lag_ratio=0.12),
            FadeIn(fp_label), FadeIn(vn_label),
            run_time=0.8,
        )

        # Threshold slider
        threshold = ValueTracker(0.0)          # position -1.0 to 1.0
        slider_line = Line(LEFT * 4.8, RIGHT * 4.8,
                           stroke_color=GRAY_D, stroke_width=0.8)
        slider_line.move_to(DOWN * 1.5)

        slider_handle = always_redraw(lambda: Line(
            DOWN * 1.5 + UP * 0.35 + RIGHT * threshold.get_value(),
            DOWN * 1.5 + DOWN * 0.35 + RIGHT * threshold.get_value(),
            stroke_color=YELLOW, stroke_width=3,
        ))
        thresh_lbl = Text("Decision Threshold", font_size=13, color=YELLOW)
        thresh_lbl.next_to(slider_line, DOWN, buff=0.12)

        sens_pct = always_redraw(lambda: Text(
            f"Sens: {int(85 + threshold.get_value() * (-15))}%",
            font_size=14, color=GREEN,
        ).move_to(LEFT * 3.2 + DOWN * 1.1))

        spec_pct = always_redraw(lambda: Text(
            f"Spec: {int(70 + threshold.get_value() * 15)}%",
            font_size=14, color=TEAL_C,
        ).move_to(RIGHT * 3.2 + DOWN * 1.1))

        self.play(Create(slider_line), Create(slider_handle),
                  FadeIn(thresh_lbl), run_time=0.5)
        self.add(sens_pct, spec_pct)
        self.wait(0.3)

        # Move slider left: more sensitivity, less specificity
        self.play(threshold.animate.set_value(-2.5), run_time=1.2)
        self.wait(0.5)
        # Move slider right: more specificity, less sensitivity
        self.play(threshold.animate.set_value(2.5), run_time=1.5)
        self.wait(0.5)
        self.play(threshold.animate.set_value(0.0), run_time=0.8)
        self.wait(0.8)

        self.play(
            FadeOut(div), FadeOut(sens_title), FadeOut(sens_sub),
            FadeOut(sens_formula), FadeOut(vp_dots), FadeOut(vp_circles),
            FadeOut(fn_label), FadeOut(vp_label),
            FadeOut(spec_title), FadeOut(spec_sub),
            FadeOut(spec_formula), FadeOut(vn_dots), FadeOut(fp_circles),
            FadeOut(fp_label), FadeOut(vn_label),
            FadeOut(slider_line), FadeOut(slider_handle), FadeOut(thresh_lbl),
            FadeOut(sens_pct), FadeOut(spec_pct),
            run_time=0.6,
        )

        # ══════════════════════════════════════════════════════════════════════
        # ACT 3 — The ROC Curve is Born
        # ══════════════════════════════════════════════════════════════════════
        act3 = Text("ROC Curve",
                    font_size=26, color=ORANGE, weight=BOLD)
        act3.to_edge(UP, buff=0.35)
        self.play(ReplacementTransform(act2, act3))

        axes = Axes(
            x_range=[0, 1, 0.5],
            y_range=[0, 1, 0.5],
            x_length=5.5,
            y_length=5.5,
            axis_config={"color": GRAY_C, "stroke_width": 1.8,
                         "include_ticks": True},
            tips=False,
        )
        axes.move_to(DOWN * 0.15)

        x_label = Text("1 - Specificity\n(False alarms)",
                       font_size=14, color=GRAY_B)
        x_label.next_to(axes.x_axis, DOWN, buff=0.25)
        y_label = Text("Sensitivity\n(Detecting sick)",
                       font_size=14, color=GRAY_B)
        y_label.next_to(axes.y_axis, LEFT, buff=0.15)

        self.play(Create(axes), FadeIn(x_label), FadeIn(y_label), run_time=1.0)

        # Diagonal line (random guess)
        diagonal = axes.plot(lambda x: x, x_range=[0, 1],
                             color=GRAY_C, stroke_width=1.5)
        diag_lbl = Text("Random guess", font_size=11, color=GRAY_C)
        diag_lbl.move_to(axes.c2p(0.72, 0.54))
        self.play(Create(diagonal), FadeIn(diag_lbl), run_time=0.8)
        self.wait(0.3)

        # X-axis annotation
        cost_note = Text(
            "Moving along X axis = paying with false alarms",
            font_size=13, color=ORANGE,
        )
        cost_note.to_edge(RIGHT, buff=0.3).shift(UP * 2.2)
        gain_note = Text(
            "Moving up Y axis = gain: detecting sick",
            font_size=13, color=GREEN,
        )
        gain_note.next_to(cost_note, DOWN, buff=0.2)
        self.play(FadeIn(cost_note, shift=LEFT * 0.2),
                  FadeIn(gain_note, shift=LEFT * 0.2), run_time=0.7)
        self.wait(0.5)

        # ROC curve drawing itself (good model: y = x^0.3)
        roc_curve = axes.plot(
            lambda x: x ** 0.28,
            x_range=[0.001, 1],
            color=YELLOW,
            stroke_width=3,
        )
        self.play(Create(roc_curve), run_time=2.0, rate_func=linear)

        # Annotated operating point
        op_point = Dot(axes.c2p(0.2, 0.78), color=YELLOW, radius=0.1)
        op_line_h = DashedLine(axes.c2p(0, 0.78), axes.c2p(0.2, 0.78),
                               stroke_color=GREEN, stroke_width=1.2, dash_length=0.08)
        op_line_v = DashedLine(axes.c2p(0.2, 0), axes.c2p(0.2, 0.78),
                               stroke_color=RED, stroke_width=1.2, dash_length=0.08)
        op_note = Text("78% sens.\n20% false alarms",
                       font_size=12, color=YELLOW)
        op_note.next_to(op_point, UP, buff=0.12)

        self.play(
            Create(op_line_h), Create(op_line_v),
            FadeIn(op_point), FadeIn(op_note),
            run_time=0.8,
        )
        self.wait(1.5)

        self.play(
            FadeOut(cost_note), FadeOut(gain_note),
            FadeOut(op_point), FadeOut(op_line_h),
            FadeOut(op_line_v), FadeOut(op_note),
            run_time=0.5,
        )

        # ══════════════════════════════════════════════════════════════════════
        # ACT 4 — The AUC: the Final Score
        # ══════════════════════════════════════════════════════════════════════
        act4 = Text("The Final Score -- AUC",
                    font_size=26, color=GREEN, weight=BOLD)
        act4.to_edge(UP, buff=0.35)
        self.play(ReplacementTransform(act3, act4))

        # Fill area under the ROC curve
        area = axes.get_area(
            roc_curve,
            x_range=[0, 1],
            color=YELLOW,
            opacity=0.2,
        )
        self.play(FadeIn(area), run_time=0.8)

        auc_val = DecimalNumber(0.0, num_decimal_places=2, color=YELLOW,
                                font_size=32)
        auc_prefix = Text("AUC = ", font_size=28, color=YELLOW)
        auc_group = VGroup(auc_prefix, auc_val).arrange(RIGHT, buff=0.1)
        auc_group.move_to(axes.c2p(0.62, 0.28))

        self.play(FadeIn(auc_group), run_time=0.4)
        self.play(ChangeDecimalToValue(auc_val, 0.85), run_time=1.5)
        self.wait(0.8)

        # ── State B: useless model (curve -> diagonal) ────────────────────
        useless_curve = axes.plot(lambda x: x, x_range=[0, 1],
                                  color=RED, stroke_width=3)
        useless_area = axes.get_area(
            useless_curve, x_range=[0, 1], color=RED, opacity=0.12)

        self.play(
            Transform(roc_curve, useless_curve),
            Transform(area, useless_area),
            ChangeDecimalToValue(auc_val, 0.50),
            auc_val.animate.set_color(RED),
            auc_prefix.animate.set_color(RED),
            run_time=1.4,
        )
        useless_lbl = Text("Useless model\n(same as flipping a coin)",
                           font_size=14, color=RED)
        useless_lbl.to_edge(RIGHT, buff=0.4).shift(UP * 1.5)
        self.play(FadeIn(useless_lbl))
        self.wait(1.0)

        # ── State C: perfect model (curve -> right angle) ─────────────────
        # Right angle: (0,0) -> (0,1) -> (1,1)
        perfect_curve = axes.plot_line_graph(
            x_values=[0, 0, 1],
            y_values=[0, 1, 1],
            line_color=GREEN,
            stroke_width=3,
            add_vertex_dots=False,
        )
        perfect_area = axes.get_area(
            axes.plot(lambda x: 1.0, x_range=[0, 1]),
            x_range=[0, 1], color=GREEN, opacity=0.18,
        )

        self.play(
            FadeOut(useless_lbl),
            Transform(roc_curve, perfect_curve),
            Transform(area, perfect_area),
            ChangeDecimalToValue(auc_val, 1.00),
            auc_val.animate.set_color(GREEN),
            auc_prefix.animate.set_color(GREEN),
            run_time=1.6,
        )
        perfect_lbl = Text("Perfect model\n100% sensitivity + 100% specificity",
                           font_size=14, color=GREEN)
        perfect_lbl.to_edge(RIGHT, buff=0.4).shift(UP * 1.5)
        self.play(FadeIn(perfect_lbl))
        self.wait(0.8)

        # ── Return to real model (AUC 0.932 from the paper) ───────────────
        real_curve = axes.plot(
            lambda x: x ** 0.28, x_range=[0.001, 1],
            color=YELLOW, stroke_width=3,
        )
        real_area = axes.get_area(
            real_curve, x_range=[0, 1], color=YELLOW, opacity=0.2)

        self.play(
            FadeOut(perfect_lbl),
            Transform(roc_curve, real_curve),
            Transform(area, real_area),
            ChangeDecimalToValue(auc_val, 0.932),
            auc_val.animate.set_color(YELLOW),
            auc_prefix.animate.set_color(YELLOW),
            run_time=1.4,
        )

        # Shift chart to the left to make room for the caption
        chart_grp = VGroup(axes, x_label, y_label, diagonal, diag_lbl,
                           roc_curve, area, auc_group)
        self.play(chart_grp.animate.shift(LEFT * 1.5), run_time=0.7)

        # Final caption — separate lines for correct spacing
        cap_line1 = Text("AUC  summarizes  how  well", font_size=16, color=GRAY_A)
        cap_line2 = Text("the  model  separates  sick", font_size=16, color=GRAY_A)
        cap_line3 = Text("from  healthy  at  any", font_size=16, color=GRAY_A)
        cap_line4 = Text("decision  threshold", font_size=16, color=GRAY_A)
        final_cap = VGroup(cap_line1, cap_line2, cap_line3, cap_line4)
        final_cap.arrange(DOWN, buff=0.22, aligned_edge=LEFT)
        final_cap.move_to(RIGHT * 4.5 + UP * 0.3)
        box = SurroundingRectangle(final_cap, color=YELLOW,
                                   buff=0.25, corner_radius=0.12,
                                   stroke_width=1.5)
        self.play(FadeIn(box), FadeIn(final_cap), run_time=0.8)
        self.wait(3.5)
