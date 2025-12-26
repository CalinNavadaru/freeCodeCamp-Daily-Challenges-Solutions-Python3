import collections
import math

LATITUDE_DAYLIGHT_SAVINGS = collections.OrderedDict(
    {
        -90: 24,
        -75: 23,
        -60: 21,
        -45: 15,
        -30: 13,
        -15: 12,
        0: 12,
        15: 11,
        30: 10,
        45: 9,
        60: 6,
        75: 2,
        90: 0
    }
)


def daylight_hours(latitude: int) -> int:
    if latitude in LATITUDE_DAYLIGHT_SAVINGS:
        return LATITUDE_DAYLIGHT_SAVINGS[latitude]
    dist = math.inf
    result = None
    for l in LATITUDE_DAYLIGHT_SAVINGS:
        d = abs(latitude - l)
        if 0 <= d < dist:
            dist = d
            result = l
        else:
            break
    return LATITUDE_DAYLIGHT_SAVINGS[result]
