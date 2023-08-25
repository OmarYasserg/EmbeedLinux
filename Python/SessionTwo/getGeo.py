import webbrowser
import requests

r = requests.get("https://api.ipify.org/?format=json")
ipAddress = r.json()["ip"]

# Geo = requests.get
# print("https://ipinfo.io/"+ str(ipAddress) +"/geo")

ActivityReq = requests.get("https://www.boredapi.com/api/activity")

CurrentActivity = ActivityReq.json()["activity"]

print(CurrentActivity)