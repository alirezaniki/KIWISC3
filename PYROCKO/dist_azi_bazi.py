from pyrocko import orthodrome, model

e = model.Event(lat=37.58, lon=57.11)
s = model.Event(lat=34.884, lon=57.159)
dist = orthodrome.distance_accurate50m(e, s)
print(dist/1000)

# Azimuth and Back Azimuth
az = orthodrome.azibazi(e, s)
print (az)
