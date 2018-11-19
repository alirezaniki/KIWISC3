from pyrocko import orthodrome

# arguments: origin lat, origin lon, north [m], east [m]
lat, lon = orthodrome.ne_to_latlon(37.58, 57.11, 3000.0, 10000.0)

print(lat, lon)
