
import requests

URL = 'https://www.python.org'

response = requests.get(URL)

if response.status_code == requests.codes.OK:

    for header, value in sorted(response.headers.items()): # response.headers is a dictionary of the headers
        print("{:20.20s} {}".format(header, value))
    print()

    # response.content  raw data as bytes
    # response.json()   JSON converted to Python data structure
    # response.text     raw data converted to Python str


    print(response.text[:200])   # The text is returned as a bytes object, so it needs to be decoded to a string; print the first 200 bytes
    print('...')
    print(response.text[-200:])   # print the last 200 bytes
