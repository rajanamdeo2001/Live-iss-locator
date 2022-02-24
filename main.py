import json, urllib.request, datetime, geocoder

Timestamp = datetime.datetime.now()

url = "http://api.open-notify.org/astros.json"
response = urllib.request.urlopen(url)
result = json.loads(response.read())
file = open("iss.text" ,"w")
file.write("\n- - - - - - - - - Complete detail about ISS - live - - - - - - - -\n\n\n")
file.write("Current time is : " + str(Timestamp) + "\n\n")
file.write("There is currently " + str(result["number"]) + " astronauts on the ISS : \n\n")
people = result["people"]
for p in people:
    file.write(p['name'] + " - on board" + "\n")

url = "http://api.open-notify.org/iss-now.json"
response = urllib.request.urlopen(url)
result = json.loads(response.read())  
#extract the iss location
location = result["iss_position"]
lat = location['latitude']
lon = location['longitude']
#Output lon and lat to the terminal
#lat = float(lat)
#lon = float(lon)
file.write("\nISS current latitude and lognitude is [" + lat + ", " + lon + "]")


g = geocoder.ip('me')
file.write("\nYour current latitude and longitude is : " + str(g.latlng) + "\n\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  ")
file.close()