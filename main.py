# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import requests


while True:
    try:
        print(f'Proxy/AntiDDOS cheker v0.1')
        input_url = input('input url to check proxy or cdn')
        fix_url = ''
        if input_url.__contains__('https://'): #check to https for request send
            fix_url =  input_url
            print(fix_url)
        else:
            fix_url = 'https://' + input_url
            print(fix_url)
        r = requests.get(fix_url)
       # headers = r.headers
    #    print(headers)
    except KeyError:
        print('Please enter a number')







# See PyCharm help at https://www.jetbrains.com/help/pycharm/
