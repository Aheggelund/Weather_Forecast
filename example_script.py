import get_data
from datetime import datetime, timedelta


currentDay = str(datetime.now().strftime('%d'))
currentHour = str((datetime.now()- timedelta(hours=2)).strftime('%H'))
currentMonth = datetime.now().strftime('%m')

if (eval(currentHour) == 22 or eval(currentHour) == 23):
    currentDay = str((datetime.now() - timedelta(days=1)).strftime('%d'))

savefile_path = r'C:/Users/Andreas/Desktop/radarImg/'
gg = get_data.GetData()
gg.get_image_data('accumulated_01h','eastern_norway', currentMonth, currentDay, currentHour, savefile_path)

"""
municipalities = ['Hamar', 'Ringsaker', 'Stange']
measurements = 'mean(air_temperature P1D),sum(precipitation_amount P1D),mean(wind_speed P1D)'
observation_ids = get_source_ids(municipalities)
get_sensor_data(observation_ids, measurements)
"""