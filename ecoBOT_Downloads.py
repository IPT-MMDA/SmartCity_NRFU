import requests
import pandas as pd
import csv
import os
import geopandas as gpd
import time

data = gpd.read_file(r"/home/eouser/data/smartcity/ecobot/shp/pointsUkraine.shp")

for id_value in data["id"]:
    print('id: ', id_value)
    url = f'https://www.saveecobot.com/api/v1/sensor-archives/{id_value}'
    headers = {
        "apikey": "hYTHIqWuYqmO15lUFPVS0IuRpt1Wka2x",
    }

    response = requests.get(url, headers=headers)
    data = response.text.split('\n')

    csv_file = f'sensor_data{id_value}.csv'

    with open(csv_file, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].split(','))
        writer.writeheader()
        for line in data[1:]:
            if line:
                writer.writerow(dict(zip(data[0].split(','), line.split(','))))
    time.sleep(1)