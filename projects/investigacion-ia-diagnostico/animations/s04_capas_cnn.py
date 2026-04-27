from manim import *
from helpers import make_neuron_col, make_sparse_edges, make_pixel_grid, make_mini_pattern

Text.set_default(font="Noto Sans", line_spacing=1.1)


class S04_CapasCNN(MovingCameraScene):
    """
    The digit '8' travels through 4 CNN layers.
    Act 1 — Input Layer    : pixel grid to neurons
    Act 2 — First Hidden   : edge detectors (zoom)
    Act 3 — Second Hidden  : shape / loop detectors (zoom)
    Act 4 — Output Layer   : softmax and probabilities
    """

    DIGIT_8 = [
        [0, 1, 1, 1, 1, 0],
        [1, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 1],
        [0, 1, 1, 1, 1, 0],
        [1, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 1],
        [0, 1, 1, 1, 1, 0],
    ]

    def construct(self):
        self.camera.frame.save_state()

        # ═══════════════════════════════════════════════════════════════════
        # ACT 1 — The Pixel Canvas (Input Layer)
        # ═══════════════════════════════════════════════════════════════════
        act_lbl = Text("Input Layer",
                       font_size=26, color=TEAL_C, weight=BOLD)
        act_lbl.to_edge(UP, buff=0.35)
        self.play(Write(act_lbl))

        # The "8" as a vector path
        top_loop = Ellipse(width=1.7, height=1.4, fill_opacity=0,
                           stroke_color=WHITE, stroke_width=6)
        bot_loop = Ellipse(width=1.7, height=1.4, fill_opacity=0,
                           stroke_color=WHITE, stroke_width=6)
        bot_loop.next_to(top_loop, DOWN, buff=-0.18)
        eight = VGroup(top_loop, bot_loop).move_to(ORIGIN)
        self.play(Create(eight), run_time=1.0)
        self.wait(0.4)

        # The grid descends over the "8"
        grid = make_pixel_grid(self.DIGIT_8, cell=0.42)
        grid.move_to(UP * 5)
        self.play(FadeOut(eight), grid.animate.move_to(ORIGIN), run_time=1.2)

        px_lbl = Text("7x6 pixels -- value between 0 and 1 per pixel",
                      font_size=15, color=GRAY_B)
        px_lbl.next_to(grid, DOWN, buff=0.22)
        self.play(FadeIn(px_lbl))
        self.wait(0.6)

        # Compress to the left side
        self.play(FadeOut(px_lbl),
                  grid.animate.scale(0.7).move_to(LEFT * 5.0), run_time=0.9)

        # Input column
        in_col = make_neuron_col(-2.8, BLUE_C)
        in_dots = Text("...", font_size=20, color=GRAY_C)
        in_dots.next_to(in_col, DOWN, buff=0.08)
        in_title = Text("Input\n784", font_size=13, color=BLUE_C)
        in_title.next_to(in_col, UP, buff=0.15)

        unroll_arr = Arrow(grid.get_right(), in_col.get_left(), buff=0.12,
                           color=GRAY_C, stroke_width=1.5, tip_length=0.15)

        self.play(GrowArrow(unroll_arr))
        self.play(LaggedStart(*[FadeIn(n, scale=0.5) for n in in_col],
                               lag_ratio=0.04), run_time=0.8)
        self.play(FadeIn(in_dots), FadeIn(in_title))
        self.wait(0.5)

        # ═══════════════════════════════════════════════════════════════════
        # ACT 2 — Edge Detectors (First Hidden Layer)
        # ═══════════════════════════════════════════════════════════════════
        act2 = Text("Edge Detectors",
                    font_size=24, color=YELLOW, weight=BOLD)
        act2.to_edge(UP, buff=0.35)
        self.play(ReplacementTransform(act_lbl, act2))

        h1_col = make_neuron_col(-0.6, TEAL_C)
        h1_dots = Text("...", font_size=20, color=GRAY_C)
        h1_dots.next_to(h1_col, DOWN, buff=0.08)
        h1_title = Text("Hidden 1\n128", font_size=13, color=TEAL_C)
        h1_title.next_to(h1_col, UP, buff=0.15)

        edges1 = make_sparse_edges(in_col, h1_col)
        self.play(Create(edges1), run_time=0.7)
        self.play(LaggedStart(*[FadeIn(n, scale=0.5) for n in h1_col],
                               lag_ratio=0.04), run_time=0.8)
        self.play(FadeIn(h1_dots), FadeIn(h1_title))
        self.wait(0.3)

        # Zoom to neuron — horizontal edge
        n_horiz = h1_col[2]
        self.play(
            self.camera.frame.animate.scale(0.38).move_to(n_horiz.get_center()),
            n_horiz.animate.set_fill(YELLOW, opacity=0.95),
            run_time=1.0,
        )
        horiz_grid = make_mini_pattern(
            [[1, 1, 1, 1, 1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], cell=0.09)
        horiz_grid.next_to(n_horiz, RIGHT, buff=0.12)
        horiz_lbl = Text("horizontal edge", font_size=5, color=YELLOW)
        horiz_lbl.next_to(horiz_grid, DOWN, buff=0.08)
        self.play(FadeIn(horiz_grid), FadeIn(horiz_lbl), run_time=0.6)
        self.wait(0.5)

        # Zoom to neuron — vertical edge
        n_vert = h1_col[5]
        self.play(
            self.camera.frame.animate.move_to(n_vert.get_center()),
            n_horiz.animate.set_fill(TEAL_C, opacity=0.5),
            n_vert.animate.set_fill(YELLOW, opacity=0.95),
            run_time=0.8,
        )
        vert_grid = make_mini_pattern(
            [[1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0]], cell=0.09)
        vert_grid.next_to(n_vert, RIGHT, buff=0.12)
        vert_lbl = Text("vertical edge", font_size=5, color=YELLOW)
        vert_lbl.next_to(vert_grid, DOWN, buff=0.08)
        self.play(FadeIn(vert_grid), FadeIn(vert_lbl), run_time=0.6)
        self.wait(0.5)

        # Zoom to neuron — curve
        n_curve = h1_col[7]
        self.play(
            self.camera.frame.animate.move_to(n_curve.get_center()),
            n_vert.animate.set_fill(TEAL_C, opacity=0.5),
            n_curve.animate.set_fill(YELLOW, opacity=0.95),
            run_time=0.8,
        )
        curve_grid = make_mini_pattern(
            [[0, 0, 1, 0, 0], [0, 1, 0, 0, 0], [1, 0, 0, 0, 0]], cell=0.09)
        curve_grid.next_to(n_curve, RIGHT, buff=0.12)
        curve_lbl = Text("curve / diagonal", font_size=5, color=YELLOW)
        curve_lbl.next_to(curve_grid, DOWN, buff=0.08)
        self.play(FadeIn(curve_grid), FadeIn(curve_lbl), run_time=0.6)
        self.wait(0.5)

        self.play(
            Restore(self.camera.frame),
            n_curve.animate.set_fill(TEAL_C, opacity=0.5),
            FadeOut(horiz_grid), FadeOut(horiz_lbl),
            FadeOut(vert_grid), FadeOut(vert_lbl),
            FadeOut(curve_grid), FadeOut(curve_lbl),
            run_time=1.0,
        )
        cap2 = Text("Layer 1: detects only edges and corners, not the full digit",
                    font_size=15, color=GRAY_B)
        cap2.to_edge(DOWN, buff=0.3)
        self.play(FadeIn(cap2))
        self.wait(1.0)
        self.play(FadeOut(cap2))

        # ═══════════════════════════════════════════════════════════════════
        # ACT 3 — Shape Detectors (Second Hidden Layer)
        # ═══════════════════════════════════════════════════════════════════
        act3 = Text("Shape Detectors",
                    font_size=24, color=ORANGE, weight=BOLD)
        act3.to_edge(UP, buff=0.35)
        self.play(ReplacementTransform(act2, act3))

        h2_col = make_neuron_col(1.2, PURPLE_B)
        h2_dots = Text("...", font_size=20, color=GRAY_C)
        h2_dots.next_to(h2_col, DOWN, buff=0.08)
        h2_title = Text("Hidden 2\n64", font_size=13, color=PURPLE_B)
        h2_title.next_to(h2_col, UP, buff=0.15)

        edges2 = make_sparse_edges(h1_col, h2_col)
        self.play(Create(edges2), run_time=0.7)
        self.play(LaggedStart(*[FadeIn(n, scale=0.5) for n in h2_col],
                               lag_ratio=0.04), run_time=0.8)
        self.play(FadeIn(h2_dots), FadeIn(h2_title))
        self.wait(0.3)

        # ── What each neuron detects — clear diagram without zoom ───────────
        n_loop1 = h2_col[2]
        n_loop2 = h2_col[5]

        # The "8" as two large visible ellipses to the right of the network
        demo_cx = 4.3
        loop_top = Ellipse(width=1.2, height=1.05, fill_opacity=0,
                           stroke_color=GRAY_B, stroke_width=2.5)
        loop_bot = Ellipse(width=1.2, height=1.05, fill_opacity=0,
                           stroke_color=GRAY_B, stroke_width=2.5)
        loop_top.move_to(RIGHT * demo_cx + UP * 0.50)
        loop_bot.move_to(RIGHT * demo_cx + DOWN * 0.50)
        eight_lbl = Text('Digit "8"', font_size=14, color=GRAY_B)
        eight_lbl.next_to(VGroup(loop_top, loop_bot), UP, buff=0.14)

        self.play(Create(loop_top), Create(loop_bot),
                  FadeIn(eight_lbl), run_time=0.7)

        # ── Upper loop → n_loop1 ──────────────────────────────────────────
        ring_top = Ellipse(width=1.45, height=1.25,
                           fill_color=ORANGE, fill_opacity=0.18,
                           stroke_color=ORANGE, stroke_width=2.8)
        ring_top.move_to(loop_top.get_center())

        top_tag = Text("Upper\nloop", font_size=13, color=ORANGE, weight=BOLD)
        top_tag.next_to(ring_top, RIGHT, buff=0.14)

        arr_top = Arrow(
            n_loop1.get_right(), ring_top.get_left(),
            buff=0.12, color=ORANGE, stroke_width=2.2, tip_length=0.18,
        )
        arr_top_lbl = Text("detects", font_size=11, color=ORANGE)
        arr_top_lbl.next_to(arr_top, UP, buff=0.06)

        self.play(
            n_loop1.animate.set_fill(ORANGE, opacity=0.95),
            Create(ring_top), FadeIn(top_tag),
            run_time=0.7,
        )
        self.play(GrowArrow(arr_top), FadeIn(arr_top_lbl), run_time=0.5)
        self.wait(0.6)

        # ── Lower loop → n_loop2 ──────────────────────────────────────────
        ring_bot = Ellipse(width=1.45, height=1.25,
                           fill_color=YELLOW, fill_opacity=0.18,
                           stroke_color=YELLOW, stroke_width=2.8)
        ring_bot.move_to(loop_bot.get_center())

        bot_tag = Text("Lower\nloop", font_size=13, color=YELLOW, weight=BOLD)
        bot_tag.next_to(ring_bot, RIGHT, buff=0.14)

        arr_bot = Arrow(
            n_loop2.get_right(), ring_bot.get_left(),
            buff=0.12, color=YELLOW, stroke_width=2.2, tip_length=0.18,
        )
        arr_bot_lbl = Text("detects", font_size=11, color=YELLOW)
        arr_bot_lbl.next_to(arr_bot, DOWN, buff=0.06)

        self.play(
            n_loop2.animate.set_fill(YELLOW, opacity=0.95),
            Create(ring_bot), FadeIn(bot_tag),
            run_time=0.7,
        )
        self.play(GrowArrow(arr_bot), FadeIn(arr_bot_lbl), run_time=0.5)
        self.wait(0.6)

        self.play(
            Flash(n_loop1, color=ORANGE, flash_radius=0.30, line_length=0.10),
            Flash(n_loop2, color=YELLOW, flash_radius=0.30, line_length=0.10),
            run_time=0.6,
        )

        self.play(
            FadeOut(loop_top), FadeOut(loop_bot), FadeOut(eight_lbl),
            FadeOut(ring_top), FadeOut(top_tag),
            FadeOut(arr_top), FadeOut(arr_top_lbl),
            FadeOut(ring_bot), FadeOut(bot_tag),
            FadeOut(arr_bot), FadeOut(arr_bot_lbl),
            run_time=0.5,
        )

        cap3 = Text("Layer 2: combines edges to recognize loops -- the '8' has TWO.",
                    font_size=15, color=GRAY_B)
        cap3.to_edge(DOWN, buff=0.3)
        self.play(FadeIn(cap3))
        self.wait(1.2)
        self.play(FadeOut(cap3))

        # ═══════════════════════════════════════════════════════════════════
        # ACT 4 — The Verdict (Output Layer)
        # ═══════════════════════════════════════════════════════════════════
        act4 = Text("Output Layer",
                    font_size=26, color=GREEN, weight=BOLD)
        act4.to_edge(UP, buff=0.35)
        self.play(ReplacementTransform(act3, act4))

        out_spacing = 0.46
        out_neurons = VGroup()
        out_labels = VGroup()
        for i in range(10):
            y = (10 - 1) / 2 * out_spacing - i * out_spacing
            color = GREEN if i == 8 else GRAY_C
            n = Circle(radius=0.16, fill_color=color, fill_opacity=0.35,
                       stroke_color=color, stroke_width=2)
            n.move_to(RIGHT * 3.0 + UP * y)
            lbl = Text(str(i), font_size=14, color=color)
            lbl.next_to(n, LEFT, buff=0.08)
            out_neurons.add(n)
            out_labels.add(lbl)

        out_title = Text("Output\n(Softmax)", font_size=13, color=GREEN)
        out_title.next_to(out_neurons, UP, buff=0.15)

        edges3 = make_sparse_edges(h2_col, out_neurons, step_a=1, step_b=2)
        self.play(Create(edges3), run_time=0.7)
        self.play(LaggedStart(*[FadeIn(n, scale=0.5) for n in out_neurons],
                               lag_ratio=0.04), run_time=0.8)
        self.play(FadeIn(out_labels), FadeIn(out_title))
        self.wait(0.3)

        # Strong connections from loops to the "8" node
        neuron_8 = out_neurons[8]
        strong_edges = VGroup(
            Line(n_loop1.get_center(), neuron_8.get_center(),
                 stroke_color=YELLOW, stroke_width=2, stroke_opacity=0.85),
            Line(n_loop2.get_center(), neuron_8.get_center(),
                 stroke_color=YELLOW, stroke_width=2, stroke_opacity=0.85),
        )
        self.play(Create(strong_edges), run_time=0.6)

        # Probabilities as static text
        probs = [0, 0, 1, 1, 0, 0, 0, 0, 98, 0]
        prob_nums = VGroup()
        for i, (neuron, p) in enumerate(zip(out_neurons, probs)):
            col = GREEN if i == 8 else GRAY_C
            txt = Text(f"{p}%", font_size=11, color=col)
            txt.next_to(neuron, RIGHT, buff=0.07)
            prob_nums.add(txt)

        self.play(
            LaggedStart(*[FadeIn(n) for n in prob_nums], lag_ratio=0.04),
            run_time=0.7,
        )

        # Flash on the "8" node
        self.play(
            neuron_8.animate.set_fill(GREEN, opacity=1.0).scale(1.15),
            Flash(neuron_8, color=GREEN, flash_radius=0.35, line_length=0.10),
            run_time=0.6,
        )

        cap4 = Text(
            "Softmax converts activations to probabilities -- '8' wins with 98%",
            font_size=15, color=GREEN)
        cap4.to_edge(DOWN, buff=0.3)
        self.play(FadeIn(cap4))
        self.wait(3.0)
