from urllib.request import urlopen
from bs4 import BeautifulSoup

url303 = "http://www.daelim.ac.kr/hme/stu_service/prg/stu_cafeteria.do?reg_week_year=46&cafe_cd=139"

html = urlopen(url303).read()
soup = BeautifulSoup(html, "html.parser")
table_meal = soup.find("table", class_="table_col mt_30 ml_22")

tr_corner = table_meal.find_all("tr")

for i in range(5):
    if i == 0:
        print("/* 월요일 */")
    elif i == 1:
        print("/* 화요일 */")
    elif i == 2:
        print("/* 수요일 */")
    elif i == 3:
        print("/* 목요일 */")
    elif i == 4:
        print("/* 금요일 */")
    for j in range(9):
        content = tr_corner[j + 1].find_all("td")
        if j == 0:
            currentCorner = content[1]
            td_meal = content[i + 2]
        else:
            currentCorner = content[0]
            td_meal = content[i + 1]
        print(currentCorner.text, ": ", end="")
        print(td_meal.text.strip())
    print("")