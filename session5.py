import time
import math

def time_it(fn, *args, repetitons= 1, **kwargs): 
    start = time.perf_counter()
    for i in range(repetitons):
        fn(*args, **kwargs)
    end = time.perf_counter()
    total_time = end - start
    avg_time = total_time/repetitons
    return avg_time

def squared_power_list(num, start=0, end=5):
    if end < start:
        raise ValueError('end should be greater than start')
    squared_power_list = []
    while start<=end:
        squared_power_list.append(math.pow(num,start))
        start = start+1
    print('squared power list is:', squared_power_list)
    return squared_power_list

def polygon_area(side_len, sides = 3):
    if sides < 3 or sides > 6:
        raise ValueError('sides of polygon can only vary from 3 to 6')
    if sides == 3:
        area = (math.pow(3, 0.5) * math.pow(side_len, 2))/4
    elif sides == 4:
        area = math.pow(side_len, 2)
    else:
        area = (sides * side_len ** 2) / (4 * math.tan(math.pi / sides))
    print('area of polygon is:', area)
    return area

def temp_converter(base_temp, temp_given_in = 'f'):
    if temp_given_in != 'f' and temp_given_in != 'c':
        raise ValueError('temperature can only be given as c or f')
    if temp_given_in == 'f':
        temp = (base_temp - 32)/(1.8)
    else:
        temp = (base_temp * 1.8) + 32
    print('temperature after conversion is:', temp)
    return temp

def speed_converter(speed, dist='km', time='min'):
    if speed < 0:
        raise ValueError('speed cannot be negative')
    if dist != 'km' and dist != 'm' and dist != 'ft' and dist != 'yrd':
        raise ValueError('distance can only be given in km/m/ft/yrd')
    if time != 'ms' and time != 's' and time != 'min' and time != 'hr' and time != 'day':
        raise ValueError('time can only be given in ms/s/min/hr/day')

    if dist == 'm':
        speed = speed * 1000
    elif dist == 'ft':
        speed = speed * 3280.839895
    elif dist == 'yrd':
        speed = speed * 1093.6132983377
    else:
        pass

    if time == 'ms':
        speed = speed / 3600000
    elif time == 's':
        speed = speed / 3600
    elif time == 'min':
        speed = speed / 60
    elif time == 'day':
        speed = speed * 24
    else:
        pass

    print('speed after conversion is:', speed)
    return speed