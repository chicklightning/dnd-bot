import requests
from bs4 import BeautifulSoup


query = "brew+potion+d20pfsrd"
goog_search = "https://www.google.co.uk/search?sclient=psy-ab&client=ubuntu&hs=k5b&channel=fs&biw=1366&bih=648&noj=1&q=" + query


r = requests.get(goog_search)

soup = BeautifulSoup(r.text, "html.parser")


print(soup.find("cite").text)

