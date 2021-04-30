def tree(point, angle, length1, length2, delta1, delta2):

    import simple_draw as sd

    sd.resolution = (1600, 900)

    if length1 < 10 and length2 < 10:
        return
    v2_1 = sd.get_vector(start_point=point, angle=angle, length=length1, width=1)
    v2_1.draw()
    delta1 = sd.random_number(a=30, b=40)
    next_point1 = v2_1.end_point
    next_angle1 = angle - delta1
    k1 = (sd.random_number(a=80, b=120)) * (0.01)
    next_length1 = length1 * .75 * k1
    v2_2 = sd.get_vector(start_point=point, angle=angle, length=length2, width=1)
    v2_2.draw()
    delta2 = sd.random_number(a=30, b=40)
    next_point2 = v2_2.end_point
    next_angle2 = angle + delta2
    k2 = (sd.random_number(a=80, b=120)) * (0.01)
    next_length2 = length2 * .75 * k2
    tree(point=next_point1, angle=next_angle1, length1=next_length1, length2=next_length2, delta1=delta1, delta2=delta2)
    tree(point=next_point2, angle=next_angle2, length1=next_length1, length2=next_length2, delta1=delta1, delta2=delta2)