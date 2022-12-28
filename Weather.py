import csv

date_index = 0
temp_index = 2
wind_index = 3

def csv_reader(file):
    nlst = []
    with open(file, 'r') as myfile:
        csv_reader = csv.reader(myfile)
        next(myfile)
        for row in csv_reader:
            nlst.append(row)
    return nlst

def client_input():
    return input('Welcome to the Fort Collins Weather Analyzer! \nPlease enter a filter:')

def average_temperature(weather, filter, n_index):
    lst = []
    for data in weather:
        if filter.lower() in data[date_index].lower():
            lst.append(data)
    total = 0
    for day in lst:
        total += float(day[n_index])
    return total / len(lst)

def maximum_temperature(weather, filter, n_index):
    lst = []
    for data in weather:
        if filter.lower() in data[date_index].lower():
            lst.append(data)
    max_temp = -99999
    for day in lst:
        if max_temp < float(day[n_index]):
            max_temp = float(day[n_index])
    return max_temp

def minimum_temperature(weather, filter, n_index):
    lst = []
    for data in weather:
        if filter.lower() in data[date_index].lower():
            lst.append(data)
    min_temp = 99999
    for day in lst:
        if min_temp > float(day[n_index]):
            min_temp = float(day[n_index])
    return min_temp

def run():
    weather = csv_reader('Temperatures.csv')
    input = client_input()
    avg_temp = "{:.2f}".format(average_temperature(weather, input, temp_index))
    max_temp = "{:.2f}".format(maximum_temperature(weather, input, temp_index))
    min_temp = "{:.2f}".format(minimum_temperature(weather, input, temp_index))
    print("\nAverage Temperature for " + str(input) + ":", avg_temp)
    print("Maximum Temperature for " + str(input) + ":", max_temp)
    print("Minimum Temperature for " + str(input) + ":", min_temp)
    avg_wind = "{:.2f}".format(average_temperature(weather, input, wind_index))
    max_wind = "{:.2f}".format(maximum_temperature(weather, input, wind_index))
    min_wind = "{:.2f}".format(minimum_temperature(weather, input, wind_index))
    print("\nAverage Wind Speed for " + str(input) + ":", avg_wind)
    print("Maximum Wind Speed for " + str(input) + ":", max_wind)
    print("Minimum Wind Speed for " + str(input) + ":", min_wind)

if __name__ == '__main__':
    run()
