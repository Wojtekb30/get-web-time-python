#import requests #Uncomment for PC Python
#import urequests as requests #Uncomment for MicroPython (for example RPI Pi Pico)

def getwebtimeint(timezone: int):
    #requires 'requests' or 'urequests' imported as 'requests'
    #Output: year [int], month [int], day [int], hour [int], minute [int], second [int]
    r = requests.get('https://birdtech.pl/api/gettime/polandstring')
    czas = str(r.text).split("/")
    if timezone!=1:
        czas[3] = int(czas[3])-1+timezone
    n = 0
    dlugosc = len(czas)
    while n<dlugosc:
        czas[n] = int(czas[n])
        n=n+1
    #print(czas)
    return czas

def getwebtimestr(timezone: int):
    #requires 'requests' or 'urequests' imported as 'requests'
    #Output: year [str], month [str], day [str], hour [str], minute [str], second [str]
    r = requests.get('https://birdtech.pl/api/gettime/polandstring')
    czas = str(r.text).split("/")
    if timezone!=1:
        czas[3] = str(int(czas[3])-1+timezone)
    #print(czas)
    return czas