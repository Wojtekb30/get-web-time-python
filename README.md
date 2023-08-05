# get-web-time-python
Python functions to get current time for a timezone from the Internet, from birdtech.pl website. Works in MicroPython too.

# Introduction:
Have you ever needed to sync your Python project with current time? Do you want to do that on a MicroPython development board like a Raspberry Pi Pico W? Do you find reading time from an NTP too hard? If yes, then this solution is perfect for you!

I created a solution to sync current time with the Internet by just a GET request from my server (birdtech.pl). This way you can access current time in Python as well as in MicroPython, on a Pi Pico W or similar device.

# How to use it?:
Copy the code from getwebtime.py into your project or import it with proper statement. Uncomment "import requests" for standard Python3 or "import urequests as requests" for MicroPython.

Call getwebtimeint or getwebtimestr function and provide timezone number (from -12 to 12) as parameter, use the map below:

Timezone map to use as reference:
![Standard_World_Time_Zones](https://github.com/Wojtekb30/get-web-time-python/assets/112283903/11ba9adf-bbfc-4525-b4f1-86f817041fce)

The function will return an array;

getwebtimestr() will return array with: year [str], month [str], day [str], hour [str], minute [str], second [str] in order in the array.

getwebtimeint() will return array with: year [int], month [int], day [int], hour [int], minute [int], second [int] in order.

Examples:

getwebtimeint(2) - time in Egypt

getwebtimestr(-3) - time in Greenland

# Limitations, usage and privacy policy:
- If you access the time resource from my server too often in short time, then the server may end up slowing down and block your further requests; so do not DDOS it please, even by accident.
- Fetching the data takes a short while so seconds will not be precise.
- My server (birdtech.pl) may save the IP address of the device which accessed it as well as time and browser name (which in case of a pure GET request will likely be empty).
- My server is located in Poland and returns time proper to its timezone.
- Feel free to modify my code from this repository to your needs, for example to fetch time from your own web server (I included the PHP code for server too) or use a proxy. But please credit me as the author of the original solution, especially if you are going to still use my server to get time. Thank you!
