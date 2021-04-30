def wall():

    import simple_draw as sd

    sd.resolution = (1600, 900)

    for x in range(400, 701, 50):
        for y in range(0, 201, 40):
            left_bottom1 = sd.get_point(x, y)
            right_top1 = sd.get_point(x + 50, y + 20)
            sd.rectangle(left_bottom1, right_top1, color=sd.COLOR_BLACK, width=3)
            left_bottom2 = sd.get_point(x + 25, y + 20)
            right_top2 = sd.get_point(x + 75, y + 40)
            sd.rectangle(left_bottom2, right_top2, color=sd.COLOR_BLACK, width=3)

    sd.rectangle(sd.get_point(400, 0), sd.get_point(775, 240), color=sd.COLOR_BLACK, width=5)
    sd.line(start_point=sd.get_point(380,240), end_point=sd.get_point(587.5, 300), color=sd.COLOR_ORANGE, width=5)
    sd.line(start_point=sd.get_point(587.5, 300), end_point=sd.get_point(795, 240), color=sd.COLOR_ORANGE, width=5)
    sd.line(start_point=sd.get_point(380,240), end_point=sd.get_point(795, 240), color=sd.COLOR_ORANGE, width=5)
    # sd.pause()

# wall()

# for x in range(-250, 1251, 250):
#     for y in range(0, 601, 120):
#         left_bottom1 = sd.get_point(x, y)
#         right_top1 = sd.get_point(x + 250, y + 60)
#         sd.rectangle(left_bottom1, right_top1, color=sd.COLOR_BLACK, width=3)
#         left_bottom2 = sd.get_point(x + 125, y + 60)
#         right_top2 = sd.get_point(x + 375, y + 120)
#         sd.rectangle(left_bottom2, right_top2, color=sd.COLOR_BLACK, width=3)