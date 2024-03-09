from pvlib.location import Location

# Rome, Italy data
latitude = 41.9
longitude = 12.5
tz = 'Europe/Rome'
altitude = 27
name = 'Rome'

location = Location(latitude, longitude, tz, altitude, name)

tus = Location(32.2, -111, 'US/Arizona', 700, 'Tucson')
print(tus)
golden = Location(39.742476, -105.1786, 'America/Denver', 1830, 'Golden')
print(golden)
golden_mst = Location(39.742476, -105.1786, 'MST', 1830, 'Golden MST')
print(golden_mst)
berlin = Location(52.5167, 13.3833, 'Europe/Berlin', 34, 'Berlin')
print(berlin)