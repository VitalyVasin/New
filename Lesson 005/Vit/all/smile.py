def smile (x1, y1, color1):
    import simple_draw as sd

    sd.resolution = (1600, 900)

    point1 = sd.get_point(x1, y1)
    point2 = sd.get_point(x1+80, y1)
    sd.line(point1, point2, color=color1, width=4)
    point3 = sd.get_point(x1-10, y1+10)
    point4 = sd.get_point(x1, y1)
    sd.line(point3, point4, color=color1, width=4)
    point5 = sd.get_point(x1+90, y1+10)
    point6 = sd.get_point(x1+80, y1)
    sd.line(point5, point6, color=color1, width=4)
    point7 = sd.get_point(x1+40, y1+50)
    sd.circle(point7, radius=100, color=color1, width=4)
    point8 = sd.get_point(x1, y1+80)
    sd.circle(point8, radius=20, color=color1, width=4)
    point9 = sd.get_point(x1+80, y1+80)
    sd.circle(point9, radius=20, color=color1, width=4)

    return