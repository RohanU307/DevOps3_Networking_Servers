import requests
domain = "google.com"

filename= "subdomains.txt"
with open(filename, "r") as file:
    for subdomain in file.readlines():
        # define subdomain url
        subdomain_url = f"https://{subdomain.strip()}.{domain}"
        try:
            response = requests.get(subdomain_url)
            
            #200 success code
            if response.status_code==200:
                print(f"Subdomain Found [+]: {subdomain_url}")

        except:
            pass  