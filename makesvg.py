#!/usr/bin/env python3
import re
from math import sin, cos, pi

# usage (from build dir): python makesvg.py
# (no args needed)

bounds = None
def update_bounds(x, y):
    global bounds
    if bounds is None:
        bounds = [x,y,x,y]
    else:
        if bounds[0] > x:
            bounds[0] = x
        if bounds[1] > y:
            bounds[1] = y
        if bounds[2] < x:
            bounds[2] = x
        if bounds[3] < y:
            bounds[3] = y

def get_steps():
    re_pendown = re.compile(r"^PENDOWN$", re.IGNORECASE)
    re_penup = re.compile(r"^PENUP$", re.IGNORECASE)
    re_setxy = re.compile(r"^SETXY\s+(-?\d+)\s+(-?\d+)$", re.IGNORECASE)
    re_cubic = re.compile(r"^CUBIC\s+(-?\d+)\s+(-?\d+)\s+(-?\d+)\s+(-?\d+)\s+(-?\d+)\s+(-?\d+)$", re.IGNORECASE)
    re_setheading = re.compile(r"^SETHEADING\s+(-?\d+)$", re.IGNORECASE)
    re_forward = re.compile(r"^FORWARD\s+(-?\d+)$", re.IGNORECASE)
    re_end = re.compile(r"^END$", re.IGNORECASE)

    pendown = True
    heading = 0
    pos = 0, 0
    with open("xkcd.lgo") as fp:
        # Skip to the actual drawing commands
        for line in fp:
            if line.strip().upper().startswith("WINDOW"):
                break

        # read out the commands
        for line in fp:
            # skip comments
            try:
                ix = line.index(';')
            except ValueError:
                pass
            else:
                line = line[:ix]
            line = line.strip()
            if not line:
                continue

            if re_pendown.match(line):
                pendown = True
            elif re_penup.match(line):
                pendown = False
            elif match := re_setxy.match(line):
                x, y = map(int, match.groups())
                if pendown:
                    yield f"L {x},{-y}"
                else:
                    yield f"M {x},{-y}"
                pos = x, y
                update_bounds(x, y)
            elif match := re_cubic.match(line):
                x1, y1, x2, y2, ex, ey = map(int, match.groups())
                if pendown:
                    yield f"C {x1},{-y1},{x2},{-y2},{ex},{-ey}"
                else:
                    yield f"M {ex},{-ey}"
                pos = ex, ey
                update_bounds(x1, y1)
                update_bounds(x2, y2)
                update_bounds(ex, ey)
            elif match := re_setheading.match(line):
                heading, = map(int, match.groups())
                heading = heading * pi / 180
            elif match := re_forward.match(line):
                dist, = map(int, match.groups())
                dx = round(dist * sin(heading))
                dy = round(dist * cos(heading))
                if pendown:
                    yield f"l {dx},{-dy}"
                else:
                    yield f"m {dx},{-dy}"
                pos = pos[0] + dx, pos[1] + dy
                update_bounds(*pos)
            elif re_end.match(line):
                break
            else:
                raise ValueError(f"Unrecognised line: {line!r}")

def write_svg():
    steps = list(get_steps())
    xmin, ymin, xmax, ymax = bounds

    with open("xkcd2601.svg", "w", encoding="utf-8") as fp:
        print('<?xml version="1.0" encoding="UTF-8" standalone="no"?>', file=fp)
        print(f'<svg xmlns="http://www.w3.org/2000/svg" width="{xmax - xmin}mm" height="{ymax - ymin}mm" viewBox="{xmin} {-ymax} {xmax-xmin} {ymax-ymin}">', file=fp)
        print(f'\t<rect x="{xmin}" y="{-ymax}" width="{xmax - xmin}" height="{ymax-ymin}" style="fill: white" />', file=fp)
        print('\t<g>', file=fp)
        print('\t\t<path style="stroke: black; stroke-width: 1px; fill: none;" d="', file=fp)
        for step in steps:
            print(f'\t\t\t{step}', file=fp)
        print('\t\t" />', file=fp)
        print('\t</g>', file=fp)
        print('</svg>', file=fp)

if __name__ == "__main__":
    write_svg()
