def to_seconds(time):
    time = str(time)
    h, m, s = map(int, time.split(':'))
    return h*3600 + m*60 + s