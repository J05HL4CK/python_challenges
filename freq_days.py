import datetime

def freq_days(year):
    week_days = ('Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun')
    freq = set([datetime.date(year, 1, 1).weekday() ,datetime.date(year, 12, 31).weekday()])
    day_freq = sorted(list(freq))
    res = [week_days[i] for i in day_freq]
    return(res)


