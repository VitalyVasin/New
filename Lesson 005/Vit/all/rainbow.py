

def rainbow():
    import simple_draw as sd

    sd.resolution = (1600, 900)

    rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN, sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
    r = 1000
    for xxx in rainbow_colors:
        point = sd.get_point(600, 0)
        sd.circle(point, radius=r, color=xxx, width=10)
        r -=11

    # sd.pause()











