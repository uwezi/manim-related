from manim import *

'''
myTexTemplate = TexTemplate(
                    tex_compiler="xelatex",
                    output_format='.pdf',
                    )
myTexTemplate.add_to_preamble(r"\usepackage{siunitx}\usepackage{stix2}\usepackage{listings}")

MathTex.set_default(tex_template=myTexTemplate) 
Tex.set_default(tex_template=myTexTemplate) 
'''

'''
config.pixel_width=320
config.pixel_height=180
'''

class unitcircle(Scene):
    def construct(self):
        ax = Axes(
            x_range  = [-1.2,1.2,0.5],
            y_range  = [-1.2,1.2,0.5],
            x_length = 7,
            y_length = 7,
            axis_config = {
                'include_tip': False,
                'include_numbers': True,
                'font_size': 22,
            }
        )
        self.play(Create(ax))

        circle = Circle().from_three_points(ax.c2p(1,0),ax.c2p(0,1),ax.c2p(-1,0))
        circle.set_color(WHITE)
        self.play(Create(circle))

        xVal = ValueTracker(0.8)

        dotA = Dot(ax.c2p(0,0), color=YELLOW)
        letterA = MathTex(r"A", color=YELLOW).next_to(dotA, DL, buff=0.1)
        self.add(dotA, letterA)

        def get_dotC():
            return VGroup(
                Dot(ax.c2p(xVal.get_value(),0), color=YELLOW),
                MathTex(r"C", color=YELLOW).move_to(ax.c2p(xVal.get_value(),0),aligned_edge=UL).shift(0.1*DR),
            ) 
        dotC = always_redraw(get_dotC)
        self.add(dotC)
        
        dotB = Dot(ax.c2p(xVal.get_value(),np.sqrt(1-xVal.get_value()**2)), color=YELLOW)
        def dotBUpdater(obj):
            obj.move_to(ax.c2p(xVal.get_value(),np.sqrt(1-xVal.get_value()**2)))
        dotB.add_updater(dotBUpdater)
        self.add(dotB)
        
        letterB = MathTex(r"B", color=YELLOW).next_to(dotB, RIGHT+UP, buff=0.1)
        def letterBUpdater(obj):
            obj.next_to(dotB, RIGHT+UP, buff=0.1)
        letterB.add_updater(letterBUpdater)
        self.play(Write(letterB))

        arc = Arc(
            radius=circle.radius,
            start_angle = 0,
            angle = np.arccos(xVal.get_value()),
            arc_center=ax.c2p(0,0),
            color = RED,
            stroke_width = 5,
        )

        def get_arcNumber():
            return DecimalNumber(
                np.arccos(xVal.get_value()),
                font_size=30,
                unit=r"\text{~~rad}",
            ).rotate(-np.pi/2).move_to(ax.c2p(1.1,0)).rotate(np.arccos(xVal.get_value())*0.5,about_point=ax.c2p(0,0)).set_color(RED)
        arcNumber = always_redraw(get_arcNumber)

        def get_sector():
            x = xVal.get_value()
            if x>=0:
                p = Polygon(
                    ax.c2p(0,0),
                    ax.c2p(x,np.sqrt(1-x**2)),
                    ax.c2p(1,np.sqrt(1-x**2)),
                    ax.c2p(1,0),
                    ax.c2p(0,0),
                )
            else:
                p = Polygon(
                    ax.c2p(0,0),
                    ax.c2p(-1/(np.tan(np.arccos(-x))),1),
                    ax.c2p(1,1),
                    ax.c2p(1,0),
                    ax.c2p(0,0),
                )
            return Intersection(
            circle.copy(),
            p,
            fill_opacity = 0.5,
            fill_color = RED,                    
            )

        sector = always_redraw(get_sector)
        self.play(Create(sector))

        def get_triangle():
            return Polygon(
                        ax.c2p(0,0),
                        ax.c2p(xVal.get_value(),0),
                        ax.c2p(xVal.get_value(),np.sqrt(1-xVal.get_value()**2)),
                        stroke_width = 1,
                        color = BLUE,
                        fill_color=BLUE,
                        fill_opacity=0.5,
                    )

        triangle = always_redraw(get_triangle)
        self.play(Create(triangle))

        def arcUpdater(obj):
            obj.become(
                Arc(
                    radius=circle.radius,
                    start_angle = 0,
                    angle = np.arccos(xVal.get_value()),
                    arc_center=ax.c2p(0,0),
                    color = RED,
                    stroke_width = 5,
                )
            )
        arc.add_updater(arcUpdater) 
        self.play(Create(arc),Write(arcNumber))   

        angle = Arc(
            radius=0.2*circle.radius,
            start_angle = 0,
            angle = np.arccos(xVal.get_value()),
            arc_center=ax.c2p(0,0),
            color = GREEN,
            stroke_width = 5,
        )

        def get_angleNumber():
            return VGroup(
                MathTex(r"\alpha=", font_size=30),
                DecimalNumber(
                    np.arccos(xVal.get_value())*180/np.pi,
                    font_size = 30,
                    num_decimal_places=1,
                    unit="^\circ",
                )
            ).arrange(RIGHT).next_to(angle,DOWN).set_color(GREEN)
        angleNumber = always_redraw(get_angleNumber)

        def angleUpdater(obj):
            obj.become(
                Arc(
                    radius=0.2*circle.radius,
                    start_angle = 0,
                    angle = np.arccos(xVal.get_value()),
                    arc_center=ax.c2p(0,0),
                    color = GREEN,
                    stroke_width = 5,
                )
            )

        angle.add_updater(angleUpdater) 
        self.play(Create(angle),Write(angleNumber))   

        self.wait(1)
        self.play(xVal.animate.set_value(0), run_time=4)

        self.play(xVal.animate.set_value(0.9), run_time=4)

        self.play(xVal.animate.set_value(-0.8), run_time=4)

        self.play(xVal.animate.set_value(0.5), run_time=4)

        self.wait(2)