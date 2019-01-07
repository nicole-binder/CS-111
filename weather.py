
'''
    Nicole Binder, 6 October 2018

    Adapted from code for the weather data assignment in CS 111 by Jeff Ondich

'''

import sys
import csv

def get_weather_data(csv_file_name):
    ''' Returns a list of lists representing the lines of the
        specified comma-separated values (CSV) file. See notes
        above for further information. '''
    weather_data = []
    with open(csv_file_name) as csv_file:
        reader = csv.reader(csv_file)
        header = next(reader)
        header_length = len(header)
        line_number = 2
        for row in reader:
            if len(row) == header_length:
                weather_data.append(row)
            else:
                print('[Line {0}] Row has the wrong number of fields'.format(line_number), file=sys.stderr)
    return weather_data

def get_highest_temperature(weather_data):
    max_temperature_ever = 0.0
    year = 1800
    for row in weather_data:
        max_temperature_string = row[3]
        if max_temperature_string != 'M':
            max_temperature = float(max_temperature_string)
            if max_temperature > max_temperature_ever:
                max_temperature_ever = max_temperature
                year = row[0]
    return max_temperature_ever, year

def get_lowest_temperature(weather_data):
    min_temperature_ever = 0.0
    year = 1800
    for row in weather_data:
        min_temperature_string = row[4]
        if min_temperature_string != 'M':
            min_temperature = float(min_temperature_string)
            if min_temperature < min_temperature_ever:
                min_temperature_ever = min_temperature
                year = row[0]
    return min_temperature_ever, year

def avg_high_temp(weather_data):
    sum_high_temp = 0
    y = 0
    for row in weather_data:
        temp_string = row[3]
        if temp_string != 'M':
            y = y + 1
            temp = float(temp_string)
            sum_high_temp = sum_high_temp + temp
    if y != 0:
        avg_high_temperature = sum_high_temp/y
    else:
        avg_high_temperature = 0
    return avg_high_temperature

def avg_low_temp(weather_data):
    sum_low_temp = 0
    y = 0
    for row in weather_data:
        temp_string = row[4]
        if temp_string != 'M':
            y = y + 1
            temp = float(temp_string)
            sum_low_temp = sum_low_temp + temp
    if y != 0:
        avg_low_temperature = sum_low_temp/y
    else:
        avg_low_temperature = 0
    return avg_low_temperature

def get_high_snowfall(weather_data):
    high_snowfall_ever = -100.0 # We're assuming that the actual max is higher than this
    year = 1800
    day = 0
    month = 0
    for row in weather_data:
        high_snowfall_string = row[6]
        if high_snowfall_string != 'M' and high_snowfall_string != 'T':
            high_snowfall = float(high_snowfall_string)
            if high_snowfall > high_snowfall_ever:
                high_snowfall_ever = high_snowfall
                year = row[0]
                day = row[2]
                month = row[1]
    return high_snowfall_ever, year, month, day

def total_snowfall(weather_data):
    total = 0
    for row in weather_data:
        if row[6] != 'M':
            if row[6] == 'T':
                snowfall = 0
                total = total + 0
            else:
                snowfall = float(row[6])
                total = total + snowfall
    return total

def get_high_rainfall(weather_data):
    high_rainfall_ever = -100.0 # We're assuming that the actual max is higher than this
    year = 1800
    day = 0
    month = 0
    for row in weather_data:
        high_rainfall_string = row[5]
        if high_rainfall_string != 'M' and high_rainfall_string != 'T':
            high_rainfall = float(high_rainfall_string)
            if high_rainfall > high_rainfall_ever:
                high_rainfall_ever = high_rainfall
                year = row[0]
                day = row[2]
                month = row[1]
    return high_rainfall_ever, year, month, day

def data_by_year(weather_data, year):
    #separates list into new lists with data from one year
    year_list = []
    for row in weather_data:
        row_int = int(row[0])
        if row_int == year:
            year_list.append(row)
    return year_list


def main():
    weather_data = get_weather_data('weather.csv')
    print('{0:8}{1:^9}{2:^11}{3:^12}{4:^11}{5:^17}'.format('Year', 'Avg High', 'Avg Low', 'Max Temp', 'Min Temp', 'Total Snowfall'))
    #prints table of indiv. year data
    for k in range(1871,2019):
        the_year = k
        years = data_by_year(weather_data, the_year)
        years_number = int(the_year)
        highest_year_temp, yearly = get_highest_temperature(years)
        lowest_year_temp, yearly1 = get_lowest_temperature(years)
        avg_high_year_temp = avg_high_temp(years)
        avg_low_year_temp = avg_low_temp(years)
        snowfall_year = total_snowfall(years)
        print('{0:<8}{1:^8.1f}{2:^13.1f}{3:^11.1f}{4:^11.1f}{5:^16.1f}'.format(years_number, highest_year_temp, lowest_year_temp, avg_high_year_temp, avg_low_year_temp, snowfall_year))


    #overall stats
    highest_temperature, year = get_highest_temperature(weather_data)
    lowest_temperature, year1 = get_lowest_temperature(weather_data)
    avg_high_temperature = avg_high_temp(weather_data)
    avg_low_temperature = avg_low_temp(weather_data)
    high_snowfall, year2, month, day = get_high_snowfall(weather_data)
    high_rainfall, year3, month1, day1 = get_high_rainfall(weather_data)

    print('The highest temperature ever: {0:.1f} ({1})'.format(highest_temperature, year))
    print('The lowest temperature ever: {0:.1f} ({1})'.format(lowest_temperature, year1))
    print('Average high temperature: {0:.1f} F'.format(avg_high_temperature))
    print('Average low temperature: {0:.1f} F'.format(avg_low_temperature))
    print('Highest snowfall in a day: {0:.1f} inches ({1}-{2}-{3})'.format(high_snowfall, year2, month, day))
    print('Highest precipitation in a day: {0:.1f} inches ({1}-{2}-{3})'.format(high_rainfall, year3, month1, day1))
main()
