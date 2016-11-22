#!/usr/bin/env python

#   Gimp-Python - allows the writing of Gimp plugins in Python.
#   Copyright (C) 1997  James Henstridge <james@daa.com.au>
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

from gimpfu import *
import time
import turtle

gettext.install("gimp20-python", gimp.locale_directory, unicode=True)


def koch_1 (img, drw, width, height, order):



    firstPoint = [x0, y0, x1, y1]
    firstPointAngle = [x0, y0, x1, y1, 0]

    nextPoints = [firstPointAngle]

    pointsArray = []

    if order == 0:
         pdb.gimp_pencil(drw, len(firstPoint), firstPoint)
    else:
        for v in range (1, int(order)+1):
            pointsArray = []
            for point in nextPoints:
                x0 = point[0]
                y0 = point[1]
                if v == order:
                    for i in range(0,4):    
                        x1 = x0 + math.cos(angles[i] + point[4])*width/(math.pow(3,v))
                        y1 = y0 - math.sin(angles[i] + point[4])*width/(math.pow(3,v))
                        newPoint = [x0, y0, x1, y1]
                        x0 = x1
                        y0 = y1
                        pdb.gimp_pencil(drw, len(newPoint), newPoint)
                else:
                    for i in range(0,4):    
                        x1 = x0 + math.cos(angles[i] + point[4])*width/(math.pow(3,v))
                        y1 = y0 - math.sin(angles[i] + point[4])*width/(math.pow(3,v))
                        newPoint = [x0, y0, x1, y1, angles[i] + point[4]]
                        pointsArray.append(newPoint)
                        x0 = x1
                        y0 = y1
            nextPoints = pointsArray


def koch(order, size):

    img = gimp.Image(500, 500, RGB)
    pdb.gimp_context_push()


    layer = gimp.Layer(img, "Test", 200, 200, RGBA_IMAGE, 100, NORMAL_MODE)
    img.add_layer(layer, -1)
    pdb.gimp_image_set_active_layer(img, layer)
    
    
    drw = pdb.gimp_image_active_drawable(img)
    width = pdb.gimp_image_width(img)
    height = pdb.gimp_image_height(img)


    k = 2
    count = 1
    length = math.pow(3, k-1)


#    koch_0(img, drw, width, height, size)

    koch_1 (img, drw, width, height, order)

#    koch_3(img, drw, width, height, size)

#    koch_1 (img, drw, width, height, size)
    gimp.Display(img)
    gimp.displays_flush()

    pdb.gimp_context_pop()

register(
    "python-fu-foggify",
    "Koch Curve Fractal Image"
    "Create a new image with a Koch fractal on it.",
    "Alexandru Ichim",
    "Alexandru Ichim",
    "2016",
    "Koch (Py)",
    "", # Create a new image don't work on the existing one "RGB*, GRAY*"
    [
        (PF_SLIDER, "order", _("_Fractal Order"), 1, (0, 10, 1)),
        (PF_SLIDER, "size",    _("Op_acity"),    100, (0, 100, 1)),
    ],
    [],
    koch,
    menu="<Image>/File/Create/Fractals")
    

main()
