from app.models.modelCars import Car, CarDataValue, CarData
from app import db


def AddCarValueToDb(car,form):
	carValue1 = CarDataValue(valueInt = form.kmattuali.data,
                                           id_CarData = 1, car_author = car )
	db.session.add(carValue1)
	carValue2 = CarDataValue(valueDate = form.dataRevisione.data,
                                           id_CarData = 2, car_author = car )
	db.session.add(carValue2)
	carValue3 = CarDataValue(valueInt = form.kmTagliando.data,
                                           id_CarData = 3, car_author = car )
	db.session.add(carValue3)
	carValue4 = CarDataValue(valueDate = form.dataAssicurazione.data,
                                           id_CarData = 4, car_author = car )
	db.session.add(carValue4)
	carValue5 = CarDataValue(valueDate = form.dataBollo.data,
                                           id_CarData = 5, car_author = car )
	db.session.add(carValue5)
	carValue6 = CarDataValue(valueInt = form.kmMedi.data,
                                           id_CarData = 6, car_author = car )
	db.session.add(carValue6)
		