import datetime

#Objeto tipo date#
date=datetime.date(2020,4,30)
print(date.year)
print(date.month)
print(date.day)

#Devuelve el dia de la semana el lunes es el cero y domingo el 6#
print(date.weekday())

#Devuelve el dia de la semana el lunes es el 1 y domingo el 7#
print(date.isoweekday())

#Devuelve una tupla con año, numero de la semana, dia de la semana#
print(date.isocalendar())

#Devuelve la fecha como un String#
print(date.isoformat())

#Fecha minima#
date_min=datetime.date.min
print(date_min)

#Fecha Maxima#
date_max=datetime.date.max
print(date_max)
#Dia de hoy#
print(datetime.date.today())
#dia de ayer# #operaciones con fechas#
yesterday=datetime.date.today()-datetime.timedelta(days=1)
print(yesterday)


#Objeto tipo timedelta#
date_and_time=datetime.datetime(2020,10,19,16,06,50)
#fecha normal#
print(date_and_time.date())
#el tiempo actual con horas, minutos y segundos#
print(datetime.datetime.now())
#fecha y hora actual en UTC (Coordinated Universal Time)#
print(datetime.datetime.utcnow())


#Objeto tipo time#
time=datetime.time(11,20,35)
print(time.hour)
print(time.min)
print(time.second)

#Convertir fechas en String y Viceversa#
date2=datetime.datetime(2020,10,19,16,6,50)
#funcion strftime convierte fecha a String#
print(date2.strftime('%Y-%m-%d'))
date2.strftime('%Y-%m-%d %H: %M: %S')
#funcion strptime convierte el String a fecha#
print(datetime.datetime.strptime('2019-01-10', '%Y-%m-%d'))













