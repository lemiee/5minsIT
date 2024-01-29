from requests import get

#Taking notes of for, formatting, request
websites = (
    "google.com",
    "naver.com",
    "nexon.com",
    "facebook.com"
)

results = {}

for website in websites:
    if not website.startswith("https://"):
        website = f"https://{website}"
    response = get(website)
    print(response.status_code)
    #URL formatting
    if response.status_code == 200:
        print(f"{website} is OK")
        results[website] = "OK"
    elif response.status_code == 304:
        print(f"{website} is not an error")
        results[website]="REDIRECTED"
    else:
        print(f"{website} is wrong")
        results[website]="ERROR"

print(results)

#pypi.org provides pacakges not in python
#requests - send request to a website for your py code
# pip install requests -> import requests
    
