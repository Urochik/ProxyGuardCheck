# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import requests


while True:
    try:
        print(f'Proxy/AntiDDOS cheker v0.1')
        input_url = input('input url to check proxy or cdn: ')
        fix_url = ''
        if input_url.__contains__('https://'): #check to https for request send
            fix_url =  input_url.strip()
            print(fix_url)
        else:
            fix_url = 'https://' + input_url.strip()
            print(fix_url)
        r = requests.get(fix_url)
        headers = r.headers

        if headers.get('server') == 'cloudflare': # cloudflare check
            print(f'server: cloudflare: \n cf-ray: {headers.get("CF-Ray")} \n CF-Cache-Status: {headers.get("CF-Cache-Status")}')
        elif headers.__contains__('X-Akam-SW-Version'):
            print(f'server: Akamai: \n X-Akam-SW-Version - {headers.get("X-Akam-SW-Version")} \n Akamai-GRN - {headers.get('Akamai-GRN')}  ')
        elif headers.get('X-Cache') == 'Miss from cloudfront' or headers.get('X-Cache') == 'Hit from cloudfront':
            print(f'server: cloudfront: \n via: {headers.get("Via")} \n X-Amz-Cf-Pop: {headers.get("X-Amz-Cf-Pop")} \n X-Amz-Cf-Id: {headers.get("X-Amz-Cf-Id")}')
        elif headers.get('Server') == 'rdwr':
            cookie = headers.get('Set-Cookie')
            print(f'server: {headers.get("Server")}: \n Cookie: {cookie}')
        elif headers.__contains__('x-vercel-cache') or headers.__contains__('x-vercel-id') or headers.get('Server')== 'Vercel':
            print(f'server: vercel: \n x-vercel-id: {headers.get("x-vercel-id")} \n x-vercel-cache: {headers.get("x-vercel-cache")} \n Etag: {headers.get("Etag")} \n Last-Modified: {headers.get("Last-Modified")}')
        elif headers.get('Server') == 'ddos-guard':
            print(f'server: {headers.get('Server')} \n Cookie: {headers.get("Set-Cookie")}')

        print(headers)
    except KeyError:
        print('Please enter a normal string')







# See PyCharm help at https://www.jetbrains.com/help/pycharm/
