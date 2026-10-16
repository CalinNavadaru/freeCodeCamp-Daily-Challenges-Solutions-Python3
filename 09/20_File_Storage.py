def number_of_files(file_size, file_unit, drive_size_gb):
    if file_unit == "KB":
        file_size *= 1000
    elif file_unit == "MB":
        file_size *= 1_000_000
    
    drive_size_gb *= 1_000_000_000

    return drive_size_gb // file_size
