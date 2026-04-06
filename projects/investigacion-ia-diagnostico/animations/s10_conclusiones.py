from manim import *

Text.set_default(font="Noto Sans")


class S10_Conclusiones(Scene):
    """
    Conclusiones finales + perspectivas futuras + galería de imágenes.
    """

    def construct(self):

        # ── Título ───────────────────────────────────────────────────────────
        title = Text("Conclusiones", font_size=40, color=GREEN, weight=BOLD)
        title.to_edge(UP, buff=0.35)
        self.play(Write(title), run_time=0.8)

        # ── Síntesis de hallazgos ────────────────────────────────────────────
        conclusions = [
            ("AUC 93.2% en gliomas · 89.6% en cáncer de mama",         GREEN),
            ("Sensibilidad > 90% en hemorragia intracraneal (Aidoc)",   BLUE_B),
            ("U-Net: estándar para segmentación médica",                TEAL_C),
            ("873 algoritmos FDA autorizados en radiología (2025)",      YELLOW),
            ("Adopción plena: solo 2% en EE.UU.",                       ORANGE),
        ]

        conc_items = VGroup()
        for text, color in conclusions:
            conc_items.add(Text(text, font_size=15, color=color))
        conc_items.arrange(DOWN, aligned_edge=LEFT, buff=0.34)
        conc_items.move_to(DOWN * 0.15)

        conc_bullets = VGroup()
        for item in conc_items:
            bullet = Square(side_length=0.12, fill_color=GREEN,
                            fill_opacity=1, stroke_width=0)
            bullet.next_to(item, LEFT, buff=0.18)
            conc_bullets.add(bullet)
            self.play(
                FadeIn(bullet, shift=RIGHT * 0.2),
                FadeIn(item,   shift=RIGHT * 0.2),
                run_time=0.45,
            )

        self.wait(1.5)

        # ── Perspectivas futuras ─────────────────────────────────────────────
        self.play(FadeOut(conc_items), FadeOut(conc_bullets), run_time=0.5)

        future_title = Text("Perspectivas Futuras", font_size=26,
                            color=PURPLE_B, weight=BOLD)
        future_title.move_to(UP * 2.0)
        self.play(FadeIn(future_title, shift=DOWN * 0.15), run_time=0.5)

        future_items_data = [
            ("IA Explicable (XAI) para eliminar la caja negra",         YELLOW),
            ("Modelos multimodales: imagen + historial + laboratorio",   TEAL_C),
            ("IA Adaptativa con marcos regulatorios flexibles",          BLUE_C),
            ("Aprendizaje Federado entre hospitales sin compartir datos", GREEN),
        ]

        future_items = VGroup()
        for text, color in future_items_data:
            future_items.add(Text(text, font_size=15, color=color))
        future_items.arrange(DOWN, aligned_edge=LEFT, buff=0.30)
        future_items.move_to(DOWN * 0.4)

        future_arrows = VGroup()
        for item in future_items:
            arr = Text("→", font_size=15, color=PURPLE_B)
            arr.next_to(item, LEFT, buff=0.15)
            future_arrows.add(arr)
            self.play(
                FadeIn(arr,  shift=RIGHT * 0.15),
                FadeIn(item, shift=RIGHT * 0.15),
                run_time=0.4,
            )

        self.wait(1.8)

        # ── Galería de imágenes reales ───────────────────────────────────────
        self.play(
            FadeOut(title), FadeOut(future_title),
            FadeOut(future_items), FadeOut(future_arrows),
            run_time=0.6,
        )

        gallery_title = Text("Imágenes Reales del Dominio", font_size=28,
                             color=TEAL_C, weight=BOLD)
        gallery_title.to_edge(UP, buff=0.40)
        self.play(FadeIn(gallery_title, shift=DOWN * 0.12), run_time=0.5)

        images_data = [
            ("../imgs/mri.jpg",              "Resonancia Magnética"),
            ("../imgs/segmentation.jpg",     "Segmentación de Tumor"),
            ("../imgs/radiologia.jpg",       "Radiología Digital"),
            ("../imgs/layers.jpg",           "Capas de una CNN"),
            ("../imgs/unet.jpg",             "Arquitectura U-Net"),
            ("../imgs/neuron.jpg",           "Neurona Artificial"),
            ("../imgs/odontology.jpg",       "Diagnóstico Dental"),
            ("../imgs/abdomentomografy.jpg", "Tomografía Abdominal"),
            ("../imgs/example.jpg",          "Ejemplo de Clasificación"),
            ("../imgs/portada.png",          "IA en Diagnóstico Médico"),
        ]

        prev_group = None

        for path, caption_text in images_data:
            img = ImageMobject(path)
            img.set_height(4.8)
            if img.width > 8.5:
                img.set_width(8.5)
            img.move_to(DOWN * 0.15)

            frame = SurroundingRectangle(
                img, color=TEAL_C, stroke_width=1.5,
                fill_opacity=0, buff=0.06,
            )

            caption = Text(caption_text, font_size=16, color="#D0D0D0")
            caption.next_to(img, DOWN, buff=0.28)

            group = Group(img, frame, caption)

            if prev_group is None:
                self.play(FadeIn(group, shift=UP * 0.2), run_time=0.6)
            else:
                self.play(
                    FadeOut(prev_group, shift=LEFT * 0.6),
                    FadeIn(group, shift=RIGHT * 0.6),
                    run_time=0.55,
                )

            self.wait(0.9)
            prev_group = group

        self.wait(1.0)
        self.play(FadeOut(prev_group), FadeOut(gallery_title), run_time=0.8)
        self.wait(1.0)
