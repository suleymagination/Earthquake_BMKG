"""
Earthquake Detection App
"""


def extract_data():
    """
    Date: August 25, 2023, 18:42:23 WIB
    Magnitude: 4.0
    Depth: 3 km
    Geolocation: 4.52 N - 96.45 E
    Center: The earthquake center is located on land 35 km northeast of Nagan Raya Regency
    Felt: Felt (MMI Scale): II Nagan Raya
    """
    earthquake = dict()
    earthquake["date"] = "August 25, 2023"
    earthquake["time"] = "18:42:23"
    earthquake["magnitude"] = "4.0"
    earthquake["depth"] = "3 km"
    earthquake["geolocation"] = {"latitude": "4.52 N", "longitude": "96.45 E"}
    earthquake["center"] = "The earthquake center is located on land 35 km northeast of Nagan Raya Regency"
    earthquake["felt"] = "Felt (MMI Scale): II Nagan Raya"
    return earthquake


def show_data(data):
    print("Recent Earthquake in Indonesia")
    print(f"Date: {data['date']}")
    print(f"Time: {data['time']}")
    print(f"Magnitude: {data['magnitude']}")
    print(f"Depth: {data['depth']}")
    print(f"Geolocation: Latitude= {data['geolocation']['latitude']}, Longitude= {data['geolocation']['longitude']}")
    print(f"Center: {data['center']}")
    print(data['felt'])


if __name__ == "__main__":
    print("Main App")
    data = extract_data()
    show_data(data)
    