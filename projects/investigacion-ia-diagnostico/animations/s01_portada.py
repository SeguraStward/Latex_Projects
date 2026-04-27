from manim import *
import numpy as np

Text.set_default(font="Noto Sans", line_spacing=1.1)
config.background_color = "#030508"

# ── Contrast palette (designed for black background) ─────────────────────────
C_HI   = "#FFFFFF"    # main text — maximum contrast
C_MED  = "#E0E0E0"    # secondary names — perfectly readable
C_SUB  = "#A8A8A8"    # subtitles and small labels — readable
C_DIM  = "#727272"    # minor decorative elements
C_ACC  = "#5CE0CF"    # teal accent (TEAL_C equivalent)
C_ACC2 = "#78B4FF"    # blue accent


class S01_Portada(Scene):
    """
    Cinematic title card:
    Phase 1 — Neural network: layers and connections appear one by one
    Phase 2 — Forward pass activation + metrics
    Phase 3 — Elegant fade-out to black
    Phase 4 — Full screen with optimal contrast
    """

    def construct(self):

        # ══════════════════════════════════════════════════════════════════════
        # NEURAL NETWORK GEOMETRY
        # ══════════════════════════════════════════════════════════════════════
        LAYER_X  = [-5.2, -1.8,  1.6,  5.0]
        LAYER_N  = [  5,    7,    5,    3  ]
        LAYER_C  = [C_ACC2, C_ACC, C_ACC2, GREEN_C]
        NODE_R   = 0.16
        YGAP     = 0.80        # vertical node spacing

        # Nodes
        node_layers    = []
        node_positions = []
        for lx, ln, lc in zip(LAYER_X, LAYER_N, LAYER_C):
            ys  = np.linspace(-(ln - 1) / 2 * YGAP, (ln - 1) / 2 * YGAP, ln)
            grp = VGroup(*[
                Circle(radius=NODE_R,
                       fill_color=lc, fill_opacity=0.88,
                       stroke_color=lc, stroke_width=1.5)
                .move_to(np.array([lx, y, 0]))
                for y in ys
            ])
            node_layers.append(grp)
            node_positions.append([np.array([lx, y, 0]) for y in ys])

        # Connections between adjacent layer pairs
        edge_layers = []
        for i in range(len(node_layers) - 1):
            eg = VGroup(*[
                Line(p1, p2,
                     stroke_color=BLUE_E,
                     stroke_width=0.40, stroke_opacity=0.18)
                for p1 in node_positions[i]
                for p2 in node_positions[i + 1]
            ])
            edge_layers.append(eg)

        all_nodes = VGroup(*node_layers)
        all_edges = VGroup(*edge_layers)
        net       = VGroup(all_edges, all_nodes)

        # Shift network upward to leave space for metrics
        net.shift(UP * 0.70)

        # ══════════════════════════════════════════════════════════════════════
        # PHASE 1 — Layer-by-layer appearance with connections
        # ══════════════════════════════════════════════════════════════════════
        for i, ng in enumerate(node_layers):
            self.play(
                LaggedStart(*[FadeIn(n, scale=0.35) for n in ng],
                            lag_ratio=0.10),
                run_time=0.50,
            )
            if i < len(edge_layers):
                self.play(
                    Create(edge_layers[i]),
                    run_time=0.40,
                )

        self.wait(0.15)

        # ══════════════════════════════════════════════════════════════════════
        # PHASE 2a — Forward pass: activation travels left to right
        # ══════════════════════════════════════════════════════════════════════
        ORIG_C = [C_ACC2, C_ACC, C_ACC2, GREEN_C]

        def pulse_nodes(ng, c_on):
            self.play(
                *[n.animate.set_fill(WHITE, 1.0).set_stroke(WHITE, 2.5)
                  for n in ng],
                run_time=0.17,
            )
            self.play(
                *[n.animate.set_fill(c_on, 0.88).set_stroke(c_on, 1.5)
                  for n in ng],
                run_time=0.13,
            )

        def pulse_edges(eg):
            self.play(
                eg.animate.set_stroke(C_ACC, width=0.85, opacity=0.50),
                run_time=0.17,
            )
            self.play(
                eg.animate.set_stroke(BLUE_E, width=0.40, opacity=0.18),
                run_time=0.13,
            )

        for i, ng in enumerate(node_layers):
            pulse_nodes(ng, ORIG_C[i])
            if i < len(edge_layers):
                pulse_edges(edge_layers[i])

        self.wait(0.20)

        # ══════════════════════════════════════════════════════════════════════
        # PHASE 2b — Key metrics emerge below the network
        # ══════════════════════════════════════════════════════════════════════
        metrics_data = [
            ("AUC",           "0.932",   C_ACC,  LEFT  * 3.8),
            ("Sensitivity",   "94.7 %",  "#66DD88", ORIGIN),
            ("Specificity",   "91.2 %",  C_ACC2, RIGHT * 3.8),
        ]

        m_groups = VGroup()
        for mlbl, mval, mcol, mpos in metrics_data:
            card = RoundedRectangle(
                width=3.0, height=1.20, corner_radius=0.10,
                fill_color="#04080f", fill_opacity=0.95,
                stroke_color=mcol, stroke_width=1.5,
            ).move_to(mpos + DOWN * 2.65)
            lbl  = Text(mlbl, font_size=13, color=mcol)
            lbl.move_to(card.get_center() + UP * 0.27)
            val  = Text(mval, font_size=24, color=mcol, weight=BOLD)
            val.move_to(card.get_center() + DOWN * 0.19)
            m_groups.add(VGroup(card, lbl, val))

        self.play(
            LaggedStart(*[FadeIn(mg, shift=UP * 0.14) for mg in m_groups],
                        lag_ratio=0.18),
            run_time=0.90,
        )
        self.wait(1.0)

        # ══════════════════════════════════════════════════════════════════════
        # PHASE 3 — Elegant fade-out
        # ══════════════════════════════════════════════════════════════════════
        self.play(
            FadeOut(net),
            FadeOut(m_groups),
            run_time=1.1, rate_func=smooth,
        )
        self.wait(0.20)

        # ══════════════════════════════════════════════════════════════════════
        # PHASE 4 — Full screen · optimized contrast
        # ══════════════════════════════════════════════════════════════════════

        # Very subtle point texture (keeps the tech look)
        np.random.seed(77)
        bg_tex = VGroup(*[
            Dot(np.array([np.random.uniform(-7.0, 7.0),
                          np.random.uniform(-4.0, 4.0), 0]),
                radius=0.020, color=BLUE_E, fill_opacity=0.05)
            for _ in range(55)
        ])
        self.play(FadeIn(bg_tex), run_time=0.35)

        # ── Institutional header ──────────────────────────────────────────────
        univ   = Text("Universidad Nacional",
                      font_size=15, color=C_MED, weight=BOLD)
        campus = Text("Sede Regional Brunca — Campus Perez Zeledon",
                      font_size=11, color=C_SUB)
        curso  = Text("Course: Artificial Intelligence",
                      font_size=11, color=C_SUB)
        header = VGroup(univ, campus, curso).arrange(DOWN, buff=0.09)
        header.move_to(UP * 3.38)

        sep_t = Line(LEFT * 7.0, RIGHT * 7.0,
                     stroke_color=C_ACC, stroke_width=1.1, stroke_opacity=0.45)
        sep_t.move_to(UP * 2.72)

        self.play(FadeIn(header, shift=DOWN * 0.12), run_time=0.45)
        self.play(Create(sep_t), run_time=0.32)

        # ── Main title ────────────────────────────────────────────────────────
        t1 = Text("Artificial Intelligence",
                  font_size=48, color=C_ACC, weight=BOLD)
        t2 = Text("in Medical Diagnosis",
                  font_size=48, color=C_HI, weight=BOLD)
        VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 1.30)

        sub_t = Text("Deep Learning  .  CNN  .  Image-Based Diagnosis",
                     font_size=14, color=C_SUB)
        sub_t.move_to(UP * 0.0)

        self.play(Write(t1), run_time=0.75)
        self.play(Write(t2), run_time=0.75)
        self.play(FadeIn(sub_t, shift=UP * 0.10), run_time=0.38)

        sep_b = Line(LEFT * 7.0, RIGHT * 7.0,
                     stroke_color=C_ACC, stroke_width=1.1, stroke_opacity=0.45)
        sep_b.move_to(DOWN * 0.65)
        self.play(Create(sep_b), run_time=0.32)

        # ── Professor (left) · Student (right) ───────────────────────────────
        prof_role = Text("PROFESSOR", font_size=10, color=C_ACC,
                         weight=BOLD, slant=ITALIC)
        prof_name = Text("Prof. Pablo Andres Venegas Elizondo",
                         font_size=19, color=C_HI, weight=BOLD)
        prof_grp  = VGroup(prof_role, prof_name).arrange(DOWN, buff=0.09)
        prof_grp.move_to(LEFT * 2.6 + DOWN * 1.52)

        stu_role = Text("STUDENT", font_size=10, color=C_SUB,
                        weight=BOLD, slant=ITALIC)
        stu_name = Text("Angel Stward Segura Mendez",
                        font_size=17, color=C_MED)
        stu_grp  = VGroup(stu_role, stu_name).arrange(DOWN, buff=0.09)
        stu_grp.move_to(RIGHT * 2.6 + DOWN * 1.52)

        # Subtle vertical divider between the two columns
        col_div = Line(UP * 0.2, DOWN * 2.2,
                       stroke_color=C_ACC, stroke_width=0.7, stroke_opacity=0.30)
        col_div.move_to(DOWN * 1.0)

        date = Text("March, 2026", font_size=12, color=C_DIM)
        date.move_to(DOWN * 3.05)

        self.play(FadeIn(col_div), run_time=0.25)
        self.play(
            FadeIn(prof_grp, shift=UP * 0.12),
            FadeIn(stu_grp,  shift=UP * 0.12),
            run_time=0.55,
        )
        self.play(FadeIn(date), run_time=0.30)

        self.wait(3.0)
