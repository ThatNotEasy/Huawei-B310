import requests

# Create a session
session = requests.Session()

# First Request
url_challenge_login = 'http://192.168.8.1/api/user/challenge_login'
headers_challenge_login = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,ms;q=0.8',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'http://192.168.8.1',
    'Referer': 'http://192.168.8.1/html/home.html',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    '__RequestVerificationToken': 'YQBEiZZ7tKnaZg1gU1zXAC1ic7vJmosr',
}

data_challenge_login = {
    'admin': '7f00894e43716f342c908621b58df9b4d1b59891acb0ef91f45ee9128a5a59a51',
}

response_challenge_login = session.post(url_challenge_login, headers=headers_challenge_login, data=data_challenge_login)

print('Response for Challenge Login:')
print(f'Response status code: {response_challenge_login.status_code}')
print('Response content:')
print(response_challenge_login.text)
print('Cookies:')
print(session.cookies.get_dict())
print('Headers:')
print(response_challenge_login.request.headers)
print('\n')

# Second Request
url_authentication_login = 'http://192.168.8.1/api/user/authentication_login'
headers_authentication_login = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,ms;q=0.8',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'http://192.168.8.1',
    'Referer': 'http://192.168.8.1/html/home.html',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    '__RequestVerificationToken': 'N4d9PiM/L+xDLFbctyLqoFbHNzlDxlbV',
}

data_authentication_login = {
    'f8eb25cafaad88ead57fc3b2229cbd3ef2a1b335ac7e811b1d9b539655428d937f00894e43716f342c908621b58df9b4d1b59891acb0ef91f45ee9128a5a59a58EgC07vBWJysUW7kxdC0EmqSW7apHYJM',
}

response_authentication_login = session.post(url_authentication_login, headers=headers_authentication_login, data=data_authentication_login)

print('Response for Authentication Login:')
print(f'Response status code: {response_authentication_login.status_code}')
print('Response content:')
print(response_authentication_login.text)
print('Cookies:')
print(session.cookies.get_dict())
print('Headers:')
print(response_authentication_login.request.headers)

import base64

encoded_string = "VmxER7/2f9gOa2qDFFgSAa1lTyT3mSjwpgH9IUhegequlsSLTPu4y933uj9h4uzf+1RB17yKfzXT45i5IsPU3McT64vIeDqXiX1Bn6NxV3bpKPqWUfkg90rcAM52dlI4"

# Decode the base64 string
decoded_bytes = base64.b64decode(encoded_string)

# Display the decoded bytes as a list of integers
decoded_byte_values = list(decoded_bytes)
print("Decoded Bytes:")
print(decoded_byte_values)