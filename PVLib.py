import pvlib
from pvlib.location import Location
from pvlib.modelchain import ModelChain
from pvlib.pvsystem import PVSystem
from pvlib.temperature import TEMPERATURE_MODEL_PARAMETERS

'''General Info - Database and components'''

sandia_modules = pvlib.pvsystem.retrieve_sam('SandiaMod')
cec_inverter = pvlib.pvsystem.retrieve_sam('CECInverter')

module = sandia_modules[ 'Canadian_Solar_CS5P_220M___2009_']
inverter = cec_inverter['ABB__MICRO_0_25_I_OUTD_US_208__208V_']
temperature_parameters = TEMPERATURE_MODEL_PARAMETERS['sapm']['open_rack_glass_glass']

'''Location'''

# Rome, Italy data
latitude = 41.9
longitude = 12.5
tz = 'Europe/Rome'
altitude = 27
name = 'Rome'

location = Location(latitude, longitude, tz, altitude, name)

'''System'''

system = PVSystem(surface_tilt = 45,
                 surface_azimuth = 180,
                 module_parameters = module,
                 inverter_parameters = inverter,
                 temperature_model_parameters = temperature_parameters
                 )

modelchain = ModelChain(system, location)


