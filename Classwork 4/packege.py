def transfer_to_rgb(cyan, magenta, yellow, black):
    white = 1 - black
    red = 255 * white * (1 - cyan)
    green = 255 * white * (1 - magenta)
    blue = 255 * white * (1 - yellow)
    return red, green, blue
