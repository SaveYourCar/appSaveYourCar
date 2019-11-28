from app.models.modelCars import Car, CarDataValue, CarData
from app import db

def AddCarValueToDb(car,form):
	lista = [form.kmattuali.data, form.dataRevisione.data,
             form.kmTagliando.data, form.dataAssicurazione.data,
             form.dataBollo.data, form.kmMedi.data]
	carDataValue={}
	for i in range(1,7):
		if i == 1 or 3 or 6:
			carDataValue[i] = CarDataValue(valueInt = lista[i-1],
                                           id_CarData = i, car_author = car )
			db.session.add(carDataValue[i])
		elif i == 2 or 4 or 5:
			carDataValue[i] = CarDataValue(valueDate = lista[i-1],
                                           id_CarData = i, car_author = car )
			db.session.add(carDataValue[i])