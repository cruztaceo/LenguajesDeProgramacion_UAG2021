# https://openflights.org/data.html

import pandas as pd
import geopy.distance as geopy

fname = input("Enter file name: ")
if len(fname) < 1: fname = "Aeropuertos2.txt"
try:
    print('Reading ' + fname + '...')
    data_frame = pd.read_csv(fname, encoding='cp1252')
except Exception as inst:
    print('File not found')

    print(type(inst))  # the exception instance
    print(inst.args)  # arguments stored in .args
    print(inst)  # __str__ allows args to be printed directly,
    # but may be overridden in exception subclasses
    x, y = inst.args  # unpack args
    print('x =', x)
    print('y =', y)
    quit()

while True:
    try:
        print('\n\rChoose an option:')
        print('1. Quantity of airports by country.')
        print('2. Quantity of airports by hemisphere.')
        print('3. Distance between airports.')
        print('4. Quantity of airports by continent or ocean.')
        print('5. Quit')
        menu_selection = int(input('Option: '))
        if menu_selection == 1:
            country = input('\n\rInput country: ')
            result = data_frame.loc[data_frame['country'] == country]
            print('Result:' + str(result.shape[0]))
            continue
        elif menu_selection == 2:
            hemisphere = input('\n\rInput hemisphere (North/South): ').upper()
            result = None
            if hemisphere == 'NORTH':
                result = data_frame.loc[data_frame['latitude_deg'] > 0]
            elif hemisphere == 'SOUTH':
                result = data_frame.loc[data_frame['latitude_deg'] < 0]
            else:
                print('Invalid hemisphere')
                continue
            print('Result:' + str(result.shape[0]))
            continue
        elif menu_selection == 3:
            try:
                iata_airport_A = input('Please input IATA for Airport A: ')
                df_coordinates_A = data_frame.loc[data_frame['IATA'] == iata_airport_A.upper(), ['latitude_deg', 'longitude_deg']]
                coordinates_A = list(zip(df_coordinates_A.latitude_deg, df_coordinates_A.longitude_deg))[0]
                iata_airport_B = input('Please input IATA for Airport B: ')
                df_coordinates_B = data_frame.loc[data_frame['IATA'] == iata_airport_B.upper(), ['latitude_deg', 'longitude_deg']]
                coordinates_B = list(zip(df_coordinates_B.latitude_deg, df_coordinates_B.longitude_deg))[0]
                distance = geopy.distance(coordinates_A, coordinates_B).km
                print('Distance in km: ' + str(distance))
            except IndexError:
                print('\n\rInvalid IATA code')
                continue
        elif menu_selection == 4:
            continent = input('\n\rInput continent or ocean (Africa, America, Antarctica, Arctic, Asia, Atlantic, '
                              'Australia, Europe, Indian, and Pacific): ')
            result = data_frame.loc[data_frame['db_timezone'].str.startswith(continent)]
            print('Result:' + str(result.shape[0]))
        else:
            print("\n\rThanks for playing")
            break
    except ValueError:
        print('Invalid Value')
        continue
