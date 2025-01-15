import re
import requests
from bs4 import BeautifulSoup
s = 0

for i in range(1,1213):
    task = "https://robocontest.uz/tasks/" + str(i).zfill(4)
    response = requests.get(task)

    soup = BeautifulSoup(response.text, 'html.parser')

    span_text = soup.find('span', {'id': 'complexity_info'}).text
    x = re.findall(r'\d+', span_text)[0]
    s += int(x)

    print(span_text,x)
print(s)