from manim import *

Text.set_default(font="Noto Sans", line_spacing=1.1)


class S03b_ANN(Scene):
    """Artificial Neural Networks: neuron, loss, and gradient descent."""

    def construct(self):
        title = Text(
            "Artificial Neural Networks",
            font_size=34,
            color=BLUE_B,
            weight=BOLD,
        )
        title.to_edge(UP, buff=0.35)
        self.play(Write(title), run_time=0.7)

        # Formula principal (simple, sin diagrama)
        formula = MathTex(
            r"y = f\left(\sum_i w_i x_i + b\right)",
            font_size=42,
        )
        formula.set_color_by_tex("y", GREEN_C)
        formula.set_color_by_tex("f", TEAL_C)
        formula.set_color_by_tex("w_i", YELLOW)
        formula.set_color_by_tex("x_i", BLUE_C)
        formula.set_color_by_tex("b", ORANGE)

        loss_title = Text("Loss function", font_size=16, color=RED_A)
        loss_eq = MathTex(r"L = (y - y_{real})^2", font_size=30, color=RED_A)
        loss_group = VGroup(loss_title, loss_eq).arrange(DOWN, aligned_edge=LEFT, buff=0.1)

        backprop = Text(
            "Backprop updates weights to reduce L",
            font_size=18,
            color=TEAL_C,
        )

        left_stack = VGroup(formula, loss_group, backprop).arrange(
            DOWN,
            aligned_edge=LEFT,
            buff=0.22,
        )
        left_stack.move_to(LEFT * 3.3 + UP * 0.2)

        self.play(Write(formula), run_time=1.0)
        self.play(FadeIn(loss_group), run_time=0.6)
        self.play(FadeIn(backprop), run_time=0.6)
        self.wait(1.0)

        # Descenso del gradiente (visual limpio)
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[0, 9, 2],
            x_length=3.6,
            y_length=2.6,
            axis_config={"color": GRAY},
        ).move_to(RIGHT * 3.2 + DOWN * 0.3)
        curve = axes.plot(lambda x: x**2, color=BLUE_B)
        gd_title = Text("Gradient descent", font_size=18, color=TEAL_C, weight=BOLD)
        gd_title.next_to(axes, UP, buff=0.12)

        dot = Dot(color=RED_C).move_to(axes.c2p(-2.2, 4.9))
        dot_lbl = MathTex("L", font_size=22, color=RED_C).next_to(dot, LEFT, buff=0.1)

        self.play(Create(axes), Create(curve), FadeIn(gd_title), run_time=1.0)
        self.play(FadeIn(dot), FadeIn(dot_lbl), run_time=0.5)

        self.play(
            MoveAlongPath(dot, axes.plot(lambda x: x**2, x_range=[-2.2, 0])),
            dot_lbl.animate.move_to(axes.c2p(0, 0) + LEFT * 0.45 + UP * 0.3),
            run_time=2.2,
        )
        self.play(dot.animate.set_color(GREEN_C), dot_lbl.animate.set_color(GREEN_C), run_time=0.6)

        self.wait(2.5)