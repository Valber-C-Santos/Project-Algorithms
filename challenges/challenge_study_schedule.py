def study_schedule(presence_periods, target_time):
    if target_time is None:
        return None

    if not all(isinstance(period, tuple) and len(period) == 2 and 
               isinstance(period[0], int) and isinstance(period[1], int) 
               for period in presence_periods):
        return None

    students_count = 0
    
    for start, end in presence_periods:
        if start <= target_time <= end:
            students_count += 1

    return students_count
