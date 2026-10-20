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
            print(f'server: cloudflare: \n cf-ray: {headers.get("CF-Ray")} \n CF-Cache-Status: {headers.get("CF-Cache-Status")} \n age: {headers.get("age")}')
        elif headers.__contains__('X-Akam-SW-Version'):
            print(f'server: Akamai: \n X-Akam-SW-Version - {headers.get("X-Akam-SW-Version")} \n Akamai-GRN - {headers.get('Akamai-GRN')} \n age: {headers.get("age")}  ')
        elif headers.get('X-Cache') == 'Miss from cloudfront' or headers.get('X-Cache') == 'Hit from cloudfront':
            print(f'server: cloudfront: \n via: {headers.get("Via")} \n X-Amz-Cf-Pop: {headers.get("X-Amz-Cf-Pop")} \n X-Amz-Cf-Id: {headers.get("X-Amz-Cf-Id")} \n age: {headers.get("age")}')
        elif headers.get('Server','').__contains__('rdwr'):
            cookie = headers.get('Set-Cookie')
            print(f'server: {headers.get("Server")}: \n Cookie: {cookie} \n age: {headers.get("age")}')
        elif headers.get('Server') == 'ddos-guard':
            print(f'server: {headers.get('Server')}: \n Cookie: {headers.get("Set-Cookie")} \n age: {headers.get("age")}')
        elif headers.get('Server') == 'Angie':
            print(f'server: {headers.get('Server' )}: \n Etag: {headers.get('Eta')} \n X-Cluster: {headers.get("X-Cluster")} \n X-Hit: {headers.get("X-Hit")}')

        elif headers.__contains__('x-vercel-cache') or headers.__contains__('x-vercel-id') or headers.get('Server')== 'Vercel':
            print(f'server: vercel: \n x-vercel-id: {headers.get("x-vercel-id")} \n x-vercel-cache: {headers.get("x-vercel-cache")} \n Etag: {headers.get("Etag")} \n Last-Modified: {headers.get("Last-Modified")} \n age: {headers.get("age")}')

        elif headers.get('Server','').__contains__('Caddy') or headers.get('Server','').__contains__('nginx'):
            print(f'server: {headers.get("Server")}: \n Cookie: {headers.get('Set-Cookie')} \n X-Node: {headers.get("X-Node")} \n X-Version: {headers.get('X-Version')} \n X-NGENIX-Cache: {headers.get('X-NGENIX-Cache')} \n age: {headers.get('age')} \n Alt-Svc{headers.get("Alt-Svc")} \n Etag: {headers.get("Etag")} \n Last-Modified: {headers.get("Last-Modified")} ')
        elif headers.get('Server','').__contains__('QRATOR'):
            print(f'server: {headers.get('Server')}: \n ETag: {headers.get('Etag')} \n Cookie: {headers.get('Set-Cookie')} \n age: {headers.get("age")} \n last-modifed: {headers.get('Last-Modified')} \n X-Powered-By: {headers.get('X-Powered-By')}')
        elif headers.__contains__('yandex'):
            print(f'server: yandex: \n _yasc: {headers.get('_yasc')} \n _ymab_param: {headers.get('_ymab_param')} \n XSRF-TOKEN: {headers.get('XSRF-TOKEN')} \n x-trace-id: {headers.get('x-trace-id')} \n ETag: {headers.get('Etag')} \n last-modified: {headers.get('last-modified')} ')
        elif headers.get('Server','').__contains__('Mitelis DDoS-Mitigation'):
            print(f'server: {headers.get('server')}: \n X-MITELIS-CACHE: {headers.get('X-MITELIS-CACHE')} \n x-powered-by: {headers.get('x-powered-by')} \n last-modified: {headers.get("last-modified")}')
        elif headers.get('server','').__contains__('Apache'):
            print(f'server: {headers.get('server')} \n Set-Cookie: {headers.get('Set-Cookie')} \n Via: {headers.get('Via')}')

        #print(headers.get('Server'))
       # print(headers)
    except KeyError:
        print('Please enter a normal string')







# See PyCharm help at https://www.jetbrains.com/help/pycharm/
