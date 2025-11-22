
def time_string(hours, minutes, time_format):
    hours = int(hours)
    minutes = int(minutes)
    time = 0
    if time_format == '24':
        if minutes < 10:
            minutes = f'0{minutes}'
        if hours < 10:
            hours = f'0{hours}'
        time = f'{hours}:{minutes}'
        return time
    elif time_format == '12':
        if minutes < 10:
            minutes = f'0{minutes}'
        if hours > 12:
            hours -= 12
            time = f'{hours}:{minutes}pm'
            return time
        if hours == 12:
            time = f'{hours}:{minutes}pm'
            return time
        if hours == 0:
            hours = 12
            time = f'{hours}:{minutes}am'
            return time
        else:
            time = f'{hours}:{minutes}am'
            return time
print(time_string(19, 2, '12'))
print(time_string(15, 38, '24'))
print(time_string(11, 15, '12'))