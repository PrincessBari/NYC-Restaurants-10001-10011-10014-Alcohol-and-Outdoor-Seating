import requests
import json

# You must sign up for an NYC Open Data app token at https://dev.socrata.com/foundry/data.cityofnewyork.us/pitm-atqc
base_url = "https://data.cityofnewyork.us/resource/pitm-atqc.json?$$app_token=[ENTER_APP_TOKEN]"

payload = {
	"borough": "Manhattan",
	"approved_for_sidewalk_seating": "yes",
	"qualify_alcohol": "yes",
	"zip" : "10001"
}

save_data = []

r = requests.get(base_url, params = payload)

data = json.loads(r.text)

for item in data:
	save_data.append(item)
	print(item["restaurant_name"])
	print(item["business_address"] + "\n")

with open ('nyc_open_rests_2.json', 'w') as out:
	json.dump(save_data, out, indent = 2)

# DATA STRUCTURE:
#[
#    {
#        "objectid": "7068",
#        "globalid": "{AD9D205E-C143-4402-837C-BEDFC1CF4407}",
#        "seating_interest_sidewalk": "sidewalk",
#        "restaurant_name": "El Ancla Restaurant Bar",
#        "legal_business_name": "El Ancla de Astoria Restaurant & Bar Inc.",
#        "doing_business_as_dba": "El Ancla de Astoria Restaurant & Bar Inc.",
#        "bulding_number": "28-08",
#        "street": "21st  street",
#        "borough": "Queens",
#        "zip": "11102",
#        "business_address": "28-08 21st  street, Queens, NY",
#        "food_service_establishment": "41682958",
#        "sidewalk_dimensions_length": "23",
#        "sidewalk_dimensions_width": "8",
#        "sidewalk_dimensions_area": "184",
#        "approved_for_sidewalk_seating": "yes",
#        "approved_for_roadway_seating": "no",
#        "qualify_alcohol": "yes",
#        "sla_serial_number": "Jan-81",
#        "sla_license_type": "OP",
#        "landmark_district_or_building": "no",
#        "healthcompliance_terms": "yes",
#        "time_of_submission": "2020-07-02T22:08:00.000",
#        "latitude": "40.770914",
#        "longitude": "-73.927003",
#        "community_board": "1",
#        "council_district": "22",
#        "census_tract": "83",
#        "bin": "4006070",
#        "bbl": "4005380043",
#        "nta": "Old Astoria"
#    },