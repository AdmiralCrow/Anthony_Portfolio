import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import googlemaps
import time
import folium
from requests.exceptions import Timeout
from googlemaps.exceptions import ApiError

#input DF
attacksdf = pd.read_csv('Your File Location', header=0, encoding = 'ISO-8859-1')

#drops NaN
attacksdf.dropna()

#combine location, area, and country column into 1 column
attacksdf['Country'] = attacksdf.apply(lambda x: f"{x['Location']}, {x['Area']}, {x['Country']}", axis=1)

#erase area, location
attacksdf = attacksdf.drop(['Area', 'Location'], axis=1)

#rename country column to addres
attacksdf = attacksdf.rename(columns={'Country': 'Address'})
print(attacksdf.head(30))

#input of location DF
locationdf=pd.read_csv('Your File Location', header=0, encoding = 'ISO-8859-1')
print(locationdf)

# Define the CRS for the GeoDataFrame
crs = 'epsg:4326'

# Create a geometry column from the LONDEC and LATDEC columns
geometry = [Point(xy) for xy in zip(locationdf['LONDEC'], locationdf['LATDEC'])]

# Create a GeoDataFrame
gdf = gpd.GeoDataFrame(locationdf, crs=crs, geometry=geometry)

# Optional: drop the LONDEC and LATDEC columns if you don't need them
gdf = gdf.drop(columns=['LONDEC', 'LATDEC'])

#geoDF for points
geo_df= gpd.GeoDataFrame(locationdf,crs=crs,geometry=gpd.points_from_xy(locationdf["LATDEC"], locationdf["LONDEC"]))
geo_df

#list of species of sharks on record for attacks
attacksdf = attacksdf.rename(columns={'Species ': 'Species'})
list_species = attacksdf.Species
list_species.dropna()

# Define the CRS for the GeoDataFrame
crs = 'epsg:4326'

# Create a geometry column from the LONDEC and LATDEC columns
geometry = [Point(xy) for xy in zip(locationdf['LONDEC'], locationdf['LATDEC'])]

# Create a GeoDataFrame
gdf = gpd.GeoDataFrame(locationdf, crs=crs, geometry=geometry)

# Optional: drop the LONDEC and LATDEC columns if you don't need them
gdf = gdf.drop(columns=['LONDEC', 'LATDEC'])

# Initialize the Google Maps API client, you will need to have an active Geolocation API through GCP
gmaps = googlemaps.Client(key='Your API Key')

# Define the map center as the approximate center of Australia
center_lat, center_lon = -25.2744, 133.7751

# Create a map using the Google Maps tiles
m = folium.Map(location=[center_lat, center_lon], zoom_start=4, tiles='https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}', attr='Google')

# Add markers for each data point
for idx, row in gdf.iterrows():
    location = (row.geometry.x, row.geometry.y)
    address = row['geometry']
    folium.Marker(location, tooltip=address, icon=folium.Icon(color='red')).add_to(m)

# Display the map
m

