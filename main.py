# This is a sample Python script.
from os import error

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import requests
import colorama
import os
import time

colorama.init()
def draw_watermark():
    print(
        "\033[0;94m▄▄▄▄\033[0;37m \033[0;94m▄▄▄▄\033[0;37m  \033[0;94m▄▄▄▄\033[0;37m         \033[0;94m▄▄\033[0;37m  \033[0;94m▄▄▄▄\033[0;37m \033[0;94m▄▄▄▄\033[0;37m \033[0;94m▄▄▄▄\033[0;37m  \033[0;94m▄▄\033[0;37m \033[0;94m▄▄\033[0;37m \033[0;94m▄▄▄▄\033[0;37m \033[0;94m▄▄▄▄\033[0;37m      \033[0;94m▄▄▄▄\033[0;37m \033[0;94m▄▄\033[0;37m \033[0;94m▄▄\033[0;37m \033[0;94m▄▄▄▄\033[0;37m \033[0;94m▄▄▄▄\033[0;37m \033[0;94m▄▄\033[0;37m \033[0;94m▄▄\033[0;37m \033[0m")
    time.sleep(0.1)
    print(
        "\033[0;94;44m██\033[0;94m▀█\033[0;37m \033[0;94m██▀██\033[0;37m \033[0;94m██▀██\033[0;37m        \033[0;94m██\033[0;37m \033[0;94m██▀██\033[0;37m \033[0;94;44m██\033[0;94m▀█\033[0;37m \033[0;94m██▀██\033[0;37m \033[0;94m██\033[0;37m \033[0;94m██\033[0;37m \033[0;94;44m██\033[0;94m▀█\033[0;37m \033[0;94m██▀██\033[0;37m     \033[0;94;44m██\033[0;94m▀█\033[0;37m \033[0;94m██\033[0;37m \033[0;94m██\033[0;37m \033[0;94;44m██\033[0;94m▀█\033[0;37m \033[0;94;44m██\033[0;94m▀█\033[0;37m \033[0;94m██\033[0;37m \033[0;94m██\033[0;37m \033[0m")
    time.sleep(0.1)
    print(
        "\033[0;94;44m▓▓\033[0;37m   \033[0;94;44m▓▓\033[0;37m \033[0;94;44m▓▓\033[0;37m \033[0;94;44m▓▓\033[0;37m \033[0;94;44m▓▓\033[0;37m       \033[0;94;44m▓▓\033[0;37m  \033[0;94;44m▓▓\033[0;37m \033[0;94;44m▓▓\033[0;37m \033[0;94;44m▓▓\033[0;37m   \033[0;94;44m▓▓\033[0;37m \033[0;94;44m▓▓\033[0;37m \033[0;94;44m▓▓\033[0;37m \033[0;94;44m▓▓\033[0;37m \033[0;94;44m▓▓\033[0;37m   \033[0;94;44m▓▓\033[0;37m \033[0;94;44m▓▓\033[0;37m     \033[0;94;44m▓▓\033[0;37m   \033[0;94;44m▓▓\033[0;37m \033[0;94;44m▓▓\033[0;37m \033[0;94;44m▓▓\033[0;37m   \033[0;94;44m▓▓\033[0;37m   \033[0;94;44m▓▓\033[0;37m \033[0;94;44m▓▓\033[0;37m \033[0m")
    time.sleep(0.1)
    print(
        "\033[0;94;44m▓▓\033[0;37m   \033[0;94;44m▓▓\033[0;37m \033[0;94;44m▓▓\033[0;37m \033[0;94;44m▓▓\033[0;37m \033[0;94;44m▓▓\033[0;37m      \033[0;94;44m▓▓\033[0;37m   \033[0;94;44m▓▓\033[0;37m \033[0;94;44m▓▓\033[0;37m \033[0;94;44m▓▓\033[0;37m   \033[0;94;44m▓▓\033[0;37m \033[0;94;44m▓▓\033[0;37m \033[0;94;44m▓▓\033[0;37m \033[0;94;44m▓▓\033[0;37m \033[0;94;44m▓▓\033[0;37m   \033[0;94;44m▓▓\033[0;37m \033[0;94;44m▓▓\033[0;37m     \033[0;94;44m▓▓\033[0;37m   \033[0;94;44m▓▓\033[0;37m \033[0;94;44m▓▓\033[0;37m \033[0;94;44m▓▓\033[0;37m   \033[0;94;44m▓▓\033[0;37m   \033[0;94;44m▓▓\033[0;37m \033[0;94;44m▓▓\033[0;37m \033[0m")
    time.sleep(0.1)
    print(
        "\033[0;94;44m▒▒\033[0;37m   \033[0;94;44m▒▒\033[0;37m \033[0;94;44m▒▒\033[0;37m \033[0;94;44m▒▒\033[0;37m \033[0;94;44m▒▒\033[0;37m     \033[0;94;44m▒▒\033[0;37m    \033[0;94;44m▒▒\033[0;37m    \033[0;94;44m▒▒\033[0;37m   \033[0;94;44m▒▒\033[0;37m \033[0;94;44m▒▒\033[0;37m \033[0;94;44m▒▒\033[0;37m \033[0;94;44m▒▒\033[0;37m \033[0;94;44m▒▒\033[0;37m   \033[0;94;44m▒▒\033[0;37m \033[0;94;44m▒▒\033[0;37m     \033[0;94;44m▒▒\033[0;37m   \033[0;94;44m▒▒\033[0;37m \033[0;94;44m▒▒\033[0;37m \033[0;94;44m▒▒\033[0;37m   \033[0;94;44m▒▒\033[0;37m   \033[0;94;44m▒▒\033[0;37m \033[0;94;44m▒▒\033[0;37m \033[0m")
    time.sleep(0.1)
    print(
        "\033[0;94;44m▒▒\033[0;37m   \033[0;94;44m▒▒\033[0;37m \033[0;94;44m▒▒\033[0;37m \033[0;94;44m▒▒\033[0;37m \033[0;94;44m▒▒\033[0;37m    \033[0;94;44m▒▒\033[0;37m     \033[0;34m▀\033[0;94;44m▒▒▒\033[0;34m▄\033[0;37m \033[0;94;44m▒▒▒\033[0;37m  \033[0;94;44m▒▒▒▒\033[0;37m  \033[0;94;44m▒▒\033[0;37m \033[0;94;44m▒▒\033[0;37m \033[0;94;44m▒▒▒\033[0;37m  \033[0;94;44m▒▒▒▒\033[0;37m      \033[0;94;44m▒▒\033[0;37m   \033[0;34m▀\033[0;94;44m▒▒▒\033[0;34m▀\033[0;37m \033[0;94;44m▒▒▒\033[0;37m  \033[0;94;44m▒▒\033[0;37m   \033[0;94;44m▒▒▒▒\033[0;34m▄\033[0;37m \033[0m")
    time.sleep(0.09)
    print(
        "\033[0;94;44m░░\033[0;37m   \033[0;94;44m░░\033[0;37m \033[0;94;44m░░\033[0;37m \033[0;94;44m░░\033[0;37m \033[0;94;44m░░\033[0;37m   \033[0;94;44m░░\033[0;37m         \033[0;94;44m░░\033[0;37m \033[0;94;44m░░\033[0;37m   \033[0;94;44m░░\033[0;37m \033[0;94;44m░░\033[0;37m \033[0;94;44m░░\033[0;37m \033[0;94;44m░░\033[0;37m \033[0;94;44m░░\033[0;37m   \033[0;94;44m░░\033[0;37m \033[0;94;44m░░\033[0;37m     \033[0;94;44m░░\033[0;37m   \033[0;94;44m░░\033[0;37m \033[0;94;44m░░\033[0;37m \033[0;94;44m░░\033[0;37m   \033[0;94;44m░░\033[0;37m   \033[0;94;44m░░\033[0;37m \033[0;94;44m░░\033[0;37m \033[0m")
    time.sleep(0.09)
    print(
        "\033[0;94;44m░░\033[0;37m   \033[0;94;44m░░\033[0;37m \033[0;94;44m░░\033[0;37m \033[0;94;44m░░\033[0;37m \033[0;94;44m░░\033[0;37m  \033[0;94;44m░░\033[0;37m       \033[0;94;44m░░\033[0;37m \033[0;94;44m░░\033[0;37m \033[0;94;44m░░\033[0;37m   \033[0;94;44m░░\033[0;37m \033[0;94;44m░░\033[0;37m \033[0;94;44m░░\033[0;37m \033[0;94;44m░░\033[0;37m \033[0;94;44m░░\033[0;37m   \033[0;94;44m░░\033[0;37m \033[0;94;44m░░\033[0;37m     \033[0;94;44m░░\033[0;37m   \033[0;94;44m░░\033[0;37m \033[0;94;44m░░\033[0;37m \033[0;94;44m░░\033[0;37m   \033[0;94;44m░░\033[0;37m   \033[0;94;44m░░\033[0;37m \033[0;94;44m░░\033[0;37m \033[0m")
    time.sleep(0.09)
    print(
        "\033[0;34m██▄█\033[0;37m \033[0;34m██▄██\033[0;37m \033[0;34m██\033[0;37m \033[0;34m██\033[0;37m \033[0;34m██\033[0;37m        \033[0;34m██▄██\033[0;37m \033[0;34m██▄█\033[0;37m \033[0;34m██\033[0;37m \033[0;34m██\033[0;37m \033[0;34m▀█▄█▀\033[0;37m \033[0;34m██▄█\033[0;37m \033[0;34m██\033[0;37m \033[0;34m██\033[0;37m     \033[0;34m██▄█\033[0;37m \033[0;34m██\033[0;37m \033[0;34m██\033[0;37m \033[0;34m██▄█\033[0;37m \033[0;34m██▄█\033[0;37m \033[0;34m██\033[0;37m \033[0;34m██\033[0;37m \033[0m")
    time.sleep(0.09)
    print(
        "\033[0;34m▀▀▀▀\033[0;37m \033[0;34m▀▀▀▀\033[0;37m  \033[0;34m▀▀\033[0;37m \033[0;34m▀▀\033[0;37m \033[0;34m▀▀\033[0;37m        \033[0;34m▀▀▀▀\033[0;37m  \033[0;34m▀▀▀▀\033[0;37m \033[0;34m▀▀\033[0;37m \033[0;34m▀▀\033[0;37m   \033[0;34m▀\033[0;37m   \033[0;34m▀▀▀▀\033[0;37m \033[0;34m▀▀\033[0;37m \033[0;34m▀▀\033[0;37m     \033[0;34m▀▀▀▀\033[0;37m \033[0;34m▀▀\033[0;37m \033[0;34m▀▀\033[0;37m \033[0;34m▀▀▀▀\033[0;37m \033[0;34m▀▀▀▀\033[0;37m \033[0;34m▀▀\033[0;37m \033[0;34m▀▀\033[0;37m \033[0m")
    time.sleep(0.09)
    print(
        "\033[0;37m    \033[0;94m▄▄\033[0;37m                                 \033[0;94m▄▄\033[0;37m               \033[0;94m▄▄\033[0;37m \033[0;94m▄▄\033[0;37m \033[0m")
    time.sleep(0.08)
    print(
        "\033[0;37m    \033[0;94m██\033[0;37m                                 \033[0;94m██\033[0;37m               \033[0;94m██\033[0;37m \033[0;94m██\033[0;37m \033[0m")
    time.sleep(0.08)
    print(
        "\033[0;37m    \033[0;94;44m▓▓\033[0;37m                       \033[0;94;44m▓▓\033[0;37m        \033[0;94;44m▓▓\033[0;37m               \033[0;94;44m▓▓\033[0;37m \033[0;94;44m▓▓\033[0;37m \033[0m")
    time.sleep(0.08)
    print(
        "\033[0;37m    \033[0;94;44m▓▓\033[0;37m    \033[0;94m▄▄\033[0;37m \033[0;94m▄▄\033[0;37m              \033[0;94m▀▀\033[0;37m        \033[0;94;44m▓▓\033[0;37m         \033[0;94m▄\033[0;37m     \033[0;94;44m▓▓\033[0;37m \033[0;94;44m▓▓\033[0;37m \033[0m")
    time.sleep(0.07)
    print(
        "\033[0;37m    \033[0;94;44m▒▒\033[0;94m▄▄\033[0;37m  \033[0;94;44m▒▒\033[0;37m \033[0;94;44m▒▒\033[0;37m     \033[0;94m▄▄▄▄▄▄\033[0;37m  \033[0;94m▄▄▄▄\033[0;37m  \033[0;94m▄▄▄▄\033[0;37m \033[0;94;44m▒▒▒▒\033[0;37m  \033[0;94m▄▄▄▄\033[0;37m \033[0;94;44m▒▒\033[0;94m▄\033[0;94;44m▒▒\033[0;37m \033[0;94;44m▒▒\033[0;37m \033[0;94;44m▒▒\033[0;37m \033[0m")
    time.sleep(0.07)
    print(
        "\033[0;37m    \033[0;94;44m▒▒\033[0;37m \033[0;94;44m▒▒\033[0;37m \033[0;94;44m░░\033[0;37m \033[0;94;44m░░\033[0;37m     \033[0;94;44m▒▒\033[0;37m \033[0;94;44m▒\033[0;37m \033[0;94;44m▒▒\033[0;37m  \033[0;94;44m▒▒\033[0;37m  \033[0;94;44m▒▒\033[0;37m \033[0;94;44m▒▒\033[0;37m \033[0;94;44m▒▒\033[0;37m   \033[0;94;44m▒▒\033[0;37m \033[0;94;44m▒▒\033[0;37m \033[0;94;44m▒▒\033[0;37m \033[0;94;44m▒▒\033[0;37m \033[0;34m▀\033[0;94;44m▒▒▒▒\033[0;37m \033[0m")
    time.sleep(0.07)
    print(
        "\033[0;37m    \033[0;94;44m░░\033[0;37m \033[0;94;44m░░\033[0;37m \033[0;94;44m░░\033[0;37m \033[0;94;44m░░\033[0;37m     \033[0;94;44m░░\033[0;37m \033[0;94;44m░\033[0;37m \033[0;94;44m░░\033[0;37m  \033[0;94;44m░░\033[0;37m  \033[0;34m▀\033[0;94;44m░\033[0;34m▄▄\033[0;37m  \033[0;94;44m░░\033[0;37m   \033[0;94;44m░░\033[0;34m▄\033[0;94;44m░░\033[0;37m \033[0;94;44m░░\033[0;37m    \033[0;34m  \033[0;37m \033[0;94;44m░░\033[0;37m \033[0m")
    time.sleep(0.07)
    print(
        "\033[0;37m    \033[0;94;44m░░\033[0;37m \033[0;94;44m░░\033[0;37m \033[0;34m██\033[0;37m \033[0;34m██\033[0;37m     \033[0;94;44m░░\033[0;37m \033[0;94;44m░\033[0;37m \033[0;94;44m░░\033[0;37m  \033[0;94;44m░░\033[0;37m  \033[0;34m▄▄\033[0;37m \033[0;94;44m░░\033[0;37m \033[0;94;44m░░\033[0;37m   \033[0;94;44m░░\033[0;37m \033[0;34m▄▄\033[0;37m \033[0;94;44m░░\033[0;37m    \033[0;94;44m░░\033[0;37m \033[0;94;44m░░\033[0;37m \033[0m")
    time.sleep(0.07)
    print(
        "\033[0;37m    \033[0;34m██\033[0;37m \033[0;34m██\033[0;37m  \033[0;34m▀▀██\033[0;37m     \033[0;34m██\033[0;37m   \033[0;34m██\033[0;37m  \033[0;34m██\033[0;37m  \033[0;34m██\033[0;37m \033[0;34m██\033[0;37m \033[0;34m██\033[0;37m \033[0;34m█\033[0;37m \033[0;34m██\033[0;37m \033[0;34m██\033[0;37m \033[0;34m██\033[0;37m    \033[0;34m██\033[0;37m \033[0;34m██\033[0;37m \033[0m")
    time.sleep(0.07)
    print(
        "\033[0;37m    \033[0;34m▀▀▀▀\033[0;37m  \033[0;34m▄█\033[0;37m \033[0;34m██\033[0;37m     \033[0;34m▀▀\033[0;37m   \033[0;34m▀▀\033[0;37m \033[0;34m▀▀▀▀\033[0;37m \033[0;34m▀▀▀▀\033[0;37m   \033[0;34m▀▀▀\033[0;37m  \033[0;34m▀▀▀▀\033[0;37m \033[0;34m▀▀\033[0;37m    \033[0;34m▀▀▀▀ \033[0;37m \033[0m")
    time.sleep(0.07)
    print(
        "\033[0;37m          \033[0;34m▀█\033[0;37m \033[0;34m██\033[0;37m                                               \033[0m")
    time.sleep(0.07)
    print("\033[0;37m            \033[0;34m▀██\033[0;37m                                               \033[0m")

def clear_terminal():
    input('enter a any key ')
    os.system('cls' if os.name == 'nt' else 'clear')


def get_cookie_from_header(headers, cookie_name):
    set_cookie = headers.get('Set-Cookie', '')
    cookies = {}
    for part in set_cookie.split(','):
        key_value = part.split(';', 1)[0].strip()
        if '=' in key_value:
            key, value = key_value.split('=', 1)
            cookies[key.strip()] = value.strip()
    return cookies.get(cookie_name, '')
while True:
    try:
        draw_watermark()
        print(colorama.Fore.BLUE+ colorama.Style.DIM+'\033[1m Proxy/AntiDDOS cheker v0.1')
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

        if headers.get('server') == 'cloudflare' or headers.__contains__('cf-ray') or headers.__contains__('cf-cache-status'): # cloudflare check
            print(f'server: cloudflare: \n'
                  f' cf-ray: {headers.get("CF-Ray")} \n'
                  f' __cf_bm: {get_cookie_from_header(headers,'__cf_bm')} \n'
                  f' CF-Cache-Status: {headers.get("CF-Cache-Status")} \n'
                  f' age: {headers.get("age")}')
        elif headers.__contains__('X-Akam-SW-Version'):
            print(f'server: Akamai: \n '
                  f'X-Akam-SW-Version - {headers.get("X-Akam-SW-Version")} \n'
                  f' Akamai-GRN - {headers.get('Akamai-GRN')} \n'
                  f' age: {headers.get("age")}  ')
        elif headers.get('X-Cache') == 'Miss from cloudfront' or headers.get('X-Cache') == 'Hit from cloudfront':
            print(f'server: cloudfront: \n'
                  f' via: {headers.get("Via")} \n'
                  f' X-Amz-Cf-Pop: {headers.get("X-Amz-Cf-Pop")} \n'
                  f' X-Amz-Cf-Id: {headers.get("X-Amz-Cf-Id")} \n'
                  f' age: {headers.get("age")}')
        elif headers.get('Server','').__contains__('rdwr'):
            print(f'server: {headers.get("Server")}: \n'
                  f' __uzma: {get_cookie_from_header(headers,'__uzma')}   \n '
                  f' __uzmb: {get_cookie_from_header(headers,'__uzmb')}   \n'
                  f' __uzme: {get_cookie_from_header(headers,'__uzme')}   \n'
                  f' __uzmc: {get_cookie_from_header(headers,'__uzmc')}   \n'
                  f' __uzmd: {get_cookie_from_header(headers,'__uzmd')}   \n'
                  f' __uzmf: {get_cookie_from_header(headers,'__uzmf')}   \n'
                  f' uzmx: {get_cookie_from_header(headers,'uzmx')}   \n'
                  f' age: {headers.get("age")}')
        elif headers.get('Server') == 'ddos-guard':
            print(f'server: {headers.get('Server')}: \n'
                  f' __ddg8_: {get_cookie_from_header(headers,'__ddg8_')} \n'
                  f' __ddg10_: {get_cookie_from_header(headers,'__ddg10_')} \n'
                  f' __ddg9_: {get_cookie_from_header(headers,'__ddg9_')} \n'
                  f' __ddg1_: {get_cookie_from_header(headers,'__ddg1_')} \n'
                  f' last-modifed: {headers.get("Last-Modified")} \n'
                  f' Etag: {headers.get("Etag")} \n'
                  f' age: {headers.get("age")}')
        elif headers.get('Server') == 'Angie':
            print(f'server: {headers.get('Server' )}: \n'
                  f' Etag: {headers.get('Eta')} \n'
                  f' X-Cluster: {headers.get("X-Cluster")} \n'
                  f' X-Hit: {headers.get("X-Hit")}')
        elif headers.__contains__('x-vercel-cache') or headers.__contains__('x-vercel-id') or headers.get('Server')== 'Vercel':
            print(f'server: vercel: \n'
                  f' x-vercel-id: {headers.get("x-vercel-id")} \n'
                  f' x-vercel-cache: {headers.get("x-vercel-cache")} \n'
                  f' Etag: {headers.get("Etag")} \n'
                  f' Last-Modified: {headers.get("Last-Modified")} \n'
                  f' age: {headers.get("age")}')
        elif headers.get('Server','').__contains__('Caddy') or headers.get('Server','').__contains__('nginx'):
            print(f'server: {headers.get("Server")}: \n'
                  f' Cookie: {headers.get('Set-Cookie')} \n'
                  f' X-Node: {headers.get("X-Node")} \n'
                  f' X-Version: {headers.get('X-Version')} \n'
                  f' X-NGENIX-Cache: {headers.get('X-NGENIX-Cache')} \n'
                  f' age: {headers.get('age')} \n'
                  f' Alt-Svc{headers.get("Alt-Svc")} \n'
                  f' Etag: {headers.get("Etag")} \n'
                  f' Last-Modified: {headers.get("Last-Modified")} ')
        elif headers.get('Server','').__contains__('QRATOR'):
            print(f'server: {headers.get('Server')}: \n'
                  f' ETag: {headers.get('Etag')} \n'
                  f' qrator_jsr: {get_cookie_from_header(headers,'qrator_jsr')} \n'
                  f' age: {headers.get("age")} \n'
                  f' last-modifed: {headers.get('Last-Modified')} \n'
                  f' X-Powered-By: {headers.get('X-Powered-By')} \n'
                  f' x-trace-id: {headers.get('x-trace-id')} \n'
                  f' x-request-id: {headers.get('x-request-id')} \n'
                  f' _ymab_param: {headers.get('_ymab_param')} ')
        elif headers.__contains__('yandex'):
            print(f'server: yandex: \n'
                  f' _yasc: {headers.get('_yasc')} \n'
                  f' _ymab_param: {headers.get('_ymab_param')} \n'
                  f' XSRF-TOKEN: {headers.get('XSRF-TOKEN')} \n'
                  f' x-trace-id: {headers.get('x-trace-id')} \n'
                  f' ETag: {headers.get('Etag')} \n'
                  f' last-modified: {headers.get('last-modified')} ')
        elif headers.get('Server','').__contains__('Mitelis DDoS-Mitigation'):
            print(f'server: {headers.get('server')}: \n'
                  f' X-MITELIS-CACHE: {headers.get('X-MITELIS-CACHE')} \n'
                  f' x-powered-by: {headers.get('x-powered-by')} \n'
                  f' last-modified: {headers.get("last-modified")}')
        elif headers.get('server','').__contains__('Apache'):
            print(f'server: {headers.get('server')} \n'
                  f' Set-Cookie: {headers.get('Set-Cookie')} \n'
                  f' Via: {headers.get('Via')}')
        elif headers.get('server','').__contains__('HAProxy'):
            print(f'server: {headers.get("server")}: \n'
                  f' x-request-id: {headers.get("x-request-id")} \n'
                  f' x-chache: {headers.get("x-chache")} \n')
        #getcookie_fromheader(headers)
        print(headers.get('Server'))
        print(headers)
        clear_terminal()
    except error as a:
        print(a)
    except KeyboardInterrupt:
        print('')







# See PyCharm help at https://www.jetbrains.com/help/pycharm/
