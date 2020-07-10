from geolite2 import geolite2
import requests


try:
    my_ip = int(input("Enter the ip you want to locate, Leave blank for your : "))
except ValueError:
    my_ip = requests.get('https://api.ipify.org').text


def my_ip_location(my_ip):
    reader = geolite2.reader()
    location = reader.get(my_ip)

    print(f'Your IP: {my_ip}')

    # geolite database dict values and fine tunning
    a = (location['city']['names']['en'])
    b = (location['continent']['names']['en'])
    c = (location['country']['names']['en'])
    d = (location['location'])

    f = (location['registered_country']['names']['en'])
    g = (location['subdivisions'][0]['names']['en'])

    print(
        '''city: %s\ncontinent: %s\ncountry: %s\nlocation: %s\nregistered_country: %s\nsubdivisions: %s\n'''
        % (a, b, c, d, f, g))


my_ip_location(my_ip)
