import time

import requests
from datetime import datetime
import smtplib
import time


my_email = "ahrentestcode@gmail.com"
password = "jvbtrwuhyogyblxa"

MY_LAT = 40.786140 # Your latitude
MY_LONG = -124.161308 # Your longitude
MY_LAT_MIN = 35.784140
MY_LAT_MAX = 45.784140
MY_LONG_MIN = -129.161308
MY_LONG_MAX = -119.161308

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

while True:
    if time_now.hour > sunrise and time_now.hour < sunset:
        is_dark = False
    else:
        is_dark = True

    #If the ISS is close to my current position
    if iss_latitude > MY_LAT_MIN and iss_latitude < MY_LAT_MAX and iss_longitude > MY_LONG_MIN and iss_longitude < MY_LONG_MAX and is_dark:
        smtplib.SMTP()
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="ahrentestcode@yahoo.com",
                                msg=f"Look Up!"
                                )
    time.sleep(60)




