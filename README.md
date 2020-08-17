# Assignment 5 Submission

This assignment is about timit fucntion which gives the average time taken to execute any function n number of times. Please find my understanding of this assignment as below:

### time_it
This function accepts any number of positional arguments in *args, repetitons is a mandatory names argument which specifies how many number of times a function should be executed, **kwargs accepts sets or dictionary value list which is passed onto their respective functions for named arguments. This function calculates average time taken by any function to execute given number of time and returns the output as float.

### print
This is python in-built function which prints the given text, pattern can also be specifie within this method using 'sep' and 'end'. 'sep' defines the character using which you want to separate the given list and 'end' specifies the character using which you want to end the line. 

### squared_power_list
This function accepts num as positional argument for which powers have to be calculated, 'start' and 'end' are named arguments which specify the start value for calculating power and end specifies ending value till where power needs to be calculated. They have default values as 0 and 5 respectively. It returns list of all powered values for that number.

### polygon_area
This function calculates area for given regular polygon, it only accepts side between 3 to 6 (included) and raises error for any other value. It accepts 'side_len' as positional argument which specifies the length for polygon and 'sides' as named argument which is number of sides in a polygon, 'sides' is defaulted to 3.

### temp_converter
This function converts given temperature from celsius to fahrenheit and vice versa. It accepts 'base_temp' as positional argument and 'temp_given_in' as named argument which is defaulted to 'f', 'temp_given_in' can only accept values as 'c' or 'f' and raises ValueError otherwise. If temperature is given as 'c', it converts it to fahrenheit and if it is given as 'f', it returns the temperature as celsius.

### speed_converter
This function converts given speed to any unit of measurement for distance and time. It accepts speed in kmph in positional argument 'speed' and has two named arguments as 'dist' abd 'time' which are defaulted to 'km' and 'min' respectively. The value for distance conversion only accepts 'km/m/ft/yrd' and time can only be given as 'ms/s/min/hr/day', for any other unit given, it raises ValueError.

## Test Cases Explanation

### test_readme_exists 
Checks if readme file exists.

### test_readme_contents
Checks if readme file has atleast 500 words.

### test_readme_proper_description
Checks if all functions implemented have been defined in readme

### test_readme_file_for_formatting
Checks if file is formatted properly using "#"

### test_indentations
Checks if four spaces multiple only have been used throughout the code

### test_function_name_had_cap_letter
Checks if no function name starts with capital letter

### test_all_functions_implemented
Checks if all functions have been implemented in code

### test_math_used
Checks if math module is used or not

### test_time_it_function_print
Checks if timeit function impl for calculating avg time for print function returns value close to python in-built timeit function.

### test_timeit_function_squared_power_list
Checks if timeit function impl for calculating avg time for squared_power_list function returns value close to python in-built timeit function.

### test_timeit_polygon_area
Checks if timeit function impl for calculating avg time for polygon_area function returns value close to python in-built timeit function.

### test_timeit_function_temp_converter
Checks if timeit function impl for calculating avg time for time_convertor function returns value close to python in-built timeit function.

### test_timeit_function_speed_converter
Checks if timeit function impl for calculating avg time for speed_convertor function returns value close to python in-built timeit function.

### test_function_print
Checks if print functions prints in expected format

### test_function_squared_power_list
Checks if squared_power_list function works as expected for correct input values.

### test_function_squared_power_list_error_case
Checks if squared_power_list function raises error for wrong input, i.e end > start

### test_function_polygon_area
Checks if polygon_area function returns area as expected for correct input values.

### test_function_polygon_area_error_case
Checks if polygon_area function raises error for wrong input values for sides, i.e. not between 3 and 6.

### test_function_temp_converter_celius_to_fahrenheit
Checks if temp_convertor function converts given celsius temp to fahrenheit.

### test_function_temp_converter_fahrenheit_to_celius
Checks if temp_convertor function converts given fahrenheit temp to celsius.

### test_function_temp_converter_error_case
Checks if temp_convertor function raises error for wrong input, i.e. temp_given_in is not 'c' or 'f'.

### test_function_speed_converter_kmph_to_kmpday
Checks if given speed in kmph is converted correctly to km per day.

### test_function_speed_converter_kmph_to_kmpmin
Checks if given speed in kmph is converted correctly to km per minute.

### test_function_speed_converter_kmph_to_kmpsec
Checks if given speed in kmph is converted correctly to km per second.

### test_function_speed_converter_kmph_to_kmpmillisec
Checks if given speed in kmph is converted correctly to km per millisecond.

### test_function_speed_converter_kmph_to_meterph
Checks if given speed in kmph is converted correctly to metre per hour.

### test_function_speed_converter_kmph_to_ftph
Checks if given speed in kmph is converted correctly to ft per hour.

### test_function_speed_converter_kmph_to_yrdph
Checks if given speed in kmph is converted correctly to yard per hour.

### test_function_speed_converter_kmph_to_mpsec
Checks if given speed in kmph is converted correctly to metre per second.

### test_function_speed_converter_kmph_to_mpmillisec
Checks if given speed in kmph is converted correctly to metre per millisecond.

### test_function_speed_converter_kmph_to_mpmin
Checks if given speed in kmph is converted correctly to metre per minute.

### test_function_speed_converter_kmph_to_mpday
Checks if given speed in kmph is converted correctly to metre per day.

### test_function_speed_converter_kmph_to_ftpsec
Checks if given speed in kmph is converted correctly to ft per second.

### test_function_speed_converter_kmph_to_ftpmillisec
Checks if given speed in kmph is converted correctly to ft per millisecond.

### test_function_speed_converter_kmph_to_ftpmin
Checks if given speed in kmph is converted correctly to ft per minute.

### test_function_speed_converter_kmph_to_ftpday
Checks if given speed in kmph is converted correctly to ft per day.

### test_function_speed_converter_kmph_to_yrdpsec
Checks if given speed in kmph is converted correctly to yard per second.

### test_function_speed_converter_kmph_to_yrdpmillisec
Checks if given speed in kmph is converted correctly to yard per millisecond.

### test_function_speed_converter_kmph_to_yrdpmin
Checks if given speed in kmph is converted correctly to yard per minute.

### test_function_speed_converter_kmph_to_yrdpday
Checks if given speed in kmph is converted correctly to yard per day.

### test_function_speed_converter_error_case
Checks if given speed for conversion does not contain unexpected values for 'dist' and 'time' as units of measurements.