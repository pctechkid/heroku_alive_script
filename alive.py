import requests


links = ["https://krishnakaranam.herokuapp.com/"]

for each in links:
    try:
        page = requests.get(each)
        print(page.status_code)
    except Exception as e:
        print(e)
        print("tried link: ", each)
