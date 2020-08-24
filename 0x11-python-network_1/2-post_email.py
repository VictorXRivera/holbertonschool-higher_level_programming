#!/usr/bin/python3
""" Script that takes in email and URL as parameters and sends POST request """

if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys

    if len(sys.argv) < 3:
        print("Usage: ./2-post_email.py domain_name email_address")
        exit(1)

    domain = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email})
    data = data.encode('ascii')
    with urllib.request.urlopen(domain, data) as response:
        body = response.read()
        print(body.decode('utf-8'))
