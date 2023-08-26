import requests
from bs4 import BeautifulSoup
import locale
from datetime import datetime


def extract():
    """
    Date: August 25, 2023, 18:42:23 WIB
    Magnitude: 4.0
    Depth: 3 km
    Geolocation: 4.52 N - 96.45 E
    Center: The earthquake center is located on land 35 km northeast of Nagan Raya Regency
    Felt: Felt (MMI Scale): II Nagan Raya
    """
    try:
        content = requests.get("https://www.bmkg.go.id/en.html") # <Response [200]> means good!
        # Check this for more information about HTTP response status codes:
        # https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
    except Exception:
        return None
    if content.status_code == 200:
        # print(content.status_code)
        # print(content.text)
        soup = BeautifulSoup(content.text, "html.parser")
        title = soup.find("title")
        print(title.string)
        date = soup.find("span", {"class": "waktu"})
        date_string = date.text
        # Remove the timezone abbreviation from the date string
        date_string = date_string.replace("WIB", "")
        # Create a dictionary to map Indonesian month names to English month names
        month_map = {
            "Januari": "January",
            "Februari": "February",
            "Maret": "March",
            "April": "April",
            "Mei": "May",
            "Juni": "June",
            "Juli": "July",
            "Agustus": "August",
            "September": "September",
            "Oktober": "October",
            "November": "November",
            "Desember": "December"
        }

        # Split the date string into parts
        date_parts = date_string.split()

        # Translate the month name from Indonesian to English
        date_parts[1] = month_map[date_parts[1]]

        # Rejoin the date string
        date_string = ' '.join(date_parts)

        # Parse the date string
        date_format = "%d %B %Y, %H:%M:%S"
        date_object = datetime.strptime(date_string, date_format)
        timestamp = date_object.timestamp()
        # print(soup.prettify())

        earthquake = dict()
        earthquake["date"] = timestamp # "August 25, 2023"
        earthquake["time"] = "18:42:23"
        earthquake["magnitude"] = "4.0"
        earthquake["depth"] = "3 km"
        earthquake["geolocation"] = {"latitude": "4.52 N", "longitude": "96.45 E"}
        earthquake["center"] = "The earthquake center is located on land 35 km northeast of Nagan Raya Regency"
        earthquake["felt"] = "Felt (MMI Scale): II Nagan Raya"
        return earthquake
    else:
        return None


def show_data(data):
    if data is None:
        print("Cannot find data")
        return
    print("Recent Earthquake in Indonesia")
    print(f"Date: {data['date']}")
    print(f"Time: {data['time']}")
    print(f"Magnitude: {data['magnitude']}")
    print(f"Depth: {data['depth']}")
    print(f"Geolocation: Latitude= {data['geolocation']['latitude']}, Longitude= {data['geolocation']['longitude']}")
    print(f"Center: {data['center']}")
    print(data['felt'])
