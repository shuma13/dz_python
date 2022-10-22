from datetime import datetime as dt
from time import strftime, time

def temperature_logger(date):
    time = dt.now().strftime('%H:%M')
    with open('log.cvs','a') as file:
        file.write('{};temperature;{}\n'
                    .format(time, data))

def pressure_logger(date):
    time = dt.now().strftime('%H:%M')
    with open('log.cvs','a') as file:
        file.write('{};pressure;{}\n'
                    .format(time, data))

def wind_speed_logger(date):
    time = dt.now().strftime('%H:%M')
    with open('log.cvs','a') as file:
        file.write('{};wind_speed;{}\n'
                    .format(time, data))



