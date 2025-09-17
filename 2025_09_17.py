import re


def generate_slug(url):
    url = url.strip().lower()
    url = re.sub(r"[^a-z0-9 ]", "", url)
    url = re.sub(r" +", "%20", url)

    return url


