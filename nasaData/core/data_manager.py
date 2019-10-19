import pandas as pd
from .models import Satellite

def get_data():

    df = pd.read_excel('data/dataSet.xlsx')
    indexes = ['name', 'satellite_type', 'description','launch_date']
    ## All string to lowecase
    columns = [x.lower() for x in list(columns)]
    if(set(indexes).issuperset(set(columns))):
        for index, row in df.iterrows():
            self.save_satellite(row)

    return None

def save_satellite(self, row):

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
            launch_date=row['launch_date']
        )
        satellite.save()

    return satellite
