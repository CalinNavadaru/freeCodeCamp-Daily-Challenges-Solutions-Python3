def image_search(images: list[str], term: str) -> list[str]:
    r = []
    for image in images:
        if term.lower() in image.lower():
            r.append(image)
    return r