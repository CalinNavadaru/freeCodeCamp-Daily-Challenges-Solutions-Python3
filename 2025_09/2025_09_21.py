def number_of_videos(video_size, video_unit, drive_size, drive_unit):
    if video_unit == "KB":
        video_size *= 1000
    elif video_unit == "MB":
        video_size *= 1_000_000
    elif video_unit == "GB":
        video_size *= 1_000_000_000
    else:
        return "Invalid video unit"

    if drive_unit == "GB":
        drive_size *= 1_000_000_000
    elif drive_unit == "TB":
        drive_size *= 1_000_000_000_000
    else:
        return "Invalid drive unit"    


    return drive_size // video_size
