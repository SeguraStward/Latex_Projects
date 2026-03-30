from manim import *
import numpy as np

# =============================================================================
# helpers.py — Utilidades compartidas entre escenas
# =============================================================================


def make_neuron_col(x, color, n=10, spacing=0.36):
    """Columna vertical de n neuronas en la posicion x."""
    col = VGroup()
    for i in range(n):
        y = (n - 1) / 2 * spacing - i * spacing
        dot = Circle(radius=0.13, fill_color=color, fill_opacity=0.5,
                     stroke_color=color, stroke_width=1.5)
        dot.move_to(RIGHT * x + UP * y)
        col.add(dot)
    return col


def make_sparse_edges(col_a, col_b, step_a=2, step_b=2):
    """Conexiones dispersas entre dos columnas de neuronas."""
    edges = VGroup()
    for a in col_a[::step_a]:
        for b in col_b[::step_b]:
            edges.add(Line(a.get_center(), b.get_center(),
                           stroke_width=0.9, stroke_color=GRAY_C,
                           stroke_opacity=0.55))
    return edges


def make_pixel_grid(matrix, cell=0.4):
    """Cuadricula de pixeles a partir de una matriz 2D (valores 0/1)."""
    rows, cols = len(matrix), len(matrix[0])
    g = VGroup()
    for r in range(rows):
        for c in range(cols):
            val = matrix[r][c]
            sq = Square(side_length=cell,
                        fill_color=WHITE, fill_opacity=float(val) * 0.92,
                        stroke_color=GRAY_D, stroke_width=0.6)
            sq.move_to(RIGHT * c * cell + DOWN * r * cell)
            g.add(sq)
    g.move_to(ORIGIN)
    return g


def make_mini_pattern(pattern, cell=0.22):
    """Mini cuadricula para mostrar que patron activa una neurona."""
    g = VGroup()
    for r, row in enumerate(pattern):
        for c, val in enumerate(row):
            sq = Square(side_length=cell,
                        fill_color=YELLOW if val else "#222233",
                        fill_opacity=0.95 if val else 0.7,
                        stroke_color=GRAY_D, stroke_width=0.4)
            sq.move_to(RIGHT * c * cell + DOWN * r * cell)
            g.add(sq)
    g.move_to(ORIGIN)
    return g


def make_eye(iris_color=BLUE_C, pupil_color="#111111"):
    """Ojo humano: esclerotica, iris, pupila, brillo, parpados, pestanas."""
    sclera = Ellipse(width=2.0, height=1.1,
                     fill_color="#f0ece8", fill_opacity=0.95,
                     stroke_color="#d4a574", stroke_width=2)
    iris = Circle(radius=0.38, fill_color=iris_color, fill_opacity=0.9,
                  stroke_color=BLUE_D, stroke_width=1.5)
    pupil = Circle(radius=0.17, fill_color=pupil_color,
                   fill_opacity=1, stroke_width=0)
    shine = Dot(radius=0.06, color=WHITE, fill_opacity=0.9)
    shine.move_to(pupil.get_center() + UP * 0.1 + RIGHT * 0.08)
    top_lid = Arc(radius=1.0, start_angle=0, angle=PI,
                  stroke_color="#d4a574", stroke_width=3, fill_opacity=0)
    bot_lid = Arc(radius=1.0, start_angle=PI, angle=PI,
                  stroke_color="#d4a574", stroke_width=3, fill_opacity=0)
    lashes = VGroup(*[
        Line(top_lid.point_from_proportion(0.15 + i * 0.12),
             top_lid.point_from_proportion(0.15 + i * 0.12) + UP * 0.18,
             stroke_color="#3a2a1a", stroke_width=1.5)
        for i in range(6)
    ])
    # eye[0]=sclera  eye[1]=iris  eye[2]=pupil  eye[3]=shine
    eye = VGroup(sclera, iris, pupil, shine, top_lid, bot_lid, lashes)
    return eye
