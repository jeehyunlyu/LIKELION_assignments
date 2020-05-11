import requests
from bs4 import BeautifulSoup
from hospital import extract_info
import csv

hospital_html = requests.get('https://www.mohw.go.kr/react/popup_200128_3.html')
hospital_html.encoding = 'utf-8'
hospital_soup = BeautifulSoup(hospital_html.text, "html.parser")
hospital_list_box = hospital_soup.find("tbody", {"class" : "tb_center"}) 
hospital_list = hospital_list_box.find_all("tr")

file = open("corona_hospital.csv", mode="w", newline="")
writer = csv.writer(file)
writer.writerow(["city", "town", "hospital_name", "phone_number"])

final_result = []
final_result += extract_info(hospital_list)

for result in final_result:
    row = []
    row.append(result["city"])
    row.append(result["town"])
    row.append(result["hospital_name"])
    row.append(result["phone_number"])
    
    writer.writerow(row)

print("크롤링 끝!")
print(final_result)

