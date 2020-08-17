import pytest
import random
import string
import session5
import os
import inspect
import re
import math
import time
import timeit

README_CONTENT_CHECK_FOR = [
    'time_it',
    '*args',
    'repetitons',
    '**kwargs',
    'average',
    'squared_power_list',
    'list',
    'start',
    'end',
    'polygon_area',
    'sides',
    'temp_converter',
    'temp_given_in',
    'speed_converter',
    'dist',
    'time'
]

CHECK_FOR_FUNCT_IMPL = [
    'time_it',
    '*args',
    'repetitons',
    '**kwargs',
    'squared_power_list',
    'start',
    'end',
    'polygon_area',
    'sides',
    'temp_converter',
    'temp_given_in',
    'speed_converter',
    'dist',
    'time'
]

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r", encoding="utf-8")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session5)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines" 

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session5, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_all_functions_implemented():
    code_lines = inspect.getsource(session5)
    FUNCS_IMPL = True
    for c in CHECK_FOR_FUNCT_IMPL:
        if c not in code_lines:
            FUNCS_IMPL = False
            pass
    assert FUNCS_IMPL == True, 'You forgot to implement all functions with appropriate arguments! Try again!'

def test_math_used():
    code_lines = inspect.getsource(session5)
    assert 'math' in code_lines, 'You have not used math module!'
    assert 'import' in code_lines, 'You have not imported anything!'

def test_time_it_function_print():
    code = '''print(1, 2, 3, sep='-', end=" ***\\n")'''
    time_it_avg = timeit.timeit(stmt=code, number=100)/100
    avg_time = session5.time_it(print, 1, 2, 3, sep='-', end=' ***\n', repetitons=100)
    print ('avg time is {} and timeit time is {}'.format(avg_time, time_it_avg))
    assert math.isclose(time_it_avg, avg_time, abs_tol=0.001) and type(avg_time) == float

def test_timeit_function_squared_power_list():
    import_module = "import math"
    code = '''
def squared_power_list():
    squared_power_list = []
    start = 0
    end = 5
    while start<=end:
        squared_power_list.append(math.pow(2,start))
        start = start+1
    print('squared power list is:', squared_power_list)
    return squared_power_list
'''
    time_it_avg = timeit.timeit(stmt = code, setup = import_module, number=5)/5
    avg_time = session5.time_it(session5.squared_power_list, 2, start=0, end=5, repetitons=5)
    assert math.isclose(time_it_avg, avg_time, abs_tol=0.001) and type(avg_time) == float

def test_timeit_polygon_area():
    import_module = "import math"
    code = '''
def polygon_area():
    side_len = 15
    sides = 3
    if sides < 3 or sides > 6:
        raise ValueError('sides of polygon can only vary from 3 to 6')
    if sides == 3:
        area = (math.pow(3, 0.5) * math.pow(side_len, 2))/4
    elif sides == 4:
        area = math.pow(side_len, 2)
    else:
        area = round((sides * side_len ** 2) / (4 * math.tan(math.pi / sides)), 5)
    print('area of polygon is:', area)
    return area
'''
    time_it_avg = timeit.timeit(stmt = code, setup = import_module, number=10)/10
    avg_time = session5.time_it(session5.polygon_area, 15, sides = 3, repetitons=10)
    assert math.isclose(time_it_avg, avg_time, abs_tol=0.001) and type(avg_time) == float

def test_timeit_function_temp_converter():
    import_module = "import math"
    code = '''
def temp_converter():
    base_temp = 100
    temp_given_in = 'f'
    if temp_given_in != 'f' and temp_given_in != 'c':
        raise ValueError('temperature can only be given as c or f')
    if temp_given_in == 'f':
        temp = (base_temp - 32)/(1.8)
    else:
        temp = (base_temp * 1.8) + 32
    print('temperature after conversion is:', temp)
    return temp
'''
    time_it_avg = timeit.timeit(stmt = code, setup = import_module, number=100)/100
    avg_time = session5.time_it(session5.temp_converter, 100, temp_given_in = 'f', repetitons=100)
    assert math.isclose(time_it_avg, avg_time, abs_tol=0.001) and type(avg_time) == float

def test_timeit_function_speed_converter():
    import_module = "import math"
    code = '''
def speed_converter():
    speed = 100
    dist='km'
    time='min'
    if speed < 0:
        raise ValueError('speed cannot be negative')
    if dist != 'km' and dist != 'm' and dist != 'ft' and dist != 'yrd':
        raise ValueError('distance can only be given in km/m/ft/yrd')
    if time != 'ms' and time != 's' and time != 'min' and time != 'hr' and time != 'day':
        raise ValueError('time can only be given in ms/s/m/hr/day')

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
'''
    time_it_avg = timeit.timeit(stmt = code, setup = import_module, number=200)/200
    avg_time = session5.time_it(session5.speed_converter,100, dist='km', time='min', repetitons=200)
    assert math.isclose(time_it_avg, avg_time, abs_tol=0.001) and type(avg_time) == float

def test_function_print():
    assert print(1, 2, 3, sep='-', end= ' ***\n') == print('1-2-3 ***')

def test_function_squared_power_list():
    values = (random.randint(-150, 150) for _ in range(random.randint(10, 50)))
    ranges = ((p, q) 
    for p in range(random.randint(-50, 50)) 
    for q in range(random.randint(50, 150)) 
    for _ in range(random.randint(20, 200)))
    for start, end in ranges:
        for n in values:
            assert [n ** i for i in range(start, end + 1)] == session5.squared_power_list(n, start=start, end=end)

def test_function_squared_power_list_error_case():
    with pytest.raises(ValueError):
        session5.squared_power_list(2, start=5, end=0)

def test_function_polygon_area():
    for _ in range(200):
        len = random.choice([11, 50, -10, 2, 0, 88])
        side = random.choice([3, 4, 5, 6])
    assert math.isclose((side * len ** 2) / (4 * math.tan(math.pi / side)), session5.polygon_area(len,sides=side))

def test_function_polygon_area_error_case():
    with pytest.raises(ValueError):
        session5.polygon_area(len,sides=2)
    with pytest.raises(ValueError):
        session5.polygon_area(len,sides=-1)
    with pytest.raises(ValueError):
        session5.polygon_area(len,sides=7)
    with pytest.raises(ValueError):
        session5.polygon_area(len,sides=50)

def test_function_temp_converter_celius_to_fahrenheit():
    celsius = random.uniform(-273.15, 1000)
    fahrenheit = (celsius * 1.8) + 32
    assert math.isclose(fahrenheit,session5.temp_converter(celsius, temp_given_in='c'))

def test_function_temp_converter_fahrenheit_to_celius():
    fahrenheit = random.uniform(-459.67, 1832.0)
    celsius = (fahrenheit - 32) / 1.8
    assert math.isclose(celsius,session5.temp_converter(fahrenheit, temp_given_in='f'))

def test_function_temp_converter_error_case():
    with pytest.raises(ValueError):
        session5.temp_converter(100, temp_given_in='h')

def test_function_speed_converter_kmph_to_kmpday():
    random_speed = random.randint(1,1000)
    speed_value = random_speed*24
    speed = session5.speed_converter(random_speed, dist='km', time='day')
    assert math.isclose(speed_value, speed)

def test_function_speed_converter_kmph_to_kmpmin():
    random_speed = random.randint(1,1000)
    speed_value = random_speed/60
    speed = session5.speed_converter(random_speed, dist='km', time='min')
    assert math.isclose(speed_value, speed)

def test_function_speed_converter_kmph_to_kmpsec():
    random_speed = random.randint(1,1000)
    speed_value = random_speed/3600
    speed = session5.speed_converter(random_speed, dist='km', time='s')
    assert math.isclose(speed_value, speed)

def test_function_speed_converter_kmph_to_kmpmillisec():
    random_speed = random.randint(1,1000)
    speed_value = random_speed/3600000
    speed = session5.speed_converter(random_speed, dist='km', time='ms')
    assert math.isclose(speed_value, speed)

def test_function_speed_converter_kmph_to_meterph():
    random_speed = random.randint(1,1000)
    speed_value = random_speed*1000
    speed = session5.speed_converter(random_speed, dist='m', time='hr')
    assert math.isclose(speed_value, speed)

def test_function_speed_converter_kmph_to_ftph():
    random_speed = random.randint(1,1000)
    speed_value = random_speed*3280.839895
    speed = session5.speed_converter(random_speed, dist='ft', time='hr')
    assert math.isclose(speed_value, speed)

def test_function_speed_converter_kmph_to_yrdph():
    random_speed = random.randint(1,1000)
    speed_value = random_speed*1093.6132983377
    speed = session5.speed_converter(random_speed, dist='yrd', time='hr')
    assert math.isclose(speed_value, speed)

def test_function_speed_converter_kmph_to_mpsec():
    random_speed = random.randint(1,1000)
    speed_value = random_speed/3.6
    speed = session5.speed_converter(random_speed, dist='m', time='s')
    assert math.isclose(speed_value, speed)

def test_function_speed_converter_kmph_to_mpmillisec():
    random_speed = random.randint(1,1000)
    speed_value = random_speed/3600
    speed = session5.speed_converter(random_speed, dist='m', time='ms')
    assert math.isclose(speed_value, speed)

def test_function_speed_converter_kmph_to_mpmin():
    random_speed = random.randint(1,1000)
    speed_value = random_speed*16.6666666667
    speed = session5.speed_converter(random_speed, dist='m', time='min')
    assert math.isclose(speed_value, speed)

def test_function_speed_converter_kmph_to_mpday():
    random_speed = random.randint(1,1000)
    speed_value = random_speed*24000
    speed = session5.speed_converter(random_speed, dist='m', time='day')
    assert math.isclose(speed_value, speed)

def test_function_speed_converter_kmph_to_ftpsec():
    random_speed = random.randint(1,1000)
    speed_value = random_speed/1.09728
    speed = session5.speed_converter(random_speed, dist='ft', time='s')
    assert math.isclose(speed_value, speed)

def test_function_speed_converter_kmph_to_ftpmillisec():
    random_speed = random.randint(1,1000)
    speed_value = random_speed/1097.28
    speed = session5.speed_converter(random_speed, dist='ft', time='ms')
    assert math.isclose(speed_value, speed)

def test_function_speed_converter_kmph_to_ftpmin():
    random_speed = random.randint(1,1000)
    speed_value = random_speed/0.018288
    speed = session5.speed_converter(random_speed, dist='ft', time='min')
    assert math.isclose(speed_value, speed, abs_tol=0.001)

def test_function_speed_converter_kmph_to_ftpday():
    random_speed = random.randint(1,1000)
    speed_value = random_speed/1.27e-5
    speed = session5.speed_converter(random_speed, dist='ft', time='day')
    assert math.isclose(speed_value, speed, abs_tol=0.001)

def test_function_speed_converter_kmph_to_yrdpsec():
    random_speed = random.randint(1,1000)
    speed_value = random_speed/3.29184
    speed = session5.speed_converter(random_speed, dist='yrd', time='s')
    assert math.isclose(speed_value, speed)

def test_function_speed_converter_kmph_to_yrdpmillisec():
    random_speed = random.randint(1,1000)
    speed_value = random_speed/3291.84
    speed = session5.speed_converter(random_speed, dist='yrd', time='ms')
    assert math.isclose(speed_value, speed)

def test_function_speed_converter_kmph_to_yrdpmin():
    random_speed = random.randint(1,1000)
    speed_value = random_speed/0.054864
    speed = session5.speed_converter(random_speed, dist='yrd', time='min')
    assert math.isclose(speed_value, speed, abs_tol=0.001)

def test_function_speed_converter_kmph_to_yrdpday():
    random_speed = random.randint(1,1000)
    speed_value = random_speed/3.81e-5
    speed = session5.speed_converter(random_speed, dist='yrd', time='day')
    assert math.isclose(speed_value, speed, abs_tol=0.001)

def test_function_speed_converter_error_case():
    random_speed = random.randint(1,1000)
    with pytest.raises(ValueError):
        session5.speed_converter(random_speed, dist='k', time='day')
    with pytest.raises(ValueError):
        session5.speed_converter(random_speed, dist='metere', time='day')
    with pytest.raises(ValueError):
        session5.speed_converter(random_speed, dist='foot', time='day')
    with pytest.raises(ValueError):
        session5.speed_converter(random_speed, dist='yard', time='day')
    with pytest.raises(ValueError):
        session5.speed_converter(random_speed, dist='yrd', time='d')
    with pytest.raises(ValueError):
        session5.speed_converter(random_speed, dist='yrd', time='hour')
    with pytest.raises(ValueError):
        session5.speed_converter(random_speed, dist='yrd', time='sec')
    with pytest.raises(ValueError):
        session5.speed_converter(random_speed, dist='yrd', time='millisec')
    with pytest.raises(ValueError):
        session5.speed_converter(random_speed, dist='yrd', time='minute')