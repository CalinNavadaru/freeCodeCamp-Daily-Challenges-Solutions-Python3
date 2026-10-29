def get_element_size(window_size: str, element_vw: str, element_vh: str) -> str:
    window_width, window_height = map(int, window_size.split("x"))
    element_vh = int(element_vh[:-2])
    element_vw = int(element_vw[:-2])

    return str(int(element_vw / 100 * window_width)) + " x " + str(int(element_vh / 100 * window_height))