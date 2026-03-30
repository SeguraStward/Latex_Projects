from manim import *

Text.set_default(font="Noto Sans")


class S02_Introduccion(Scene):
    """
    MRI cerebral simulado, CNN detecta tumor con bounding box verde,
    y puntos clave de la introduccion.
    """

    def _make_brain_scan(self):
        bg = Circle(radius=1.9, fill_color="#111111", fill_opacity=1,
                    stroke_color="#333333", stroke_width=1.5)
        brain = Ellipse(width=3.2, height=2.6, fill_color="#2a2525",
                        fill_opacity=1, stroke_color="#3a3030", stroke_width=1)
        sulci = VGroup(
            Arc(radius=0.7, start_angle=PI * 0.3, angle=PI * 0.7,
                stroke_color="#3d3030", stroke_width=1.2),
            Arc(radius=1.1, start_angle=PI * 0.1, angle=PI * 0.5,
                stroke_color="#3d3030", stroke_width=1),
            Arc(radius=0.9, start_angle=-PI * 0.4, angle=-PI * 0.6,
                stroke_color="#3d3030", stroke_width=1),
            Arc(radius=1.3, start_angle=PI * 0.6, angle=PI * 0.4,
                stroke_color="#3d3030", stroke_width=0.8),
        )
        gray_matter = Ellipse(width=2.6, height=2.1, fill_color="#332d2d",
                              fill_opacity=0.6, stroke_width=0)
        v1 = Ellipse(width=0.4, height=0.6, fill_color="#1a1515",
                     fill_opacity=0.9, stroke_width=0).shift(LEFT * 0.25 + UP * 0.1)
        v2 = Ellipse(width=0.4, height=0.6, fill_color="#1a1515",
                     fill_opacity=0.9, stroke_width=0).shift(RIGHT * 0.25 + UP * 0.1)
        tumor = Circle(radius=0.22, fill_color="#c0392b", fill_opacity=0.92,
                       stroke_color="#e74c3c", stroke_width=1.5)
        tumor.shift(RIGHT * 0.75 + UP * 0.55)
        edema = Circle(radius=0.38, fill_color="#7b241c",
                       fill_opacity=0.35, stroke_width=0)
        edema.move_to(tumor.get_center())
        scan = VGroup(bg, brain, gray_matter, sulci, v1, v2, edema, tumor)
        return scan, tumor

    def _make_network(self):
        layer_sizes = [4, 6, 6, 3]
        layer_colors = [BLUE_C, TEAL_C, TEAL_C, GREEN_C]
        x_positions = [-0.9, -0.3, 0.3, 0.9]
        layers = []
        for n, color, x in zip(layer_sizes, layer_colors, x_positions):
            layer = VGroup()
            for j in range(n):
                y = (n - 1) / 2 * 0.32 - j * 0.32
                dot = Circle(radius=0.1, fill_color=color, fill_opacity=0.5,
                             stroke_color=color, stroke_width=1.2)
                dot.move_to(RIGHT * x + UP * y)
                layer.add(dot)
            layers.append(layer)
        edges = VGroup()
        for i in range(len(layers) - 1):
            for na in layers[i]:
                for nb in layers[i + 1]:
                    edges.add(Line(na.get_center(), nb.get_center(),
                                   stroke_width=0.4, stroke_color=GRAY_D,
                                   stroke_opacity=0.25))
        network = VGroup(edges, *layers)
        return network, layers

    def construct(self):
        title = Text("Introducción", font_size=40, color=BLUE_B, weight=BOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title), run_time=0.9)

        # Scan MRI
        scan_group, tumor = self._make_brain_scan()
        scan_group.scale(0.95).move_to(LEFT * 4.2 + DOWN * 0.3)
        tumor_center = tumor.get_center()
        scan_label = Text("Resonancia Magnética (MRI)", font_size=15, color=GRAY_C)
        scan_label.next_to(scan_group, DOWN, buff=0.18)
        self.play(FadeIn(scan_group), FadeIn(scan_label), run_time=1.2)

        # Red neuronal
        network, layers = self._make_network()
        network.move_to(ORIGIN + DOWN * 0.3)
        cnn_label = Text("CNN", font_size=18, color=TEAL_C, weight=BOLD)
        cnn_label.next_to(network, UP, buff=0.2)
        self.play(Create(network), Write(cnn_label), run_time=1.2)

        arr_in = Arrow(scan_group.get_right(), network.get_left(),
                       buff=0.12, color=GRAY_C, stroke_width=1.8, tip_length=0.18)
        self.play(GrowArrow(arr_in), run_time=0.5)

        # Linea de escaneo
        scan_top = scan_group.get_top() + DOWN * 0.15
        scan_line = Line(scan_group.get_left() + RIGHT * 0.05,
                         scan_group.get_right() + LEFT * 0.05,
                         stroke_color=TEAL_C, stroke_width=1.5, stroke_opacity=0.7)
        scan_line.move_to(scan_top)
        self.play(scan_line.animate.move_to(scan_group.get_bottom() + UP * 0.15),
                  run_time=1.4, rate_func=linear)

        # Bounding boxes falsos
        for pos in [LEFT * 4.2 + UP * 0.2, LEFT * 3.8 + DOWN * 0.5, LEFT * 4.5 + UP * 0.6]:
            fb = Rectangle(width=0.55, height=0.55,
                           stroke_color=YELLOW, stroke_width=1.5, fill_opacity=0)
            fb.move_to(pos)
            self.play(FadeIn(fb), run_time=0.18)
            self.play(FadeOut(fb), run_time=0.18)

        # Forward pass
        for layer in layers:
            self.play(*[n.animate.set_fill(YELLOW, opacity=0.95) for n in layer],
                      run_time=0.25)
            self.play(*[n.animate.set_fill(n.get_fill_color(), opacity=0.5) for n in layer],
                      run_time=0.2)

        # Bounding box verde
        bbox = Rectangle(width=0.72, height=0.72,
                         stroke_color=GREEN, stroke_width=2.8, fill_opacity=0)
        bbox.move_to(tumor_center)
        conf_label = Text("Tumor  94.7%", font_size=13, color=GREEN, weight=BOLD)
        conf_label.next_to(bbox, UP, buff=0.06)
        self.play(Create(bbox), run_time=0.5)
        self.play(bbox.animate.set_stroke(YELLOW, width=3), run_time=0.2)
        self.play(bbox.animate.set_stroke(GREEN, width=2.8),
                  FadeIn(conf_label), run_time=0.4)

        arr_out = Arrow(network.get_right(), RIGHT * 1.5 + DOWN * 0.3,
                        buff=0.1, color=GREEN, stroke_width=1.8, tip_length=0.18)
        result_text = Text("Diagnóstico", font_size=16, color=GREEN)
        result_text.next_to(arr_out, RIGHT, buff=0.1)
        self.play(GrowArrow(arr_out), FadeIn(result_text), run_time=0.5)

        # Puntos clave
        self.play(FadeOut(arr_out), FadeOut(result_text),
                  FadeOut(network), FadeOut(cnn_label), FadeOut(arr_in),
                  FadeOut(scan_line), run_time=0.6)

        points = VGroup(
            Text("Deep Learning revoluciona el diagnóstico", font_size=17, color=WHITE),
            Text("Radiología | Dermatología | Oftalmología", font_size=15, color=GRAY_B),
            Text("AlexNet (2012): punto de inflexión en ImageNet", font_size=17, color=YELLOW),
            Text("CNN supera a especialistas en ciertas tareas", font_size=17, color=WHITE),
            Text("FDA autoriza modelos como copilotos clínicos", font_size=17, color=TEAL_C),
            Text("Elimina handcrafted features", font_size=17, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.28)
        points.move_to(RIGHT * 2.5 + DOWN * 0.2)

        for p in points:
            bullet = Dot(radius=0.07, color=TEAL_C)
            bullet.next_to(p, LEFT, buff=0.15)
            self.play(FadeIn(bullet, shift=RIGHT * 0.2),
                      FadeIn(p, shift=RIGHT * 0.2), run_time=0.45)

        self.wait(2.5)
