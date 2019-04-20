import requests
import datetime

hour = datetime.datetime.now().hour
if hour < 8 or hour > 21:
    exit(0)

links = ["https://krishnakaranam.herokuapp.com/"]

for each in links:
    try:
        page = requests.get(each)
        print("First try:", page.status_code)
        if page.status_code != 200:
            page = requests.get(each)
            print("retry:", page.status_code)
    except Exception as e:
        print(e)
        print("tried link: ", each)
