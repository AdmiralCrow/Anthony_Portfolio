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


# Define a function to geocode a location string and return the (latitude, longitude) tuple
def geocode_location(location):
    print(f"Geocoding location: {location}")
    
    try:
        # Use the geocoder to geocode the location
        geocoded = gmaps.geocode(location)

        # If a location was found, return its (latitude, longitude) tuple
        if len(geocoded) > 0:
            lat = geocoded[0]['geometry']['location']['lat']
            lng = geocoded[0]['geometry']['location']['lng']
            print(lat, lng)
            return (lat, lng)

    except (Timeout, ApiError):
        # If the geocoding request timed out or encountered an API error, log an error message and return None
        print(f"Error geocoding location: {location}")
        return None

    # If geocoding failed, log an error message and return None
    print(f"Unable to geocode location: {location}")
    return None

# Apply the geocode_location function to the "Address" column of the DataFrame, with a delay of 1 second between requests
attacksdf["coordinates"] = attacksdf[["Address"]].apply(lambda x: (geocode_location(", ".join(x)), time.sleep(1))[0], axis=1)


# Extract the latitude and longitude into separate columns
attacksdf["latitude"] = attacksdf["coordinates"].apply(lambda x: x[0] if x is not None else None)
attacksdf["longitude"] = attacksdf["coordinates"].apply(lambda x: x[1] if x is not None else None)

# Remove the "coordinates" column
attacksdf = attacksdf.drop("coordinates", axis=1)

# Print the resulting DataFrame
print(attacksdf.head())
print("Failed to geocode the following rows:")
print(attacksdf[attacksdf['latitude'].isna()])
#https://maps.googleapis.com/maps/api/geocode/json?address=Shipwreck%20s%20Beach,%20Keoneloa%20Bay,%20Kauai,%20Hawaii,%20USA&key=AIzaSyAAJOzQeBv0O77OmqJAz3sHoAL8-1pBF08

