from manimlib.imports import *


class Intro(Scene):
    def construct(self):
        title = TextMobject("Linear Equations", color=RED)
        title.scale(2)

        eq1 = TexMobject("2y = 3x + 2").scale(1.5).shift(2 * LEFT + 1 * UP)
        eq2 = TexMobject("y = x + 3").scale(1.5).shift(3 * LEFT + 1 * DOWN)
        eq3 = TexMobject("3y + 2x = 1").scale(1.5).shift(2 * LEFT + 3 * DOWN)

        axes = Axes(
            x_min=-3,
            x_max=3,
            y_min=-3,
            y_max=3,
            number_line_config={
                "include_tip": False,
            }
        )
        f = FunctionGraph(lambda x: 0.5*x + 1, x_min=-3, x_max=3)
        func = VGroup(axes, f)

        func.shift(2 * RIGHT + 1 * DOWN)

        self.play(Write(title))
        self.wait()

        self.play(title.shift, 3 * UP)
        self.wait()

        self.play(Write(func), Write(eq1), Write(eq2), Write(eq3))
        self.wait()


class Shapes(Scene):
    def construct(self):
        circle = Circle(radius=1)
        square = Square()
        line = Line(np.array([3, 0, 0]), np.array([5, 0, 0]))
        triangle = Polygon(np.array([0, 0, 0]), np.array(
            [1, 1, 0]), np.array([1, -1, 0]))
        ellipse = Ellipse(width=2.7, height=5.7)
        dashedline = DashedLine(dash_length=1)

        # self.add(ellipse)
        # self.add(line)
        self.add(dashedline)
        self.play(ShowCreation(circle))
        self.play(FadeOut(circle))
        self.play(GrowFromCenter(square))
        self.play(Transform(square, triangle))


class MoreShapes(Scene):
    def construct(self):
        circle = Circle(color=PURPLE_A)
        square = Square(fill_color=GOLD_B, fill_opacity=1, color=GOLD_A)
        square.move_to(UP+LEFT)
        circle.surround(square)
        rectangle = Rectangle(height=2, width=3)
        ellipse = Ellipse(width=3, height=1, color=RED)
        ellipse.shift(2*DOWN+2*RIGHT)
        pointer = CurvedArrow(2*RIGHT, 5*RIGHT, color=MAROON_C)
        arrow = Arrow(LEFT, UP)
        arrow.next_to(circle, DOWN+LEFT)
        rectangle.next_to(arrow, DOWN+LEFT)
        ring = Annulus(inner_radius=.5, outer_radius=1, color=BLUE)
        ring.next_to(ellipse, RIGHT)

        self.add(pointer)
        self.play(FadeIn(square))
        self.play(Rotating(square), FadeIn(circle))
        self.play(GrowArrow(arrow))
        self.play(GrowFromCenter(rectangle), GrowFromCenter(
            ellipse), GrowFromCenter(ring))


class AddingText(Scene):
    def construct(self):
        my_first_text = TextMobject("Writing with manim is fun")
        second_line = TextMobject("and easy to do!")
        second_line.next_to(my_first_text, DOWN)
        third_line = TextMobject("for me and you!")
        third_line.next_to(my_first_text, DOWN)
        self.add(my_first_text, second_line)
        self.wait(2)
        self.play(Transform(second_line, third_line))
        self.wait(2)
        second_line.shift(3*DOWN)
        self.play(ApplyMethod(my_first_text.shift, 3*UP))


class AddingMoreText(Scene):
    def construct(self):
        quote = TextMobject("Imagination is more important than knowledge")
        quote.set_color(RED)
        quote.to_edge(UP)
        quote2 = TextMobject(
            "A person who never made a mistake never tried anything new")
        quote2.set_color(YELLOW)
        author = TextMobject("-Albert Einstein")
        author.scale(0.75)
        author.next_to(quote.get_corner(DOWN+RIGHT), DOWN)
        self.add(quote)
        self.add(author)
        self.wait(2)
        self.play(Transform(quote, quote2), ApplyMethod(
            author.move_to, quote2.get_corner(DOWN+RIGHT)+DOWN+2*LEFT))
        self.play(ApplyMethod(author.match_color, quote2),
                  Transform(author, author.scale(1)))
        self.play(FadeOut(quote))


class BasicEquations(Scene):
    def construct(self):
        eq1 = TexMobject("\\vec{X}_0 \\cdot \\vec{Y}_1 = 3")
        eq1.shift(2*UP)
        eq2 = TexMobject("\\vec{F}_{net} = \\sum_i \\vec{F}_i")
        eq2.shift(2*DOWN)
        self.play(Write(eq1))
        self.play(Write(eq2))


class ColoringEquations(Scene):
    def construct(self):
        line1 = TexMobject("\\text{The vector }", "\\vec{F}_{net}",
                           "\\text{ is the net force on object of mass }")
        line1.set_color_by_tex("F", BLUE)
        line2 = TexMobject("m", "\\text{ and acceleration }", "\\vec{a}", ". ")
        line2.set_color_by_tex_to_color_map({"m": YELLOW, "{a}": RED})
        sentence = VGroup(line1, line2)
        sentence.arrange_submobjects(DOWN, buff=MED_LARGE_BUFF)
        self.play(Write(sentence))


class UsingBraces(Scene):
    def construct(self):
        eq1A = TextMobject("4x + 3y")
        eq1B = TextMobject("=")
        eq1C = TextMobject("0")
        eq2A = TextMobject("5x -2y")
        eq2B = TextMobject("=")
        eq2C = TextMobject("3")
        eq1B.next_to(eq1A, RIGHT)
        eq1C.next_to(eq1B, RIGHT)
        eq2A.shift(DOWN)
        eq2B.shift(DOWN)
        eq2C.shift(DOWN)
        eq2A.align_to(eq1A, LEFT)
        eq2B.align_to(eq1B, LEFT)
        eq2C.align_to(eq1C, LEFT)

        eq_group = VGroup(eq1A, eq2A)
        braces = Brace(eq_group, LEFT)
        eq_text = braces.get_text("A pair of equations")
        self.add(eq1A, eq1B, eq1C)
        self.add(eq2A, eq2B, eq2C)
        self.play(GrowFromCenter(braces), Write(eq_text))


class PlotFunctions(GraphScene):
    CONFIG = {
        "x_min": -10,
        "x_max": 10.3,
        "y_min": -1.5,
        "y_max": 1.5,
        "graph_origin": ORIGIN,
        "function_color": RED,
        "axes_color": GREEN,
        "x_labeled_nums": range(-10, 12, 2),
    }

    def construct(self):
        self.setup_axes(True)
        func_graph = self.get_graph(lambda x: np.cos(x), RED)
        func_graph2 = self.get_graph(lambda x: np.sin(x))
        vert_line = self.get_vertical_line_to_graph(
            TAU, func_graph, color=YELLOW)
        graph_lab = self.get_graph_label(func_graph, label="\\cos(x)")
        graph_lab2 = self.get_graph_label(
            func_graph2, label="\\sin(x)", x_val=-10, direction=UP/2)
        two_pi = TexMobject("x = 2 \\pi")
        label_coord = self.input_to_graph_point(TAU, func_graph)
        two_pi.next_to(label_coord, RIGHT+UP)

        self.play(ShowCreation(func_graph), ShowCreation(func_graph2))
        self.play(ShowCreation(vert_line), ShowCreation(graph_lab),
                  ShowCreation(graph_lab2), ShowCreation(two_pi))


class ExampleApproximation(GraphScene):
    CONFIG = {
        "function": lambda x: np.cos(x),
        "function_color": BLUE,
        "taylor": [lambda x: 1, lambda x: 1-x**2/2, lambda x: 1-x**2/math.factorial(2)+x**4/math.factorial(4), lambda x: 1-x**2/2+x**4/math.factorial(4)-x**6/math.factorial(6),
                   lambda x: 1-x**2/math.factorial(2)+x**4/math.factorial(4)-x**6/math.factorial(6)+x**8/math.factorial(8), lambda x: 1-x**2/math.factorial(2)+x**4/math.factorial(4)-x**6/math.factorial(6)+x**8/math.factorial(8) - x**10/math.factorial(10)],
        "center_point": 0,
        "approximation_color": GREEN,
        "x_min": -10,
        "x_max": 10,
        "y_min": -1,
        "y_max": 1,
        "graph_origin": ORIGIN,
        "x_labeled_nums": range(-10, 12, 2),

    }

    def construct(self):
        self.setup_axes(animate=True)

        func_graph = self.get_graph(self.function, self.function_color)

        approx_graphs = [self.get_graph(
            f, self.approximation_color) for f in self.taylor]

        term_num = [TexMobject("n = " + str(n), aligned_edge=TOP)
                    for n in range(0, 8)]
        #[t.to_edge(BOTTOM,buff=SMALL_BUFF) for t in term_num]

        #term = TexMobject("")
        # term.to_edge(BOTTOM,buff=SMALL_BUFF)
        term = VectorizedPoint(3*DOWN)

        approx_graph = VectorizedPoint(
            self.input_to_graph_point(self.center_point, func_graph)
        )

        self.play(
            ShowCreation(func_graph),
        )

        for n in range(6):
            self.play(
                Transform(approx_graph, approx_graphs[n], run_time=2),
                Transform(term, term_num[n])
            )
            self.wait()


class DrawAnAxis1(Scene):
    CONFIG = {"plane_kwargs": {
        "x_line_frequency": 2,
        "y_line_frequency": 2
    }
    }

    def construct(self):
        my_plane = NumberPlane(**self.plane_kwargs)
        my_plane.add(my_plane.get_axis_labels())
        self.add(my_plane)


class SimpleField(Scene):
    CONFIG = {
        "plane_kwargs": {
            "color": RED_A
        },
    }

    def construct(self):
        plane = NumberPlane(**self.plane_kwargs)
        plane.add(plane.get_axis_labels())
        self.add(plane)

        points = [x*RIGHT+y*UP
                  for x in np.arange(-5, 5, 1)
                  for y in np.arange(-5, 5, 1)
                  ]

        vec_field = []
        for point in points:
            field = 0.5*RIGHT + 0.5*UP
            result = Vector(field).shift(point)
            vec_field.append(result)

        draw_field = VGroup(*vec_field)

        self.play(ShowCreation(draw_field))
