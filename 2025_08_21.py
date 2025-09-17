def mile_pace(miles, duration):
    minutes, seconds = map(int, duration.split(":"))
    time_in_seconds = seconds + minutes * 60
    average_time_mile = time_in_seconds // miles
    average_time_mile_minutes = average_time_mile // 60
    average_time_mile_seconds = average_time_mile - average_time_mile_minutes * 60
    return "{:0>2}".format(int(average_time_mile_minutes)) + ":" + "{:0>2}".format(int(average_time_mile_seconds))

