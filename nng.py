import requests
import json
import time


GOOGLE_API_KEY = '-'
address = input("輸入地址：")

def get_latitude_longtitude(address):
    # decode url
    
    url = "https://maps.googleapis.com/maps/api/geocode/json?address=" + address + '&key=' + GOOGLE_API_KEY
    
    while True:
        res = requests.get(url)
        js = json.loads(res.text)
        if js["status"] != "OVER_QUERY_LIMIT":
            time.sleep(1)
            break
    result = js["results"][0]["geometry"]["location"]
    #print(latitude,longitude)
    lat = result["lat"]
    lng = result["lng"]
    print(lat,lng)
    return (lat , lng)


while (address != 'q'):
    get_latitude_longtitude(address)
    address = input("輸入地址：(輸入'q'退出)")
exit()