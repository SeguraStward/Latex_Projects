from manim import *

Text.set_default(font="Noto Sans")


class S05b_TransferLearning(Scene):
    """
    Transfer Learning: dominio fuente (ImageNet) → dominio destino (médico).
    """

    # ── construct ─────────────────────────────────────────────────────────────

    def construct(self):

        title = Text("Transfer Learning", font_size=38, color=TEAL_C, weight=BOLD)
        title.to_edge(UP, buff=0.35)
        self.play(Write(title), run_time=0.8)

        # ══════════════════════════════════════════════════════════════════════
        # ACT 1 — Dominio fuente → dominio destino
        # ══════════════════════════════════════════════════════════════════════
        # ── Dominio fuente (ImageNet) ─────────────────────────────────────
        src_box = RoundedRectangle(
            width=4.2, height=2.6,
            fill_color="#070c1a", fill_opacity=0.9,
            stroke_color=BLUE_C, stroke_width=1.8,
            corner_radius=0.12,
        )
        src_box.move_to(LEFT * 3.5 + DOWN * 0.2)

        src_title = Text("Dominio Fuente", font_size=14, color=BLUE_C, weight=BOLD)
        src_title.next_to(src_box, UP, buff=0.12)

        src_tag = Text("ImageNet  —  1.2 M imágenes", font_size=11, color=GRAY_B)
        src_tag.move_to(src_box.get_top() + DOWN * 0.28)

        # Pequeña cuadrícula de fotos naturales
        nat_labels = ["Perro", "Gato", "Auto", "Avión", "Árbol", "Flor"]
        nat_colors = [BLUE_C, TEAL_C, GREEN_C, YELLOW, ORANGE, PURPLE_B]
        nat_cards = VGroup(*[
            VGroup(
                Rectangle(width=0.55, height=0.45,
                          fill_color=col, fill_opacity=0.22,
                          stroke_color=col, stroke_width=0.9),
                Text(lbl, font_size=7, color=col),
            ).arrange(DOWN, buff=0.04)
            for lbl, col in zip(nat_labels, nat_colors)
        ])
        nat_cards.arrange_in_grid(rows=2, cols=3, buff=0.12)
        nat_cards.move_to(src_box.get_center() + DOWN * 0.15)

        self.play(FadeIn(src_box), FadeIn(src_title), FadeIn(src_tag), run_time=0.5)
        self.play(
            LaggedStart(*[FadeIn(c, shift=UP * 0.1) for c in nat_cards],
                        lag_ratio=0.07),
            run_time=0.9,
        )

        # ── Flecha de transferencia ───────────────────────────────────────
        transfer_arrow = Arrow(
            src_box.get_right() + RIGHT * 0.1,
            src_box.get_right() + RIGHT * 2.0,
            buff=0.0, color=TEAL_C, stroke_width=3, tip_length=0.22,
        )
        tl_badge = Text("Transfer\nLearning", font_size=13, color=TEAL_C, weight=BOLD)
        tl_badge.next_to(transfer_arrow, UP, buff=0.1)
        self.play(GrowArrow(transfer_arrow), FadeIn(tl_badge), run_time=0.6)

        # ── Dominio destino (Médico) ──────────────────────────────────────
        dst_box = RoundedRectangle(
            width=4.2, height=2.6,
            fill_color="#070c0e", fill_opacity=0.9,
            stroke_color=TEAL_C, stroke_width=1.8,
            corner_radius=0.12,
        )
        dst_box.move_to(RIGHT * 3.5 + DOWN * 0.2)

        dst_title = Text("Dominio Destino", font_size=14, color=TEAL_C, weight=BOLD)
        dst_title.next_to(dst_box, UP, buff=0.12)

        dst_tag = Text("Imágenes Médicas  —  ~500 muestras", font_size=11, color=GRAY_B)
        dst_tag.move_to(dst_box.get_top() + DOWN * 0.28)

        med_labels = ["RX Tórax", "MRI", "Derma", "Retina", "Histo", "TC"]
        med_colors = [BLUE_C, TEAL_C, ORANGE, RED_C, GREEN_C, PURPLE_B]
        med_cards = VGroup(*[
            VGroup(
                Rectangle(width=0.55, height=0.45,
                          fill_color="#0a0a12", fill_opacity=1,
                          stroke_color=col, stroke_width=0.9),
                Text(lbl, font_size=7, color=col),
            ).arrange(DOWN, buff=0.04)
            for lbl, col in zip(med_labels, med_colors)
        ])
        med_cards.arrange_in_grid(rows=2, cols=3, buff=0.12)
        med_cards.move_to(dst_box.get_center() + DOWN * 0.15)

        self.play(FadeIn(dst_box), FadeIn(dst_title), FadeIn(dst_tag), run_time=0.5)
        self.play(
            LaggedStart(*[FadeIn(c, shift=UP * 0.1) for c in med_cards],
                        lag_ratio=0.07),
            run_time=0.9,
        )

        caption1 = Text(
            "Una red entrenada en millones de imágenes genéricas\n"
            "se adapta a tareas médicas con muy pocos datos",
            font_size=14, color=GRAY_A,
        )
        caption1.to_edge(DOWN, buff=0.28)
        self.play(FadeIn(caption1, shift=UP * 0.15), run_time=0.6)
        self.wait(3.0)
