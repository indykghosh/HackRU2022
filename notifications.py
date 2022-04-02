import os
from twilio.rest import Client
import datetime
import pandas as pd

key = "SKd9a607a5573a97dc32002e2b43648675"
secret = "gjyVH0EUvl3I8XXVJ4W3s4zfgwVoZly5"
twilio_sid = "AC6e7f493586c79a5c3cf3a8e85305af4d"
mg_sid = "MGbc475ef0b56418fd500454d524e52384"

# twilio_sid = os.environ['TWILIO_SID']
# key = os.environ['TWILIO_API_KEY']
# secret = os.environ['TWILIO_API_SECRET']

notif_list = ['+18482473420']
events = []

client = Client(key, secret, twilio_sid)

month_dict = {
    'january': 1, 'fbruary' : 2, 'march' : 3, 'april' : 4,
    'may' : 5, 'june' : 6, 'july' : 7, 'august' : 8, 'september' : 9,
    'october' : 10, 'november' : 11, 'december' : 12
}

def schedule_notifs(event, dateStart):
    send_day = int(dateStart.strftime("%d"))
    send_month = int(dateStart.strftime("%m"))
    
    for i in range(7):
      if send_day == 1:
        send_month -= 1
        if send_month == 2:
          send_day = 28
        elif send_month == 4 or send_month == 6 or send_month == 9 or send_month == 11:
          send_day = 30
        else:
          send_day = 31
      else:
        send_day -= 1

    send_date = datetime.datetime(int(dateStart.strftime("%Y")), send_month, send_day, 14)

    # test_date = datetime.datetime(2022, 4, 2, 14)

    print(send_date.strftime("%A, %B %d %Y"))


    for number in notif_list:
        print(number)
        mess_body = event + 'will begin in a week on ' + dateStart.strftime("%A, %B %d")
        message = client.messages \
            .create(
                messaging_service_sid = mg_sid,
                body = "testing schedules message",
                send_at = send_date,
                schedule_type='fixed',
                to=number
            )


#make into separate function
# file = 'events.csv'
# df = pd.read_csv(file)



year = 2022
month = 4
day = 10


send_date = datetime.datetime(year, month, day, 0, 22, 0)
events.append("Thanksgiving Break")

schedule_notifs(events[0], send_date)
