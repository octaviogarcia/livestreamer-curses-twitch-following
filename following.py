__author__ = 'octavio'
import json
import requests
import sys
if __name__=='__main__':
	if(len(sys.argv)==1):
		print("Usage: python following.py <your_username>, without the <>")
		exit()
	url = "https://api.twitch.tv/kraken/users/"+sys.argv[1]+"/follows/channels"
	headers = {"Accept": "application/vnd.twitchtv.v3+json"}
	headers["limit"]="100"
	headers["offset"]="0"
	channels=[]
	while(True):
		req = requests.get(url,headers)
		json = req.json()
		if(len(json["follows"]) == 0):
			break
		for i in json["follows"]:
			channel_name=i["channel"]["name"]
			channels.append(channel_name)
		headers["offset"]=str(int(headers["offset"])+100)

	idd=1
	print("[")
	print('{','"last_seen":',0,', "online":',0,', "name":','"'+channels[0]+'"',', "res":','"source"',', "seen":',0,', "id":',idd,', "url":',('"twitch.tv/'+channels[0]+'"'),'}')
	idd+=1
	for i in channels[1:]:
		print(',')
		print('{','"last_seen":',0,',"online":',0,', "name":','"'+i+'"',', "res": ','"source"',', "seen":',0,', "id":',idd,', "url":',('"twitch.tv/'+i+'"'),'}')
		idd+=1
	print("]")
