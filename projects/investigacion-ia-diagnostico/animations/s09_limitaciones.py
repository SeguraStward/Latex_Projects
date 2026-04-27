from manim import *

Text.set_default(font="Noto Sans", line_spacing=1.1)


class S09_Limitaciones(Scene):
    """
    Limitations and ethical challenges -- 6 key topics.
    """

    def construct(self):

        title = Text("Limitations and Challenges", font_size=36,
                     color=ORANGE, weight=BOLD)
        title.to_edge(UP, buff=0.35)
        self.play(Write(title), run_time=0.7)

        # ══════════════════════════════════════════════════════════════════════
        # ACT 1 — Bias and Generalization
        # ══════════════════════════════════════════════════════════════════════
        act1_lbl = Text("1.  Bias and Generalization",
                        font_size=20, color=YELLOW, weight=BOLD)
        act1_lbl.next_to(title, DOWN, buff=0.28)
        self.play(FadeIn(act1_lbl, shift=DOWN * 0.1), run_time=0.45)

        # Two hospitals compared
        hosp_a = RoundedRectangle(
            width=3.8, height=2.2, corner_radius=0.10,
            fill_color="#0a1a0a", fill_opacity=0.80,
            stroke_color=GREEN_C, stroke_width=1.5,
        ).move_to(LEFT * 2.8 + DOWN * 0.8)
        ha_title = Text("Hospital A", font_size=14, color=GREEN_C, weight=BOLD)
        ha_title.move_to(hosp_a.get_top() + DOWN * 0.25)
        ha_acc = Text("95% accuracy", font_size=20, color=GREEN_C, weight=BOLD)
        ha_acc.move_to(hosp_a.get_center())
        ha_note = Text("Same equipment and\ntraining population",
                       font_size=10, color="#999999", line_spacing=1.2)
        ha_note.move_to(hosp_a.get_bottom() + UP * 0.35)

        hosp_b = RoundedRectangle(
            width=3.8, height=2.2, corner_radius=0.10,
            fill_color="#1a0a0a", fill_opacity=0.80,
            stroke_color=RED, stroke_width=1.5,
        ).move_to(RIGHT * 2.8 + DOWN * 0.8)
        hb_title = Text("Hospital B", font_size=14, color=RED, weight=BOLD)
        hb_title.move_to(hosp_b.get_top() + DOWN * 0.25)
        hb_acc = Text("~80% accuracy", font_size=20, color=RED, weight=BOLD)
        hb_acc.move_to(hosp_b.get_center())
        hb_note = Text("Different equipment,\ndifferent population",
                       font_size=10, color="#999999", line_spacing=1.2)
        hb_note.move_to(hosp_b.get_bottom() + UP * 0.35)

        arrow_drop = Arrow(
            hosp_a.get_right(), hosp_b.get_left(),
            buff=0.15, color=YELLOW, stroke_width=2.5, tip_length=0.18,
        )
        drop_lbl = Text("-15%", font_size=16, color=YELLOW, weight=BOLD)
        drop_lbl.next_to(arrow_drop, UP, buff=0.08)

        self.play(FadeIn(hosp_a), FadeIn(ha_title), FadeIn(ha_acc),
                  FadeIn(ha_note), run_time=0.5)
        self.play(GrowArrow(arrow_drop), FadeIn(drop_lbl), run_time=0.4)
        self.play(FadeIn(hosp_b), FadeIn(hb_title), FadeIn(hb_acc),
                  FadeIn(hb_note), run_time=0.5)
        self.wait(1.2)

        act1_all = VGroup(act1_lbl, hosp_a, ha_title, ha_acc, ha_note,
                          hosp_b, hb_title, hb_acc, hb_note,
                          arrow_drop, drop_lbl)
        self.play(FadeOut(act1_all), run_time=0.45)

        # ══════════════════════════════════════════════════════════════════════
        # ACT 2 — Black Box + XAI
        # ══════════════════════════════════════════════════════════════════════
        act2_lbl = Text("2.  Interpretability -- Black Box",
                        font_size=20, color=ORANGE, weight=BOLD)
        act2_lbl.next_to(title, DOWN, buff=0.28)
        self.play(FadeIn(act2_lbl, shift=DOWN * 0.1), run_time=0.45)

        # Simplified black box
        bbox = Rectangle(width=3.5, height=2.0,
                         fill_color="#040408", fill_opacity=1,
                         stroke_color=GRAY_C, stroke_width=2)
        bbox.move_to(DOWN * 0.5)
        q_mark = Text("?", font_size=70, color=GRAY_C, weight=BOLD)
        q_mark.move_to(bbox.get_center())

        arr_in = Arrow(LEFT * 4.5 + DOWN * 0.5, bbox.get_left(),
                       buff=0.12, color=BLUE_C, stroke_width=2, tip_length=0.18)
        lbl_in = Text("Image", font_size=12, color=BLUE_C)
        lbl_in.next_to(arr_in, UP, buff=0.06)

        arr_out = Arrow(bbox.get_right(), RIGHT * 4.5 + DOWN * 0.5,
                        buff=0.12, color=GREEN, stroke_width=2, tip_length=0.18)
        lbl_out = Text("Malignant 94.7%", font_size=12, color=GREEN, weight=BOLD)
        lbl_out.next_to(arr_out, UP, buff=0.06)

        self.play(FadeIn(bbox), FadeIn(q_mark), run_time=0.4)
        self.play(GrowArrow(arr_in), FadeIn(lbl_in),
                  GrowArrow(arr_out), FadeIn(lbl_out), run_time=0.5)

        xai_note = Text("XAI (Grad-CAM, SHAP) tries to explain,\n"
                        "but radiologists find it insufficient",
                        font_size=12, color=YELLOW, line_spacing=1.2)
        xai_note.to_edge(DOWN, buff=0.50)
        self.play(FadeIn(xai_note, shift=UP * 0.15), run_time=0.5)
        self.wait(1.2)

        act2_all = VGroup(act2_lbl, bbox, q_mark, arr_in, lbl_in,
                          arr_out, lbl_out, xai_note)
        self.play(FadeOut(act2_all), run_time=0.45)

        # ══════════════════════════════════════════════════════════════════════
        # ACT 3 — 4 remaining challenges (compact)
        # ══════════════════════════════════════════════════════════════════════
        act3_lbl = Text("Additional Challenges",
                        font_size=20, color=RED, weight=BOLD)
        act3_lbl.next_to(title, DOWN, buff=0.28)
        self.play(FadeIn(act3_lbl, shift=DOWN * 0.1), run_time=0.45)

        challenges = [
            ("Regulation",    "FDA/MDR approve static\nversions; updates require\n"
                              "new authorization",
             YELLOW,   LEFT * 3.2 + DOWN * 0.3),
            ("Accountability","The radiologist signs and is\nlegally responsible\n"
                              "for the diagnosis",
             RED,      RIGHT * 3.2 + DOWN * 0.3),
            ("Integration",   "Legacy systems make it hard\n"
                              "to integrate AI into PACS/RIS",
             BLUE_C,   LEFT * 3.2 + DOWN * 2.5),
            ("Scalability",   "Expensive GPUs + expert\n"
                              "labeling = prohibitive\nfor small clinics",
             PURPLE_B, RIGHT * 3.2 + DOWN * 2.5),
        ]

        all_ch = VGroup()
        for name, desc, color, pos in challenges:
            card = RoundedRectangle(
                width=4.8, height=1.6, corner_radius=0.10,
                fill_color="#080c14", fill_opacity=0.85,
                stroke_color=color, stroke_width=1.4,
            ).move_to(pos)
            n_txt = Text(name, font_size=14, color=color, weight=BOLD)
            n_txt.move_to(card.get_top() + DOWN * 0.25)
            d_txt = Text(desc, font_size=10, color="#B0B0B0", line_spacing=1.2)
            d_txt.move_to(card.get_center() + DOWN * 0.15)
            all_ch.add(VGroup(card, n_txt, d_txt))

        self.play(
            LaggedStart(*[FadeIn(ch, shift=UP * 0.15) for ch in all_ch],
                        lag_ratio=0.20),
            run_time=1.2,
        )
        self.wait(1.2)

        # Closing
        close_txt = Text(
            "AI is a co-pilot, not a replacement for the specialist",
            font_size=16, color=TEAL_C, weight=BOLD,
        )
        close_txt.to_edge(DOWN, buff=0.30)
        close_box = SurroundingRectangle(close_txt, color=TEAL_C,
                                         buff=0.14, stroke_width=1.3)
        self.play(FadeIn(close_txt), Create(close_box), run_time=0.55)
        self.wait(3.0)
