from manim import *
import numpy as np

Text.set_default(font="Noto Sans", line_spacing=1.1)


class S03c_IntroCNN(Scene):
    """Introduction to CNNs.

    Right side: a giant stylized eye, iris moves around (vision metaphor —
    CNNs are inspired by the human visual cortex).
    Left side: the names of the CNN layers we are about to see in detail
    in the next scene (S04_CapasCNN).
    """

    def construct(self):
        title = Text(
            "Convolutional Neural Networks",
            font_size=34,
            color=TEAL_C,
            weight=BOLD,
        )
        title.to_edge(UP, buff=0.35)

        subtitle = Text(
            "Inspired by the human visual cortex",
            font_size=18,
            color=GRAY_B,
        )
        subtitle.next_to(title, DOWN, buff=0.18)

        self.play(Write(title), run_time=0.8)
        self.play(FadeIn(subtitle, shift=DOWN * 0.1), run_time=0.5)

        # ── LEFT: CNN layer titles ────────────────────────────────────────
        layers_header = Text("Layers we  will explore", font_size=18,
                             color=YELLOW, weight=BOLD)
        layer_specs = [
            ("1.", "Input Layer",          BLUE_C),
            ("2.", "Convolution Layer",    BLUE_B),
            ("3.", "Activation (ReLU)",    GREEN_C),
            ("4.", "Pooling Layer",        ORANGE),
            ("5.", "Fully Connected",      PURPLE_B),
            ("6.", "Output (Softmax)",     GREEN),
        ]

        layer_rows = VGroup()
        for num, name, color in layer_specs:
            num_t = Text(num, font_size=20, color=GRAY_B, weight=BOLD)
            name_t = Text(name, font_size=20, color=color)
            row = VGroup(num_t, name_t).arrange(RIGHT, buff=0.18,
                                                aligned_edge=DOWN)
            layer_rows.add(row)
        layer_rows.arrange(DOWN, aligned_edge=LEFT, buff=0.28)

        layers_block = VGroup(layers_header, layer_rows).arrange(
            DOWN, aligned_edge=LEFT, buff=0.32,
        )
        layers_block.move_to(LEFT * 3.8)
        layers_block.shift(DOWN * 0.2)

        # ── RIGHT: giant stylized eye ─────────────────────────────────────
        eye_center = RIGHT * 3.2 + DOWN * 0.2
        eye_h = 1.4   # vertical half-height
        eye_w = 2.6   # horizontal half-width

        # White-ish sclera fill (slightly inset ellipse).
        sclera = Ellipse(width=eye_w * 1.95, height=eye_h * 1.85,
                         color="#F1F4F8", fill_color="#F1F4F8",
                         fill_opacity=0.92, stroke_width=0)
        sclera.move_to(eye_center)

        # Iris + pupil + highlight (will move together).
        iris_radius = 0.55
        iris = Circle(radius=iris_radius,
                      fill_color=BLUE_D, fill_opacity=1.0,
                      stroke_color=BLUE_E, stroke_width=2)
        iris_inner = Circle(radius=iris_radius * 0.78,
                            fill_color=BLUE_C, fill_opacity=1.0,
                            stroke_width=0)
        pupil = Dot(radius=iris_radius * 0.40, color=BLACK)
        highlight = Dot(radius=iris_radius * 0.13, color=WHITE)
        highlight.shift(UP * iris_radius * 0.35 + LEFT * iris_radius * 0.30)

        eyeball = VGroup(iris, iris_inner, pupil, highlight)
        eyeball.move_to(eye_center)

        eye = VGroup(sclera, eyeball)

        # Build everything on screen.
        self.play(
            FadeIn(layers_header, shift=RIGHT * 0.2),
            FadeIn(sclera),
            run_time=1.0,
        )
        self.play(FadeIn(eyeball, scale=0.6), run_time=0.6)
        self.play(
            LaggedStart(
                *[FadeIn(row, shift=RIGHT * 0.15) for row in layer_rows],
                lag_ratio=0.18,
            ),
            run_time=1.6,
        )
        self.wait(0.4)

        # Iris movement: scan around as if the eye is "looking" at the layers.
        # Movement is constrained inside the sclera ellipse (visual safe area).
        gaze_offsets = [
            LEFT * 0.85,
            LEFT * 0.85 + UP * 0.25,
            RIGHT * 0.95 + UP * 0.20,
            RIGHT * 0.95 + DOWN * 0.25,
            LEFT * 0.40 + DOWN * 0.30,
            ORIGIN,
        ]
        for offset in gaze_offsets:
            self.play(
                eyeball.animate.move_to(eye_center + offset),
                run_time=0.55,
                rate_func=smooth,
            )
            self.wait(0.15)

        # Quick blink to feel alive.
        eyelid = Rectangle(
            width=eye_w * 2.2, height=eye_h * 2.2,
            fill_color=config.background_color, fill_opacity=1.0,
            stroke_width=0,
        )
        eyelid.move_to(eye_center)
        eyelid.stretch_to_fit_height(0.0)
        self.add(eyelid)
        self.play(eyelid.animate.stretch_to_fit_height(eye_h * 2.2),
                  run_time=0.18)
        self.play(eyelid.animate.stretch_to_fit_height(0.0),
                  run_time=0.18)
        self.remove(eyelid)

        # Closing tag pointing to the next scene.
        cta = Text("Let's see what each layer does →",
                   font_size=18, color=TEAL_C, weight=BOLD)
        cta.to_edge(DOWN, buff=0.45)
        self.play(FadeIn(cta, shift=UP * 0.15), run_time=0.6)
        self.wait(2.2)
