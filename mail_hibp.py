import requests
from email.utils import parseaddr

def Check(account):
	headers = {
		'User-Agent':'Pwnage-Checker-For-Python',
		"Accept": "application/vnd.haveibeenpwned.v2+json"
	}
	r = requests.get("https://haveibeenpwned.com/api/v2/breachedaccount/{0}".format(account),headers=headers)
	names = {}
	if not r.status_code == 200:
		return False
	json = r.json()
	for i in range(len(json)):
		names[json[i]["Name"]] = json[i]["BreachDate"]
	return names

a = input("-> ")
liste = []
a = a.replace("\n"," ")
for i in a.split(","):
	r = parseaddr(i)
	if r[1] != "":
		liste.append(r)
for n in liste:
	print("Checking ", str(n[0]))
	che = Check(str(n[1]))
	if che != False:
		print(" > Results for ",str(n[1]),": \n",che,"\n")
