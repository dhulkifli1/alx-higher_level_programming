#!/usr/bin/python3
'''
Takes in a URL, sends a request to the URL and displays the value of
the X-Request-Id variable found in the header of the response
'''


if __name__ == '__main__':
    import sys
    import urllib.request

    url = sys.argv[1]
    with urllib.response.urlopen(url) as response:
        id = response.headers.get('X-Request-Id')
        print(id)
