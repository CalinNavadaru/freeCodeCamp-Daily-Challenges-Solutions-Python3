def too_much_screen_time(hours):
    for hours_day in hours:
        if hours_day >= 10:
            return True

    for i in range(0, 5):
        avg_3_days = sum(hours[i:i + 3]) / 3
        if avg_3_days >= 8:
            return True

    avg_hours_week = sum(hours) / 7
    if avg_hours_week >= 6:
        return True

    return False
