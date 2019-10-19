import os.path
import pandas as pd
from .models import Satellite
from pyorbital.orbital import Orbital
from datetime import datetime

def get_satellite_coordinates(lon, lat, alt, satellite_id):
    try:
        satellite = Satellite.objects.get(id=satellite_id)
        orb = Orbital(satellite.codename)
        now = datetime.utcnow()
        return orb.get_observer_look(now, lon, lat, alt)
    except Satellite.DoesNotExist:
        return None

def load_data():
    path = 'nasaData/core/data/dataSet.xlsx'
    if(os.path.exists(path)):
        df = pd.read_excel(path)
        indexes = ['name', 'satellite_type',
        'description','launch_date', 'codename']
        columns = df.columns
        ## All string to lowecase
        columns = [x.lower() for x in list(columns)]
        if(set(indexes).issuperset(set(columns))):
            for index, row in df.iterrows():
                save_satellite(row)

def save_satellite(row):

    # Check for existent satellite, or create new one

    try:
        satellite = Satellite.objects.get(
            name=row['name'],
        )
    except Satellite.DoesNotExist:
        satellite = Satellite(
            satellite_type=row['satellite_type'],
            name=row['name'],
            description=row['description'],
            launch_date=row['launch_date'],
            codename=row['codename']
        )
        satellite.save()

    return satellite
