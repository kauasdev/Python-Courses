# import requests
#
# try:
#     requests.get("http://pudim.com.br/").status_code
# except requests.exceptions.ConnectionError:
#     print("Unable to access 'pudim.com.br' website")
# except Exception as error:
#     print(error.__class__)
# else:
#     print("The 'pudim.com.br' website is available!")

import urllib
from urllib import request, error

site = "http://pudim.com.br/"

try:
    website = urllib.request.urlopen(site)
except urllib.error.URLError:
    print(f"Unable to access '{site}' website")
except Exception as error:
    print(error.__class__)
else:
    print(f"The '{site}' website is available!")
