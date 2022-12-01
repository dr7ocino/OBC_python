import time

minutes=time.strftime('%M')
hours=time.strftime('%H')

def selector(hours,minutes):
    if int(hours) >= 19:
        return 'Hora de volver a casa, son las :{}:{}'.format(hours, minutes)
    else:
        h_f=18-int(hours)
        m_f=59-int(minutes)
        return 'faltan ; {} hrs :{} m para las 19:00'.format(h_f, m_f)
print(selector(hours, minutes))