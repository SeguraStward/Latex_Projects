from manim import *

Text.set_default(font="Noto Sans")


class S08_Aplicaciones(Scene):
    """
    Aplicaciones reales de IA en diagnostico medico:
    Radiologia, Dermatologia, Oftalmologia, Patologia digital.
    Luego: impacto en la practica clinica.
    """

    # ── helpers de ilustraciones ──────────────────────────────────────────────

    def _chest_icon(self, color):
        """Radiografia de torax simulada."""
        bg = Rectangle(width=0.9, height=1.1,
                       fill_color="#060810", fill_opacity=1,
                       stroke_color=color, stroke_width=1)
        lung_l = Ellipse(width=0.28, height=0.62, fill_opacity=0,
                         stroke_color="#223322", stroke_width=0.8)
        lung_l.move_to(bg.get_center() + LEFT * 0.17)
        lung_r = Ellipse(width=0.28, height=0.62, fill_opacity=0,
                         stroke_color="#223322", stroke_width=0.8)
        lung_r.move_to(bg.get_center() + RIGHT * 0.17)
        nodule = Circle(radius=0.07, fill_color="#c0392b",
                        fill_opacity=0.9, stroke_width=0)
        nodule.move_to(bg.get_center() + RIGHT * 0.14 + UP * 0.18)
        return VGroup(bg, lung_l, lung_r, nodule)

    def _skin_icon(self, color):
        """Lesion de piel."""
        bg = Rectangle(width=0.9, height=0.9,
                       fill_color="#c8895a", fill_opacity=1,
                       stroke_color=color, stroke_width=1)
        mole = Ellipse(width=0.32, height=0.26, fill_color="#1a0c08",
                       fill_opacity=0.9, stroke_width=0)
        mole.move_to(bg.get_center())
        spot = Circle(radius=0.07, fill_color="#0d0604",
                      fill_opacity=0.7, stroke_width=0)
        spot.move_to(bg.get_center() + RIGHT * 0.12 + UP * 0.07)
        return VGroup(bg, mole, spot)

    def _retina_icon(self, color):
        """Fondo de ojo."""
        bg = Circle(radius=0.48, fill_color="#120000",
                    fill_opacity=1, stroke_color=color, stroke_width=1)
        v1 = Line(bg.get_center() + LEFT * 0.35,
                  bg.get_center() + RIGHT * 0.35,
                  stroke_color="#6B0000", stroke_width=1.2)
        v2 = Line(bg.get_center() + UP * 0.3,
                  bg.get_center() + DOWN * 0.25,
                  stroke_color="#6B0000", stroke_width=1)
        disc = Circle(radius=0.09, fill_color="#ff9933",
                      fill_opacity=0.8, stroke_width=0)
        disc.move_to(bg.get_center() + LEFT * 0.18)
        micro = VGroup(*[
            Dot(radius=0.03, color="#ff3333", fill_opacity=0.8).move_to(
                bg.get_center() + RIGHT * x + UP * y)
            for x, y in [(0.18, 0.1), (0.28, -0.06), (0.1, 0.22)]
        ])
        return VGroup(bg, v1, v2, disc, micro)

    def _histo_icon(self, color):
        """Histologia digital."""
        bg = Rectangle(width=0.9, height=0.9,
                       fill_color="#f2ede4", fill_opacity=1,
                       stroke_color=color, stroke_width=1)
        normal = VGroup(*[
            Circle(radius=0.09, fill_color="#4a90d9", fill_opacity=0.6,
                   stroke_color="#2a70b9", stroke_width=0.6).move_to(
                bg.get_center() + RIGHT * (j % 3 - 1) * 0.22 + UP * (1 - j // 3) * 0.22)
            for j in range(6)
        ])
        cancer = VGroup(*[
            Ellipse(width=0.18, height=0.13, fill_color="#e74c3c",
                    fill_opacity=0.8, stroke_color="#c0392b", stroke_width=0.5).move_to(
                bg.get_center() + RIGHT * x + UP * y)
            for x, y in [(0.28, 0.2), (0.32, -0.05), (0.22, -0.25)]
        ])
        return VGroup(bg, normal, cancer)

    # ── construct ─────────────────────────────────────────────────────────────

    def construct(self):

        title = Text("Aplicaciones Reales", font_size=36, color=BLUE_B, weight=BOLD)
        title.to_edge(UP, buff=0.35)
        self.play(Write(title), run_time=0.8)

        # ── 4 paneles en grilla 2x2 ───────────────────────────────────────────
        configs = [
            ("Radiología",    BLUE_C,   "95.2% AUC", "Detección de\nnódulos pulmonares",
             self._chest_icon,  LEFT * 2.7 + UP * 1.1),
            ("Dermatología",  ORANGE,   "91.0% AUC", "Clasificación\nde melanoma",
             self._skin_icon,   RIGHT * 2.7 + UP * 1.1),
            ("Oftalmología",  TEAL_C,   "97.5% AUC", "Retinopatía\ndiabética",
             self._retina_icon, LEFT * 2.7 + DOWN * 1.6),
            ("Patología",     PURPLE_B, "94.8% AUC", "Histología digital\nde tejidos",
             self._histo_icon,  RIGHT * 2.7 + DOWN * 1.6),
        ]

        all_panels = VGroup()

        for name, color, auc, task, icon_fn, pos in configs:
            panel = RoundedRectangle(
                width=4.4, height=2.1,
                fill_color="#0a0d18", fill_opacity=0.75,
                stroke_color=color, stroke_width=1.5,
                corner_radius=0.12,
            )
            panel.move_to(pos)

            icon = icon_fn(color)
            icon.scale(1.15).move_to(pos + LEFT * 1.4)

            bbox = Rectangle(
                width=icon.width * 0.65, height=icon.height * 0.65,
                stroke_color=GREEN, stroke_width=1.5, fill_opacity=0,
            )
            bbox.move_to(icon.get_center() + RIGHT * 0.1 + UP * 0.08)

            name_txt = Text(name, font_size=15, color=color, weight=BOLD)
            name_txt.move_to(pos + RIGHT * 0.72 + UP * 0.62)

            auc_txt = Text(auc, font_size=22, color=color, weight=BOLD)
            auc_txt.move_to(pos + RIGHT * 0.72 + UP * 0.18)

            task_txt = Text(task, font_size=12, color=GRAY_B, line_spacing=1.2)
            task_txt.move_to(pos + RIGHT * 0.72 + DOWN * 0.48)

            all_panels.add(panel, icon, bbox, name_txt, auc_txt, task_txt)

            self.play(FadeIn(panel), FadeIn(icon), run_time=0.3)
            self.play(
                Create(bbox),
                FadeIn(name_txt), FadeIn(auc_txt), FadeIn(task_txt),
                run_time=0.4,
            )

        self.wait(1.5)

        # ── Impacto en la practica clinica ────────────────────────────────────
        self.play(FadeOut(all_panels), run_time=0.5)

        impact_title = Text("Impacto en la Práctica Clínica",
                            font_size=22, color=TEAL_C, weight=BOLD)
        impact_title.move_to(UP * 2.2)
        self.play(FadeIn(impact_title, shift=DOWN * 0.2), run_time=0.5)

        items = [
            ("Reduce la carga del radiólogo hasta 40%",         WHITE),
            ("Detecta patologías en fases más tempranas",        GREEN),
            ("Disponible 24/7 sin fatiga en emergencias",        TEAL_C),
            ("Segunda opinión inmediata para el médico",         YELLOW),
            ("Diagnóstico en zonas sin especialistas",           ORANGE),
        ]

        impact_group = VGroup()
        for text, color in items:
            impact_group.add(Text(text, font_size=16, color=color))
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
