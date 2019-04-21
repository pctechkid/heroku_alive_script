import requests
from pytz import timezone
import datetime
import logging

FORMAT = '%(process)d-%(levelname)s-%(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)

logger = logging.getLogger()

tz = timezone('EST')

hour = datetime.datetime.now(tz).hour
if hour < 9 or hour > 21:
    logger.info("exiting cause not in daytime")
    exit(0)

links = ["https://krishnakaranam.herokuapp.com/",
         "https://react-googlemaps.herokuapp.com/",
         "https://persistent-hangman-ui.herokuapp.com/"]

for each in links:
    try:
        page = requests.get(each)
        print("First try:", page.status_code)
        logger.info("First try: %s", str(page.status_code))
        if page.status_code != 200:
            page = requests.get(each)
            print("retry:", page.status_code)
            logger.info("retry: %s", str(page.status_code))
    except Exception as e:
        print(e)
        print("tried link: ", each)
        logger.info("Exception: %s", str(e))
