import requests,json,pytz,yagmail
from datetime import date
from datetime import datetime

urlWalgreens = "https://www.walgreens.com/hcschedulersvc/svc/v1/immunizationLocations/availability"

########### C:\Python27\ArcGISx6410.6\python.exe C:\Sourcecode\Other\VaccineChecker\VaccinneChecker.py

def CallWalgreens():

    utc_time = datetime.utcnow()
    to_zone = pytz.timezone("US/Eastern")
    from_zone = pytz.timezone('UTC')
    utc_time = utc_time.replace(tzinfo=from_zone)
    eastern = utc_time.astimezone(to_zone)
    today = str(eastern.year) + "-" + str(eastern.month).zfill(2) + "-" + str(eastern.day) 
    print(today)

    headers = {'User-Agent': 'Mozilla/5.0','content-type':'application/json; charset=UTF-8'}
    data = '{"serviceId":"99","position":{"latitude":38.1495841,"longitude":-85.8793252},"appointmentAvailability":{"startDateTime":"' + today + '"},"radius":25}'
    # print(data)
    r = requests.post(urlWalgreens, headers=headers, data = data)
    # print(r.text)
    json_data = json.loads(r.text)
    print(json_data["appointmentsAvailable"])
    return json_data["appointmentsAvailable"]


def SendEmail():
    
    receiver = "eri*@gmail.com"

    print("Emailing results table to: " + receiver)
    yag = yagmail.SMTP("eao*@gmail.com",'*')
    yag.send(
    to=receiver,
    subject="Louisville Walgreens are taking COVID appointments"
    )



isTakingAppointments = CallWalgreens()        
isTakingAppointments = True
if(isTakingAppointments == True):
    SendEmail()