def extract_info(hospital_list):
    result = []
    for hospital in hospital_list :
        info_table = hospital.find_all("td")
        city = info_table[0].string
        town = info_table[1].string
        hospital_name = info_table[2].contents[0]
        phone_number = info_table[3].string

        hospital_info = {
            "city" : city,
            "town" : town,
            "hospital_name" : hospital_name,
            "phone_number" : phone_number,
        }
        result.append(hospital_info)
    return result