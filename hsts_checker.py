import requests

def main():
	check_sts()

def check_sts():
	url = raw_input("Please enter the URL you wish to check: ")
	#url = "https://preload.mbproject.pw"
	response = requests.get(url)

	print("Results for:", url)

	#Check for presence of strict-transport-security response header
	if 'strict-transport-security' in response.headers:
		print("HSTS header present")
		hsts_present = True
	else:
		print("HSTS header not present")
		hsts_present = False

	#If sts header found, check for preload flag
	if hsts_present == True:
		if 'preload' in response.headers['strict-transport-security']:
			print("Preload flag present")
		else:
			print("Preload flag not present")
	else:
		None
	
	#If sts header found, check for includeSubdomains flag
	if hsts_present == True:
		if 'includeSubDomains' in response.headers['strict-transport-security']:
			print("Include SubDomains flag present")
		else:
			print("Include SubDomains flag not present")
	else:
		None
main()