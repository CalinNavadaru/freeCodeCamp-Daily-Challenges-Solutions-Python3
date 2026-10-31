def largest_number(s: str) -> int | float | None:
    import re

    m = re.findall(r"([+-]?\d+\.\d+|[+-]?\d+)", s)
    if m:
        m: list[str]
        max_v = float(m[0]) if "." in m[0] else int(m[0])
        for i in range(1, len(m)):
            v = m[i]
            if "." in v:
                val = float(v)
            else:
                val = int(v)
            if val > max_v:
                max_v = val
        return max_v
    return None
