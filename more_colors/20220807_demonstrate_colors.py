from os import remove
from typing_extensions import runtime
from manim import *
from sympy import Le
import X11colors as X11
import RALcolors as RAL
import NBScolors as NBS
import NCScolors as NCS
import XKCDcolors as XKCD
import RESENEcolors as RESENE
import FS595colors as FS595
import BS381colors as BS381
import BS4800colors as BS4800
import AS2700colors as AS2700
import CRAYOLAcolors as CRAYOLA

class demonstrate_X11(Scene):
    def construct(self):
        y = 0
        objs = []
        for name in X11.COLOR.keys():
            obj = VGroup()
            obj += Text(name).scale(0.5).move_to(3.5*LEFT,LEFT)
            obj += Square(side_length=0.45).set_fill(X11.COLOR[name], opacity = 1).move_to(4.5*LEFT)
            objs.append(obj)

        title = Text("{} X11 colors for Manim".format(len(objs)+1))
        self.play(Write(title))
        self.wait(2)
        self.remove(title)    

        i = 0
        onscreen = VGroup()
        while True:
            if i > 20:
                self.remove(objs[i-20])
                onscreen -= objs[i-20]
            self.play(onscreen.animate.shift(0.5*UP),run_time=0.1,rate_func=rate_functions.linear) 
            if i<len(objs):
                self.add(objs[i].shift(4.5*DOWN))
                onscreen.add(objs[i])
            i += 1
            if i == (len(objs)+20):
                break


class demonstrate_NBS(Scene):
    def construct(self):
        y = 0
        objs = []
        for name in NBS.COLOR.keys():
            obj = VGroup()
            obj += Text(name).scale(0.5).move_to(3.5*LEFT,LEFT)
            obj += Square(side_length=0.45).set_fill(NBS.COLOR[name], opacity = 1).move_to(4.5*LEFT)
            objs.append(obj)

        title = Text("{} NBS colors for Manim".format(len(objs)+1))
        self.play(Write(title))
        self.wait(2)
        self.remove(title)    

        i = 0
        onscreen = VGroup()
        while True:
            if i > 20:
                self.remove(objs[i-20])
                onscreen -= objs[i-20]
            self.play(onscreen.animate.shift(0.5*UP),run_time=0.1,rate_func=rate_functions.linear) 
            if i<len(objs):
                self.add(objs[i].shift(4.5*DOWN))
                onscreen.add(objs[i])
            i += 1
            if i == (len(objs)+20):
                break

class demonstrate_NCS(Scene):
    def construct(self):
        y = 0
        objs = []
        for name in NCS.COLOR.keys():
            obj = VGroup()
            obj += Text(name).scale(0.5).move_to(3.5*LEFT,LEFT)
            obj += Square(side_length=0.45).set_fill(NCS.COLOR[name], opacity = 1).move_to(4.5*LEFT)
            objs.append(obj)

        title = Text("{} NCS colors for Manim".format(len(objs)+1))
        self.play(Write(title))
        self.wait(2)
        self.remove(title)    

        i = 0
        onscreen = VGroup()
        while True:
            if i > 20:
                self.remove(objs[i-20])
                onscreen -= objs[i-20]
            self.play(onscreen.animate.shift(0.5*UP),run_time=0.1,rate_func=rate_functions.linear) 
            if i<len(objs):
                self.add(objs[i].shift(4.5*DOWN))
                onscreen.add(objs[i])
            i += 1
            if i == (len(objs)+20):
                break

class demonstrate_XKCD(Scene):
    def construct(self):
        y = 0
        objs = []
        for name in XKCD.COLOR.keys():
            obj = VGroup()
            obj += Text(name).scale(0.5).move_to(3.5*LEFT,LEFT)
            obj += Square(side_length=0.45).set_fill(XKCD.COLOR[name], opacity = 1).move_to(4.5*LEFT)
            objs.append(obj)

        title = Text("{} XKCD colors for Manim".format(len(objs)+1))
        self.play(Write(title))
        self.wait(2)
        self.remove(title)    

        i = 0
        onscreen = VGroup()
        while True:
            if i > 20:
                self.remove(objs[i-20])
                onscreen -= objs[i-20]
            self.play(onscreen.animate.shift(0.5*UP),run_time=0.1,rate_func=rate_functions.linear) 
            if i<len(objs):
                self.add(objs[i].shift(4.5*DOWN))
                onscreen.add(objs[i])
            i += 1
            if i == (len(objs)+20):
                break

class demonstrate_RESENE(Scene):
    def construct(self):
        y = 0
        objs = []
        for name in RESENE.COLOR.keys():
            obj = VGroup()
            obj += Text(name).scale(0.5).move_to(3.5*LEFT,LEFT)
            obj += Square(side_length=0.45).set_fill(RESENE.COLOR[name], opacity = 1).move_to(4.5*LEFT)
            objs.append(obj)

        title = Text("{} RESENE colors for Manim".format(len(objs)+1))
        self.play(Write(title))
        self.wait(2)
        self.remove(title)    

        i = 0
        onscreen = VGroup()
        while True:
            if i > 20:
                self.remove(objs[i-20])
                onscreen -= objs[i-20]
            self.play(onscreen.animate.shift(0.5*UP),run_time=0.1,rate_func=rate_functions.linear) 
            if i<len(objs):
                self.add(objs[i].shift(4.5*DOWN))
                onscreen.add(objs[i])
            i += 1
            if i == (len(objs)+20):
                break


class demonstrate_RAL(Scene):
    def construct(self):
        y = 0
        objs = []
        for name in RAL.COLOR.keys():
            obj = VGroup()
            obj += Text(name).scale(0.5).move_to(3.5*LEFT,LEFT)
            obj += Square(side_length=0.45).set_fill(RAL.COLOR[name], opacity = 1).move_to(4.5*LEFT)
            objs.append(obj)

        title = Text("{} RAL colors for Manim".format(len(objs)+1))
        self.play(Write(title))
        self.wait(2)
        self.remove(title)    

        i = 0
        onscreen = VGroup()
        while True:
            if i > 20:
                self.remove(objs[i-20])
                onscreen -= objs[i-20]
            self.play(onscreen.animate.shift(0.5*UP),run_time=0.1,rate_func=rate_functions.linear) 
            if i<len(objs):
                self.add(objs[i].shift(4.5*DOWN))
                onscreen.add(objs[i])
            i += 1
            if i == (len(objs)+20):
                break

class demonstrate_FS595(Scene):
    def construct(self):
        y = 0
        objs = []
        for name in FS595.COLOR.keys():
            obj = VGroup()
            obj += Text(name).scale(0.5).move_to(3.5*LEFT,LEFT)
            obj += Square(side_length=0.45).set_fill(FS595.COLOR[name], opacity = 1).move_to(4.5*LEFT)
            objs.append(obj)

        title = Text("{} FS595 colors for Manim".format(len(objs)+1))
        self.play(Write(title))
        self.wait(2)
        self.remove(title)    

        i = 0
        onscreen = VGroup()
        while True:
            if i > 20:
                self.remove(objs[i-20])
                onscreen -= objs[i-20]
            self.play(onscreen.animate.shift(0.5*UP),run_time=0.1,rate_func=rate_functions.linear) 
            if i<len(objs):
                self.add(objs[i].shift(4.5*DOWN))
                onscreen.add(objs[i])
            i += 1
            if i == (len(objs)+20):
                break

class demonstrate_BS381(Scene):
    def construct(self):
        y = 0
        objs = []
        for name in BS381.COLOR.keys():
            obj = VGroup()
            obj += Text(name).scale(0.5).move_to(3.5*LEFT,LEFT)
            obj += Square(side_length=0.45).set_fill(BS381.COLOR[name], opacity = 1).move_to(4.5*LEFT)
            objs.append(obj)

        title = Text("{} BS381 colors for Manim".format(len(objs)+1))
        self.play(Write(title))
        self.wait(2)
        self.remove(title)    

        i = 0
        onscreen = VGroup()
        while True:
            if i > 20:
                self.remove(objs[i-20])
                onscreen -= objs[i-20]
            self.play(onscreen.animate.shift(0.5*UP),run_time=0.1,rate_func=rate_functions.linear) 
            if i<len(objs):
                self.add(objs[i].shift(4.5*DOWN))
                onscreen.add(objs[i])
            i += 1
            if i == (len(objs)+20):
                break

class demonstrate_BS4800(Scene):
    def construct(self):
        y = 0
        objs = []
        for name in BS4800.COLOR.keys():
            obj = VGroup()
            obj += Text(name).scale(0.5).move_to(3.5*LEFT,LEFT)
            obj += Square(side_length=0.45).set_fill(BS4800.COLOR[name], opacity = 1).move_to(4.5*LEFT)
            objs.append(obj)

        title = Text("{} BS4800 colors for Manim".format(len(objs)+1))
        self.play(Write(title))
        self.wait(2)
        self.remove(title)    

        i = 0
        onscreen = VGroup()
        while True:
            if i > 20:
                self.remove(objs[i-20])
                onscreen -= objs[i-20]
            self.play(onscreen.animate.shift(0.5*UP),run_time=0.1,rate_func=rate_functions.linear) 
            if i<len(objs):
                self.add(objs[i].shift(4.5*DOWN))
                onscreen.add(objs[i])
            i += 1
            if i == (len(objs)+20):
                break


class demonstrate_AS2700(Scene):
    def construct(self):
        y = 0
        objs = []
        for name in AS2700.COLOR.keys():
            obj = VGroup()
            obj += Text(name).scale(0.5).move_to(3.5*LEFT,LEFT)
            obj += Square(side_length=0.45).set_fill(AS2700.COLOR[name], opacity = 1).move_to(4.5*LEFT)
            objs.append(obj)

        title = Text("{} AS2700 colors for Manim".format(len(objs)+1))
        self.play(Write(title))
        self.wait(2)
        self.remove(title)    

        i = 0
        onscreen = VGroup()
        while True:
            if i > 20:
                self.remove(objs[i-20])
                onscreen -= objs[i-20]
            self.play(onscreen.animate.shift(0.5*UP),run_time=0.1,rate_func=rate_functions.linear) 
            if i<len(objs):
                self.add(objs[i].shift(4.5*DOWN))
                onscreen.add(objs[i])
            i += 1
            if i == (len(objs)+20):
                break


class demonstrate_CRAYOLA(Scene):
    def construct(self):
        y = 0
        objs = []
        for name in CRAYOLA.COLOR.keys():
            obj = VGroup()
            obj += Text(name).scale(0.5).move_to(3.5*LEFT,LEFT)
            obj += Square(side_length=0.45).set_fill(CRAYOLA.COLOR[name], opacity = 1).move_to(4.5*LEFT)
            objs.append(obj)

        title = Text("{} CRAYOLA colors for Manim".format(len(objs)+1))
        self.play(Write(title))
        self.wait(2)
        self.remove(title)    

        i = 0
        onscreen = VGroup()
        while True:
            if i > 20:
                self.remove(objs[i-20])
                onscreen -= objs[i-20]
            self.play(onscreen.animate.shift(0.5*UP),run_time=0.1,rate_func=rate_functions.linear) 
            if i<len(objs):
                self.add(objs[i].shift(4.5*DOWN))
                onscreen.add(objs[i])
            i += 1
            if i == (len(objs)+20):
                break







