import pyowm
p = input('Введіть місто ')
owm = pyowm.OWM('2d09fe1dc7dd25b2ce61b52a358b9fde')
observation = owm.weather_at_place(p)
w = observation.get_weather()
temp = w.get_temperature('celsius')
tempint = temp['temp'] // 1
print('Зараз температура : ' + str(int(tempint)))
