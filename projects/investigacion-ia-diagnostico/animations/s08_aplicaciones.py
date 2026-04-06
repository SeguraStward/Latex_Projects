from manim import *

Text.set_default(font="Noto Sans")


class S08_Aplicaciones(Scene):
    """
    Aplicaciones reales de CNN en diagnóstico médico:
    5 casos concretos de implementación + impacto clínico.
    """

    def construct(self):

        title = Text("Aplicaciones Reales", font_size=36, color=BLUE_B, weight=BOLD)
        title.to_edge(UP, buff=0.35)
        self.play(Write(title), run_time=0.8)

        # ── 5 casos en lista con datos clave ─────────────────────────────────
        cases = [
            ("Viz.ai",       "Detección de ACV",           "AUC > 0.90",
             "1,600+ hospitales  ·  −66 min tratamiento",   TEAL_C),
            ("Mirai (MIT)",  "Riesgo cáncer de mama",      "C-index 0.69–0.78",
             "Validado en 5 países  ·  Predicción a 5 años", GREEN_C),
            ("Aidoc",        "Hemorragia intracraneal",    "Sens. > 90%",
             "Triaje automático  ·  Prioriza casos críticos", ORANGE),
            ("Qure.ai",     "Nódulos pulmonares",          "FDA cleared",
             "Segmentación en CT  ·  Cribado de cáncer",    BLUE_C),
            ("Shockmatrix", "Triaje en trauma",             "1,292 casos",
             "IA y médicos son complementarios",             PURPLE_B),
        ]

        all_cards = VGroup()

        for i, (name, task, metric, detail, color) in enumerate(cases):
            y_pos = 1.8 - i * 1.05

            # Card background
            card = RoundedRectangle(
                width=11.0, height=0.88, corner_radius=0.08,
                fill_color="#0a0d18", fill_opacity=0.75,
                stroke_color=color, stroke_width=1.3,
            )
            card.move_to(DOWN * (-y_pos))

            # Name badge
            name_txt = Text(name, font_size=15, color=color, weight=BOLD)
            name_txt.move_to(card.get_left() + RIGHT * 1.1)

            # Task
            task_txt = Text(task, font_size=13, color="#D0D0D0")
            task_txt.move_to(card.get_left() + RIGHT * 3.4)

            # Metric highlight
            metric_txt = Text(metric, font_size=14, color=color, weight=BOLD)
            metric_txt.move_to(card.get_left() + RIGHT * 5.8)

            # Detail
            detail_txt = Text(detail, font_size=10, color="#999999")
            detail_txt.move_to(card.get_left() + RIGHT * 8.8)

            grp = VGroup(card, name_txt, task_txt, metric_txt, detail_txt)
            all_cards.add(grp)

            self.play(
                FadeIn(card, shift=RIGHT * 0.3),
                FadeIn(name_txt), FadeIn(task_txt),
                FadeIn(metric_txt), FadeIn(detail_txt),
                run_time=0.45,
            )

        self.wait(1.5)

        # ── Impacto en la práctica clínica ────────────────────────────────────
        self.play(FadeOut(all_cards), run_time=0.5)

        impact_title = Text("Impacto Clínico",
                            font_size=22, color=TEAL_C, weight=BOLD)
        impact_title.move_to(UP * 2.2)
        self.play(FadeIn(impact_title, shift=DOWN * 0.2), run_time=0.5)

        items = [
            ("Triaje en tiempo real antes de que el radiólogo abra el caso",  TEAL_C),
            ("Reducción de 66 minutos en tratamiento de ACV",                 GREEN),
            ("Detección complementaria: IA y médicos se cubren mutuamente",   YELLOW),
            ("Cribado personalizado según riesgo individual",                  BLUE_C),
            ("873 algoritmos FDA autorizados en radiología (2025)",            ORANGE),
        ]

        impact_group = VGroup()
        for text, color in items:
            impact_group.add(Text(text, font_size=15, color=color))
        impact_group.arrange(DOWN, aligned_edge=LEFT, buff=0.30)
        impact_group.move_to(DOWN * 0.2)

        bullets = VGroup()
        for item in impact_group:
            b = Square(side_length=0.11, fill_color=TEAL_C,
                       fill_opacity=1, stroke_width=0)
            b.next_to(item, LEFT, buff=0.18)
            bullets.add(b)
            self.play(
                FadeIn(b, shift=RIGHT * 0.2),
                FadeIn(item, shift=RIGHT * 0.2),
                run_time=0.4,
            )

        self.wait(3.0)
