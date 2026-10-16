def is_match(fingerprint_a: str, fingerprint_b: str) -> bool:
    if len(fingerprint_a) != len(fingerprint_b):
        return False
    diffs = 0
    for c_a, c_b in zip(fingerprint_a, fingerprint_b):
        if c_a != c_b:
            diffs += 1

    return diffs / len(fingerprint_a) * 100 <= 10
