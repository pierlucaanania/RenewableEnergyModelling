from pvlib.location import Location
from pvlib.pvsystem import PVSystem


# Rome, Italy data
latitude = 41.9
longitude = 12.5
tz = 'Europe/Rome'
altitude = 27
name = 'Rome'

location = Location(latitude, longitude, tz, altitude, name)

'''Create Instance'''
system = PVSystem(surface_tilt=45,
                 surface_azimuth=180,
                 )
system

