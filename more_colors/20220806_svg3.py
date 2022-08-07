from typing_extensions import runtime
from manim import *
from sympy import Le
import X11colors as X11

def mkVGroup(mainVMobject, indices):
    grp = VGroup()
    for i in indices:
        grp.add(mainVMobject[i])
    return grp

class svg3(Scene):
    def construct(self):
        for x in range(-7, 8):
            for y in range(-4, 5):
                if (x==0) and (y==0):
                    self.add(Dot(np.array([x, y, 0]),radius=0.03, color=RED))        
                else:
                    self.add(Dot(np.array([x, y, 0]),radius=0.03, color=DARK_GREY))

        circuit = SVGMobject("20220806_nodeanalysis_01.svg", stroke_color=WHITE, fill_color=WHITE, height=6)
        lbls = index_labels(circuit, label_height=0.2, background_stroke_width=2, background_stroke_color='#000000')

        # self.play(Create(circuit), runtime=2)
        # self.add(lbls)

        lbl={}
        comp = {}
        comp['U1arrow'] = mkVGroup(circuit, [34, 35]).set_color(X11.COLOR['Firebrick1'])
        comp['U1'] = mkVGroup(circuit, [ 0, 1, 34, 35])
        comp['U1'].add(MathTex("U_1").move_to(comp['U1'].get_critical_point(LEFT),RIGHT).shift(0.1*(LEFT)).set_color(X11.COLOR['Firebrick1']))

        comp['R1'] = mkVGroup(circuit, [ 2, 3, 4, 5, 6, 7])
        comp['R1'].add(MathTex("R_1").move_to(comp['R1'].get_critical_point(UP),DOWN).shift(0.1*(UP)))

        comp['R2'] = mkVGroup(circuit, [ 8, 9,10,11,12,13])
        comp['R2'].add(MathTex("R_2").move_to(comp['R2'].get_critical_point(LEFT),RIGHT).shift(0.1*(LEFT)))

        comp['R3'] = mkVGroup(circuit, [14,15,16,17,18,19])
        comp['R3'].add(MathTex("R_3").move_to(comp['R3'].get_critical_point(UP),DOWN).shift(0.1*(UP)))

        comp['R4'] = mkVGroup(circuit, [20,21,22,23,24,25])
        comp['R4'].add(MathTex("R_4").move_to(comp['R4'].get_critical_point(LEFT),RIGHT).shift(0.1*(LEFT)))

        comp['gnd'] = mkVGroup(circuit, [36,37,38,39,40,41])
        comp['nodeA'] = mkVGroup(circuit, [26])
        lbl['nodeA'] = MathTex("A").move_to(comp['nodeA'].get_critical_point(UL),DOWN+RIGHT).shift(0.2*(UP+LEFT))

        comp['nodeB'] = mkVGroup(circuit, [27, 29, 33])
        lbl['nodeB'] = MathTex("B").move_to(comp['nodeB'].get_critical_point(UP),DOWN).shift(0.2*(UP))

        comp['nodeC'] = mkVGroup(circuit, [28])
        lbl['nodeC'] = MathTex("C").move_to(comp['nodeC'].get_critical_point(UR),DOWN+LEFT).shift(0.2*(UP+RIGHT))

        comp['nodeD'] = mkVGroup(circuit, [30, 31, 32])
        lbl['nodeD'] = MathTex("D").move_to(circuit[30].get_critical_point(DOWN),DOWN).shift(0.2*(UP))

        # circuit without GND symbol
        circ = mkVGroup(comp, ['U1', 'R1', 'R2', 'R3', 'R4','nodeA','nodeB','nodeC','nodeD'])

        self.play(Create(circ), runtime=4)

        for name in ['U1','R1','R2','R3','R4']:
            self.play(Indicate(comp[name], color=YELLOW, scale_factor=1.5), runtime=3)

        for node_n,node_c in [['nodeA',YELLOW],['nodeB',RED],['nodeC',BLUE],['nodeD',LIGHT_BROWN]]:
            comp[node_n].set_color(node_c)     
            self.play(Wiggle(comp[node_n], color=node_c), run_time=4)
            lbl[node_n].set_color(node_c) 
            self.play(Write(lbl[node_n]), run_time=1) 
            comp[node_n].add(lbl[node_n])

        comp['gnd'].set_color(LIGHT_BROWN)
        self.play(Create(comp['gnd']),runtime=2)

        # now the circuit is complete
        circ += comp['gnd']
        self.wait(2)

        # self.play(ScaleInPlace(circ, scale_factor=0.7), runtime=2)

        comp['I1'] = Arrow(comp['R1'].get_critical_point(DL),comp['R1'].get_critical_point(DR), stroke_width=4, buff=0).shift(0.2*DOWN)
        comp['I1'].add(MathTex("I_1").move_to(comp['I1'].get_critical_point(DOWN),UP).shift(0.0*DOWN))
        comp['I1'].set_color(X11.COLOR['DodgerBlue2'])
        self.play(Create(comp['I1']), runtime=2) 

        comp['I2'] = Arrow(comp['R2'].get_critical_point(UR),comp['R2'].get_critical_point(DR), stroke_width=4, buff=0).shift(0.2*RIGHT)
        comp['I2'].add(MathTex("I_2").move_to(comp['I2'].get_critical_point(RIGHT),LEFT).shift(0.0*RIGHT))
        comp['I2'].set_color(X11.COLOR['DodgerBlue2'])
        self.play(Create(comp['I2']), runtime=2) 

        comp['I3'] = Arrow(comp['R3'].get_critical_point(DL),comp['R3'].get_critical_point(DR), stroke_width=4, buff=0).shift(0.2*DOWN)
        comp['I3'].add(MathTex("I_3").move_to(comp['I3'].get_critical_point(DOWN),UP).shift(0.0*DOWN))
        comp['I3'].set_color(X11.COLOR['DodgerBlue2'])
        self.play(Create(comp['I3']), runtime=2) 

        comp['I4'] = Arrow(comp['R4'].get_critical_point(UR),comp['R4'].get_critical_point(DR), stroke_width=4, buff=0).shift(0.2*RIGHT)
        comp['I4'].add(MathTex("I_4").move_to(comp['I4'].get_critical_point(RIGHT),LEFT).shift(0.0*RIGHT))
        comp['I4'].set_color(X11.COLOR['DodgerBlue2'])
        self.play(Create(comp['I4']), runtime=2) 

        for name in ['I1','I2','I3','I4']:
            circ += comp[name]

        self.wait(2)
        self.play(circ.animate.scale(0.5).to_corner(UL))

        eq_currents = MathTex(
            r"I_1 &= \frac{V_A - V_B}{R_1}\\",
            r"I_2 &= \frac{V_B - V_D}{R_2}\\",
            r"I_3 &= \frac{V_B - V_C}{R_3}\\",
            r"I_4 &= \frac{V_C - V_D}{R_4}\\",
        ).move_to(circ.get_corner(DL), UP+LEFT).shift(0.2*DOWN).scale(0.7)

        self.play(Circumscribe(comp['I1'], Circle, color=X11.COLOR['OliveDrab1'], stroke_width=5))
        self.play(Write(eq_currents[0]), runtime=3)

        self.play(Circumscribe(comp['I2'], Circle, color=X11.COLOR['OliveDrab1'], stroke_width=5))
        self.play(Write(eq_currents[1]), runtime=3)

        self.play(Circumscribe(comp['I3'], Circle, color=X11.COLOR['OliveDrab1'], stroke_width=5))
        self.play(Write(eq_currents[2]), runtime=3)

        self.play(Circumscribe(comp['I4'], Circle, color=X11.COLOR['OliveDrab1'], stroke_width=5))
        self.play(Write(eq_currents[3]), runtime=3)

        self.wait(2)
