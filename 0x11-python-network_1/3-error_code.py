#!/usr/bin/python3
'''
Script that takes in a URL,
sends a request to the URL
and displays the body of the response (decoded in utf-8)
'''


if __name__ == '__main__':
    import urllib
    import sys

    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            body = response.read().decode('UTF-8')
            print(body)
    except urllib.error.URLError as e:
        print(f"Error code: {e.code}")
