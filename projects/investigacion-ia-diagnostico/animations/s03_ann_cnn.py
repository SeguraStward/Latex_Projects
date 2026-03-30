from manim import *
import numpy as np

Text.set_default(font="Noto Sans")
from helpers import make_eye


class S03_ANN_CNN(Scene):
    """ANN vs CNN: neurona basica, red completa y el ojo (corteza visual)."""

    def _make_ann_network(self):
        layer_cfg = [(4, BLUE_C), (4, BLUE_D), (2, GREEN_C)]
        x_pos = [-1.0, 0.0, 1.0]
        layers = []
        for (n, color), x in zip(layer_cfg, x_pos):
            layer = VGroup()
            for j in range(n):
                y = (n - 1) / 2 * 0.55 - j * 0.55
                c = Circle(radius=0.18, fill_color=color, fill_opacity=0.45,
                           stroke_color=color, stroke_width=1.5)
                c.move_to(RIGHT * x + UP * y)
                layer.add(c)
            layers.append(layer)
        edges = VGroup()
        for i in range(len(layers) - 1):
            for a in layers[i]:
                for b in layers[i + 1]:
                    edges.add(Line(a.get_center(), b.get_center(),
                                   stroke_width=0.5, stroke_color=GRAY_C,
                                   stroke_opacity=0.2))
        return VGroup(edges, *layers), layers

    def construct(self):
        title = Text("Redes Neuronales: ANN vs CNN",
                     font_size=38, color=BLUE_B, weight=BOLD)
        title.to_edge(UP, buff=0.35)
        self.play(Write(title), run_time=0.8)

        # ── BLOQUE IZQUIERDO — ANN ────────────────────────────────────────
        ann_title = Text("Red Neuronal Artificial (ANN)",
                         font_size=20, color=BLUE_C, weight=BOLD)
        ann_title.move_to(LEFT * 3.5 + UP * 2.7)
        self.play(FadeIn(ann_title, shift=DOWN * 0.2))

        neuron = Circle(radius=0.35, fill_color=BLUE_D, fill_opacity=0.4,
                        stroke_color=BLUE_C, stroke_width=2)
        neuron.move_to(LEFT * 3.5 + UP * 1.1)
        sigma = Text("Σ", font_size=22, color=WHITE)
        sigma.move_to(neuron.get_center())

        inputs_pos = [LEFT * 5.2 + UP * 1.7, LEFT * 5.2 + UP * 1.1,
                      LEFT * 5.2 + UP * 0.5]
        input_dots = VGroup(*[Dot(p, radius=0.12, color=BLUE_C) for p in inputs_pos])
        input_texts = VGroup(*[
            Text(l, font_size=16, color=GRAY_A).move_to(p + LEFT * 0.25)
            for l, p in zip(["x1", "x2", "x3"], inputs_pos)
        ])
        arrows_in = VGroup(*[Arrow(p, neuron.get_left(), buff=0.12,
                                   color=BLUE_C, stroke_width=1.5, tip_length=0.14)
                              for p in inputs_pos])
        weight_texts = VGroup(*[
            Text(w, font_size=14, color=YELLOW).move_to(
                (inputs_pos[i] + neuron.get_left()) / 2 + UP * 0.15)
            for i, w in enumerate(["w1", "w2", "w3"])
        ])
        out_arrow = Arrow(neuron.get_right(), neuron.get_right() + RIGHT * 0.8,
                          color=GREEN_C, stroke_width=2, tip_length=0.14)
        out_lbl = Text("y", font_size=18, color=GREEN_C)
        out_lbl.next_to(out_arrow, RIGHT, buff=0.1)

        self.play(Create(neuron), Write(sigma),
                  FadeIn(input_dots), FadeIn(input_texts), run_time=0.7)
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows_in], lag_ratio=0.15),
                  FadeIn(weight_texts), run_time=0.7)
        self.play(GrowArrow(out_arrow), FadeIn(out_lbl), run_time=0.5)

        ann_net, ann_layers = self._make_ann_network()
        ann_net.scale(0.85).move_to(LEFT * 3.5 + DOWN * 0.9)
        ann_lbl = VGroup(
            Text("Entrada", font_size=12, color=BLUE_C),
            Text("Oculta", font_size=12, color=BLUE_D),
            Text("Salida", font_size=12, color=GREEN_C),
        )
        for lbl, layer in zip(ann_lbl, ann_layers):
            lbl.next_to(layer, DOWN, buff=0.1)
        self.play(Create(ann_net), FadeIn(ann_lbl), run_time=1.0)

        flat_group = VGroup(
            Text("Imagen 2D a vector 1D", font_size=14, color=RED),
            Text("Pierde estructura espacial", font_size=12, color=RED),
        ).arrange(DOWN, buff=0.08)
        flat_group.move_to(LEFT * 3.5 + DOWN * 2.6)
        flat_box = SurroundingRectangle(flat_group, color=RED,
                                        buff=0.12, corner_radius=0.08)
        self.play(FadeIn(flat_group), Create(flat_box), run_time=0.7)

        # ── DIVISOR CENTRAL ───────────────────────────────────────────────
        divider = DashedLine(UP * 3, DOWN * 3.5, color=GRAY_D,
                             stroke_width=1.2, dash_length=0.15)
        center_arrow = Arrow(LEFT * 0.6, RIGHT * 0.6, color=TEAL_C,
                             stroke_width=2, tip_length=0.16)
        center_arrow.move_to(ORIGIN + UP * 0.15)
        center_lbl = Text("Inspirada en\nla corteza visual",
                          font_size=14, color=TEAL_C)
        center_lbl.next_to(center_arrow, DOWN, buff=0.1)
        self.play(Create(divider), run_time=0.5)
        self.play(GrowArrow(center_arrow), FadeIn(center_lbl), run_time=0.6)

        # ── BLOQUE DERECHO — CNN con el OJO ──────────────────────────────
        cnn_title = Text("Red Neuronal Convolucional (CNN)",
                         font_size=20, color=TEAL_C, weight=BOLD)
        cnn_title.move_to(RIGHT * 3.2 + UP * 2.7)
        self.play(FadeIn(cnn_title, shift=DOWN * 0.2))

        eye = make_eye()
        eye.scale(1.1).move_to(RIGHT * 3.2 + DOWN * 0.2)
        sclera_w = eye[0].width
        eyeball = VGroup(eye[1], eye[2], eye[3])  # iris + pupila + brillo

        cortex_lbl = Text("Corteza Visual Humana", font_size=14, color=GRAY_B)
        cortex_lbl.next_to(eye, DOWN, buff=0.2)

        self.play(FadeIn(eye), FadeIn(cortex_lbl), run_time=0.6)
        self.wait(0.5)

        # Cornea se mueve de lado a lado
        move = sclera_w * 0.18
        self.play(eyeball.animate.shift(RIGHT * move), run_time=0.55)
        self.wait(0.2)
        self.play(eyeball.animate.shift(LEFT * move * 2), run_time=0.8)
        self.wait(0.2)
        self.play(eyeball.animate.shift(RIGHT * move), run_time=0.55)

        self.wait(2.5)
