from manim import *

Text.set_default(font="Noto Sans")


class S09_Limitaciones(Scene):
    """
    Limitaciones y consideraciones eticas del uso de IA en medicina.
    Act 1 — Sesgo en los datos de entrenamiento
    Act 2 — El problema de la caja negra (explainabilidad)
    Act 3 — Privacidad, regulacion y responsabilidad
    """

    def construct(self):

        title = Text("Limitaciones y Ética", font_size=36, color=ORANGE, weight=BOLD)
        title.to_edge(UP, buff=0.35)
        self.play(Write(title), run_time=0.7)

        # ══════════════════════════════════════════════════════════════════════
        # ACT 1 — Sesgo en los datos
        # ══════════════════════════════════════════════════════════════════════
        act1_lbl = Text("1.  Sesgo en los Datos de Entrenamiento",
                        font_size=20, color=YELLOW, weight=BOLD)
        act1_lbl.next_to(title, DOWN, buff=0.28)
        self.play(FadeIn(act1_lbl, shift=DOWN * 0.1), run_time=0.5)

        # Barras de distribucion de dataset (sesgo demografico)
        groups  = ["Caucásico", "Latinoam.", "Asiático", "Africano"]
        values  = [72, 14, 9, 5]   # porcentajes aproximados
        colors  = [BLUE_C, TEAL_C, GREEN_C, PURPLE_B]
        x0      = -3.2   # x inicial (float)
        bar_w   = 0.65
        gap     = 1.15
        base_y  = -2.0   # y de la linea base (float)

        bars      = VGroup()
        bar_lbls  = VGroup()
        pct_lbls  = VGroup()

        for i, (g, v, c) in enumerate(zip(groups, values, colors)):
            bar_h = v * 0.045
            bar = Rectangle(
                width=bar_w, height=bar_h,
                fill_color=c, fill_opacity=0.85,
                stroke_color=c, stroke_width=1,
            )
            bar.move_to([x0 + i * gap, base_y + bar_h / 2, 0])

            grp_lbl = Text(g, font_size=11, color=c)
            grp_lbl.next_to(bar, DOWN, buff=0.1)

            pct_lbl = Text(f"{v}%", font_size=13, color=c, weight=BOLD)
            pct_lbl.next_to(bar, UP, buff=0.08)

            bars.add(bar)
            bar_lbls.add(grp_lbl)
            pct_lbls.add(pct_lbl)

        axis_line = Line(
            [x0 - 0.3, base_y, 0],
            [x0 + (len(groups) - 1) * gap + 0.6, base_y, 0],
            stroke_color=GRAY_D, stroke_width=1,
        )

        self.play(Create(axis_line), run_time=0.3)
        self.play(
            LaggedStart(*[GrowFromEdge(b, DOWN) for b in bars], lag_ratio=0.15),
            run_time=1.0,
        )
        self.play(FadeIn(bar_lbls), FadeIn(pct_lbls), run_time=0.5)

        # Resaltar la barra dominante
        self.play(bars[0].animate.set_fill(RED, opacity=0.95), run_time=0.4)

        bias_note = Text("El modelo aprende peor para los grupos minoritarios",
                         font_size=14, color=RED)
        bias_note.move_to(RIGHT * 2.2 + DOWN * 0.5)
        bias_box = SurroundingRectangle(bias_note, color=RED, buff=0.14,
                                        stroke_width=1.2)
        self.play(FadeIn(bias_note), Create(bias_box), run_time=0.5)
        self.wait(1.2)

        self.play(
            FadeOut(act1_lbl), FadeOut(bars), FadeOut(bar_lbls),
            FadeOut(pct_lbls), FadeOut(axis_line),
            FadeOut(bias_note), FadeOut(bias_box),
            run_time=0.5,
        )

        # ══════════════════════════════════════════════════════════════════════
        # ACT 2 — Caja negra
        # ══════════════════════════════════════════════════════════════════════
        act2_lbl = Text("2.  El Problema de la Caja Negra",
                        font_size=20, color=ORANGE, weight=BOLD)
        act2_lbl.next_to(title, DOWN, buff=0.28)
        self.play(FadeIn(act2_lbl, shift=DOWN * 0.1), run_time=0.5)

        # Imagen de entrada
        img_bg = Rectangle(width=1.2, height=1.2,
                           fill_color="#101525", fill_opacity=1,
                           stroke_color=BLUE_C, stroke_width=1.5)
        img_bg.move_to(LEFT * 4.5 + DOWN * 0.3)
        img_txt = Text("Imagen\nMédica", font_size=12, color=BLUE_C)
        img_txt.move_to(img_bg.get_center())

        # Caja negra
        bbox_nn = Rectangle(width=2.8, height=1.8,
                            fill_color="#040408", fill_opacity=1,
                            stroke_color=GRAY_C, stroke_width=2)
        bbox_nn.move_to(DOWN * 0.3)
        q_mark = Text("?", font_size=70, color=GRAY_C, weight=BOLD)
        q_mark.move_to(bbox_nn.get_center())
        nn_lbl = Text("Red Neuronal  —  700M parámetros", font_size=11, color=GRAY_C)
        nn_lbl.next_to(bbox_nn, DOWN, buff=0.14)

        # Salida
        out_bg = RoundedRectangle(width=1.6, height=0.9,
                                  fill_color="#0a1a0a", fill_opacity=1,
                                  stroke_color=GREEN, stroke_width=1.5,
                                  corner_radius=0.1)
        out_bg.move_to(RIGHT * 4.5 + DOWN * 0.3)
        out_txt = Text("Maligno\n94.7%", font_size=14, color=GREEN, weight=BOLD)
        out_txt.move_to(out_bg.get_center())

        arr_in  = Arrow(img_bg.get_right(), bbox_nn.get_left(),
                        buff=0.1, color=GRAY_C, stroke_width=2, tip_length=0.18)
        arr_out = Arrow(bbox_nn.get_right(), out_bg.get_left(),
                        buff=0.1, color=GREEN, stroke_width=2, tip_length=0.18)

        self.play(FadeIn(img_bg), FadeIn(img_txt), run_time=0.4)
        self.play(FadeIn(bbox_nn), FadeIn(q_mark), FadeIn(nn_lbl), run_time=0.5)
        self.play(GrowArrow(arr_in), GrowArrow(arr_out), run_time=0.5)
        self.play(FadeIn(out_bg), FadeIn(out_txt), run_time=0.4)

        why_txt = Text("¿Por qué esta decisión?", font_size=17, color=RED, weight=BOLD)
        why_txt.move_to(UP * 2.1)
        self.play(FadeIn(why_txt, shift=DOWN * 0.2), run_time=0.4)

        xai_note = Text("Solución: XAI — Grad-CAM y SHAP visualizan qué activa la red",
                        font_size=13, color=YELLOW)
        xai_note.to_edge(DOWN, buff=0.45)
        self.play(FadeIn(xai_note, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(act2_lbl), FadeOut(img_bg), FadeOut(img_txt),
            FadeOut(bbox_nn), FadeOut(q_mark), FadeOut(nn_lbl),
            FadeOut(arr_in), FadeOut(arr_out),
            FadeOut(out_bg), FadeOut(out_txt),
            FadeOut(why_txt), FadeOut(xai_note),
            run_time=0.5,
        )

        # ══════════════════════════════════════════════════════════════════════
        # ACT 3 — Privacidad, regulacion y responsabilidad
        # ══════════════════════════════════════════════════════════════════════
        act3_lbl = Text("3.  Privacidad, Regulación y Responsabilidad",
                        font_size=20, color=RED, weight=BOLD)
        act3_lbl.next_to(title, DOWN, buff=0.28)
        self.play(FadeIn(act3_lbl, shift=DOWN * 0.1), run_time=0.5)

        concerns = [
            ("Privacidad",       "Datos clínicos sensibles\nbajo GDPR e HIPAA",  BLUE_C,   LEFT * 3.5),
            ("Regulación",       "FDA / CE Mark\naprobación 3–7 años",            YELLOW,   ORIGIN),
            ("Responsabilidad",  "Si el modelo falla,\n¿quién responde?",         RED,      RIGHT * 3.5),
        ]

        concern_objs = VGroup()
        for name, desc, color, pos in concerns:
            circle = Circle(radius=0.88, fill_color=color,
                            fill_opacity=0.12, stroke_color=color, stroke_width=2)
            circle.move_to(pos + UP * 0.5)
            name_txt = Text(name, font_size=12, color=color, weight=BOLD)
            name_txt.move_to(circle.get_center())
            desc_txt = Text(desc, font_size=11, color=GRAY_B, line_spacing=1.2)
            desc_txt.move_to(pos + DOWN * 1.1)

            concern_objs.add(circle, name_txt, desc_txt)
            self.play(
                Create(circle), FadeIn(name_txt), FadeIn(desc_txt),
                run_time=0.55,
            )

        self.wait(1.0)

        # Declaracion de cierre
        close_txt = Text(
            "La IA es apoyo al médico, no su reemplazo",
            font_size=17, color=TEAL_C, weight=BOLD,
        )
        close_txt.to_edge(DOWN, buff=0.55)
        close_box = SurroundingRectangle(close_txt, color=TEAL_C,
                                         buff=0.18, stroke_width=1.5)
        self.play(FadeIn(close_txt), Create(close_box), run_time=0.6)
        self.wait(3.0)
