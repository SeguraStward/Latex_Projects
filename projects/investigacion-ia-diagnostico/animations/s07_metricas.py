from manim import *
import numpy as np

Text.set_default(font="Noto Sans")


class S07_Metricas(Scene):
    """
    Acto 1 — El Espejismo de la Precision
    Acto 2 — Las Dos Balanzas (Sensibilidad y Especificidad)
    Acto 3 — Nace la Curva ROC
    Acto 4 — El AUC: la calificacion final
    """

    # ── helpers ───────────────────────────────────────────────────────────────

    def _dot_grid(self, n_green, n_red, cols=10, dot_r=0.09, spacing=0.32):
        """Grid de puntos: n_green verdes y n_red rojos (mezclados)."""
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
        # ACTO 1 — El Espejismo de la Precision
        # ══════════════════════════════════════════════════════════════════════
        act_lbl = Text("El Espejismo de la Precisión",
                       font_size=26, color=TEAL_C, weight=BOLD)
        act_lbl.to_edge(UP, buff=0.35)
        self.play(Write(act_lbl))

        # 100 puntos: 99 verdes + 1 rojo
        dots, red_indices = self._dot_grid(99, 1)
        dots.move_to(UP * 0.2)
        red_dot = dots[list(red_indices)[0]]

        self.play(
            LaggedStart(*[FadeIn(d, scale=0.5) for d in dots], lag_ratio=0.01),
            run_time=1.5,
        )
        self.wait(0.4)

        # Scanner barre de arriba a abajo pintando todo de verde
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

        # Mostrar "Precision: 99%"
        acc_text = Text("Precisión:", font_size=36, color=WHITE)
        acc_val = Text("99%", font_size=48, color=GREEN, weight=BOLD)
        acc_group = VGroup(acc_text, acc_val).arrange(RIGHT, buff=0.2)
        acc_group.to_edge(DOWN, buff=0.7)
        self.play(FadeIn(acc_group, shift=UP * 0.3), run_time=0.6)
        self.wait(0.8)

        # Zoom al punto rojo original — fue pintado de verde
        # Desplazar la cuadricula a la izquierda para dejar espacio a la etiqueta
        self.play(dots.animate.shift(LEFT * 2.0), run_time=0.5)
        self.play(
            red_dot.animate.scale(3.5).set_color(RED),
            run_time=0.7,
        )
        fn_lbl = Text("Falso Negativo:\nel tumor que se perdió",
                      font_size=16, color=RED, weight=BOLD)
        fn_lbl.move_to(RIGHT * 2.5 + UP * 0.2)
        self.play(FadeIn(fn_lbl, shift=LEFT * 0.2))
        self.wait(0.5)

        # "99%" se rompe: tiembla y se pone rojo
        self.play(
            acc_val.animate.set_color(RED),
            acc_val.animate.shift(RIGHT * 0.08),
            run_time=0.15,
        )
        self.play(acc_val.animate.shift(LEFT * 0.16), run_time=0.1)
        self.play(acc_val.animate.shift(RIGHT * 0.08), run_time=0.1)

        useless = Text("Alta precisión NO garantiza detectar enfermos",
                       font_size=15, color=RED)
        useless.to_edge(DOWN, buff=0.3)
        self.play(FadeIn(useless, shift=UP * 0.2))
        self.wait(1.5)

        self.play(
            FadeOut(dots), FadeOut(fn_lbl), FadeOut(acc_group), FadeOut(useless),
            run_time=0.5,
        )

        # ══════════════════════════════════════════════════════════════════════
        # ACTO 2 — Las Dos Balanzas
        # ══════════════════════════════════════════════════════════════════════
        act2 = Text("Las Dos Balanzas",
                    font_size=26, color=YELLOW, weight=BOLD)
        act2.to_edge(UP, buff=0.35)
        self.play(ReplacementTransform(act_lbl, act2))

        # Divisor
        div = Line(UP * 2.8, DOWN * 3.2, stroke_color=GRAY_D, stroke_width=1)
        self.play(Create(div), run_time=0.3)

        # ── Izquierda: Sensibilidad ────────────────────────────────────────
        sens_title = Text("Sensibilidad", font_size=22, color=GREEN, weight=BOLD)
        sens_title.move_to(LEFT * 3.2 + UP * 2.3)
        sens_sub = Text("Detectar a los enfermos", font_size=14, color=GRAY_B)
        sens_sub.next_to(sens_title, DOWN, buff=0.08)
        self.play(FadeIn(sens_title), FadeIn(sens_sub))

        sens_formula = MathTex(
            r"\text{Sensibilidad} = \frac{VP}{VP + FN}",
            font_size=26, color=GREEN,
        )
        sens_formula.move_to(LEFT * 3.2 + UP * 1.3)
        self.play(Write(sens_formula), run_time=0.8)

        # Puntos rojos (enfermos): algunos rodeados (VP), otros escapan (FN)
        vp_dots = VGroup(*[
            Dot(radius=0.1, color=RED, fill_opacity=0.85).move_to(
                LEFT * (4.5 - i * 0.45) + DOWN * 0.1)
            for i in range(6)
        ])
        vp_circles = VGroup(*[
            Circle(radius=0.16, stroke_color=GREEN, stroke_width=2, fill_opacity=0)
            .move_to(vp_dots[i].get_center())
            for i in range(4)           # solo 4 detectados (VP)
        ])
        fn_label = VGroup(*[
            Text("FN", font_size=9, color=RED).next_to(vp_dots[i], DOWN, buff=0.05)
            for i in range(4, 6)        # 2 no detectados
        ])
        vp_label = Text("VP: detectados", font_size=12, color=GREEN)
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

        # ── Derecha: Especificidad ─────────────────────────────────────────
        spec_title = Text("Especificidad", font_size=22, color=TEAL_C, weight=BOLD)
        spec_title.move_to(RIGHT * 3.2 + UP * 2.3)
        spec_sub = Text("Descartar a los sanos", font_size=14, color=GRAY_B)
        spec_sub.next_to(spec_title, DOWN, buff=0.08)
        self.play(FadeIn(spec_title), FadeIn(spec_sub))

        spec_formula = MathTex(
            r"\text{Especificidad} = \frac{VN}{VN + FP}",
            font_size=26, color=TEAL_C,
        )
        spec_formula.move_to(RIGHT * 3.2 + UP * 1.3)
        self.play(Write(spec_formula), run_time=0.8)

        # Puntos verdes (sanos): algunos correctamente ignorados (VN), otros FP
        vn_dots = VGroup(*[
            Dot(radius=0.1, color=GREEN, fill_opacity=0.85).move_to(
                RIGHT * (2.0 + i * 0.45) + DOWN * 0.1)
            for i in range(6)
        ])
        fp_circles = VGroup(*[
            Circle(radius=0.16, stroke_color=RED, stroke_width=2, fill_opacity=0)
            .move_to(vn_dots[i].get_center())
            for i in range(4, 6)        # 2 falsos positivos
        ])
        fp_label = VGroup(*[
            Text("FP", font_size=9, color=RED).next_to(vn_dots[i], DOWN, buff=0.05)
            for i in range(4, 6)
        ])
        vn_label = Text("VN: correctamente sanos", font_size=12, color=TEAL_C)
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

        # Umbral slider
        threshold = ValueTracker(0.0)          # posicion -1.0 a 1.0
        slider_line = Line(LEFT * 4.8, RIGHT * 4.8,
                           stroke_color=GRAY_D, stroke_width=0.8)
        slider_line.move_to(DOWN * 1.5)

        slider_handle = always_redraw(lambda: Line(
            DOWN * 1.5 + UP * 0.35 + RIGHT * threshold.get_value(),
            DOWN * 1.5 + DOWN * 0.35 + RIGHT * threshold.get_value(),
            stroke_color=YELLOW, stroke_width=3,
        ))
        thresh_lbl = Text("Umbral de Decisión", font_size=13, color=YELLOW)
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

        # Mover slider izquierda: mas sensibilidad, menos especificidad
        self.play(threshold.animate.set_value(-2.5), run_time=1.2)
        self.wait(0.5)
        # Mover slider derecha: mas especificidad, menos sensibilidad
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
        # ACTO 3 — Nace la Curva ROC
        # ══════════════════════════════════════════════════════════════════════
        act3 = Text("Curva ROC",
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

        x_label = Text("1 - Especificidad\n(Falsas alarmas)",
                       font_size=14, color=GRAY_B)
        x_label.next_to(axes.x_axis, DOWN, buff=0.25)
        y_label = Text("Sensibilidad\n(Detectar enfermos)",
                       font_size=14, color=GRAY_B)
        y_label.next_to(axes.y_axis, LEFT, buff=0.15)

        self.play(Create(axes), FadeIn(x_label), FadeIn(y_label), run_time=1.0)

        # Linea diagonal (adivinanza aleatoria)
        diagonal = axes.plot(lambda x: x, x_range=[0, 1],
                             color=GRAY_C, stroke_width=1.5)
        diag_lbl = Text("Adivinanza aleatoria", font_size=11, color=GRAY_C)
        diag_lbl.move_to(axes.c2p(0.72, 0.54))
        self.play(Create(diagonal), FadeIn(diag_lbl), run_time=0.8)
        self.wait(0.3)

        # Anotacion del eje X
        cost_note = Text(
            "Moverse por el eje X = pagar con falsas alarmas",
            font_size=13, color=ORANGE,
        )
        cost_note.to_edge(RIGHT, buff=0.3).shift(UP * 2.2)
        gain_note = Text(
            "Subir en el eje Y = ganar: detectar enfermos",
            font_size=13, color=GREEN,
        )
        gain_note.next_to(cost_note, DOWN, buff=0.2)
        self.play(FadeIn(cost_note, shift=LEFT * 0.2),
                  FadeIn(gain_note, shift=LEFT * 0.2), run_time=0.7)
        self.wait(0.5)

        # Curva ROC dibujandose (modelo bueno: y = x^0.3)
        roc_curve = axes.plot(
            lambda x: x ** 0.28,
            x_range=[0.001, 1],
            color=YELLOW,
            stroke_width=3,
        )
        self.play(Create(roc_curve), run_time=2.0, rate_func=linear)

        # Punto de operacion anotado
        op_point = Dot(axes.c2p(0.2, 0.78), color=YELLOW, radius=0.1)
        op_line_h = DashedLine(axes.c2p(0, 0.78), axes.c2p(0.2, 0.78),
                               stroke_color=GREEN, stroke_width=1.2, dash_length=0.08)
        op_line_v = DashedLine(axes.c2p(0.2, 0), axes.c2p(0.2, 0.78),
                               stroke_color=RED, stroke_width=1.2, dash_length=0.08)
        op_note = Text("78% sens.\n20% falsas alarmas",
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
        # ACTO 4 — El AUC: la Calificacion Final
        # ══════════════════════════════════════════════════════════════════════
        act4 = Text("La Calificación Final — AUC",
                    font_size=26, color=GREEN, weight=BOLD)
        act4.to_edge(UP, buff=0.35)
        self.play(ReplacementTransform(act3, act4))

        # Rellenar area bajo la curva ROC
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

        # ── Estado B: modelo inutil (curva → diagonal) ────────────────────
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
        useless_lbl = Text("Modelo inútil\n(igual que lanzar una moneda)",
                           font_size=14, color=RED)
        useless_lbl.to_edge(RIGHT, buff=0.4).shift(UP * 1.5)
        self.play(FadeIn(useless_lbl))
        self.wait(1.0)

        # ── Estado C: modelo perfecto (curva → angulo recto) ──────────────
        # Angulo recto: (0,0) → (0,1) → (1,1)
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
        perfect_lbl = Text("Modelo perfecto\n100% sensibilidad + 100% especificidad",
                           font_size=14, color=GREEN)
        perfect_lbl.to_edge(RIGHT, buff=0.4).shift(UP * 1.5)
        self.play(FadeIn(perfect_lbl))
        self.wait(0.8)

        # ── Volver al modelo real (AUC 0.932 del paper) ────────────────────
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

        # Desplazar el grafico a la izquierda para dejar espacio al caption
        chart_grp = VGroup(axes, x_label, y_label, diagonal, diag_lbl,
                           roc_curve, area, auc_group)
        self.play(chart_grp.animate.shift(LEFT * 1.5), run_time=0.7)

        # Caption final — lineas separadas para espaciado correcto
        cap_line1 = Text("AUC resume que tan bien", font_size=15, color=GRAY_A)
        cap_line2 = Text("el modelo separa enfermos", font_size=15, color=GRAY_A)
        cap_line3 = Text("de sanos a cualquier", font_size=15, color=GRAY_A)
        cap_line4 = Text("umbral de decision", font_size=15, color=GRAY_A)
        final_cap = VGroup(cap_line1, cap_line2, cap_line3, cap_line4)
        final_cap.arrange(DOWN, buff=0.22, aligned_edge=LEFT)
        final_cap.move_to(RIGHT * 4.5 + UP * 0.3)
        box = SurroundingRectangle(final_cap, color=YELLOW,
                                   buff=0.25, corner_radius=0.12,
                                   stroke_width=1.5)
        self.play(FadeIn(box), FadeIn(final_cap), run_time=0.8)
        self.wait(3.5)
