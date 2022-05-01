# Python Version 2.7.10
# Dark Sky

# Dark Sky Weather

# Import | From
from darksky import forecast

# API Key
api_key = 'api_key_here'

# Hometown
SEATTLE = forecast(api_key, 47.6036, 122.3294)

# Current
OKLAHOMA_CITY = forecast(api_key, 35.4676, 97.5164)

# 5 Places to Visit
QUEENSLAND_AUSTRALIA = forecast(api_key, 20.9176, 142.7028)
TOKYO_JAPAN = forecast(api_key, 35.6804, 139.7690)
NORWAY = forecast(api_key, 60.4720, 8.4689)
DENMARK = forecast(api_key, 56.2639, 9.5018)
SWEDEN = forecast(api_key, 60.1282, 18.6435)


# Print Statements
print ('Seattle Daily Summary: \n' + SEATTLE.daily.summary + '\n')
print ('Oklahoma City Daily Summary: \n' + OKLAHOMA_CITY.daily.summary + '\n')

print ('Queensland Australia Current Temperature:' + str(QUEENSLAND_AUSTRALIA.currently.temperature) + ' Degrees')
print ('Tokyo Japan Current Temperature:' + str(TOKYO_JAPAN.currently.temperature) + ' Degrees')
print ('Norway Current Temperature:' + str(NORWAY.currently.temperature) + ' Degrees')
print ('Denmark Current Temperature:'+ str(DENMARK.currently.temperature) + ' Degrees')
print ('Sweden Current Temperature:'+ str(SWEDEN.currently.temperature) + ' Degrees')
