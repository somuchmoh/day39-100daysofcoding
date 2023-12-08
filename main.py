from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from datetime import datetime, timedelta
from notification_manager import NotificationManager

data = DataManager()
sheet_data = data.prices
flight_search = FlightSearch()
flight_data = FlightData()
notif = NotificationManager()

for i in range(0, len(sheet_data)):
    if sheet_data[i]['iataCode'] == '':
        row_id = sheet_data[i]['id']
        code = flight_search.get_code(city_name=sheet_data[i]['city'])
        body = {"price": {
                        "iataCode": code,
                    }}
        data.update_sheet(row_id=row_id, body=body)

for n in range(0, len(sheet_data)):
    flight_info = flight_data.get_data(city=sheet_data[n]['iataCode'])['data']
    my_price = sheet_data[n]['lowestPrice']
    for i in range(0, len(flight_info)):
        if flight_info[i]['price'] < my_price:
            fly_city = flight_info[i]['cityTo']
            fly_price = flight_info[i]['price']
            city_iata = flight_info[i]['cityCodeTo']
            nights = flight_info[i]['nightsInDest']
            fly_on = flight_info[i]['local_departure']
            fly_on_date = datetime.strptime(fly_on.split("T")[0], '%Y-%m-%d')
            fly_on_date_1 = str(fly_on_date).strip("00:00:00")
            fly_from_date = fly_on_date + timedelta(days=nights)
            fly_from_date_1 = str(fly_from_date).strip("00:00:00")
            notif.send_notif(price=fly_price, city_to=fly_city, iata_code=city_iata,
                             from_date=fly_on_date_1, to_date=fly_from_date_1)
