# MY OBJECTIVE:
# To find restaurants in the 10001, 10011, and 10014 zip codes of Manhattan that serve alcohol and have
# outdoor sidewalk seating and map them.

# ABOUT THIS DATA:
# NYC Open Data Open Restaurant Applications:
# https://data.cityofnewyork.us/Transportation/Open-Restaurant-Applications/pitm-atqc
# is a dataset of applications from food service establishments seeking authorization to re-open
# under Phase Two of the State’s New York Forward Plan, and place outdoor seating in front of 
# their business on the sidewalk and/or roadway.

# API details: https://dev.socrata.com/foundry/data.cityofnewyork.us/pitm-atqc
# You must sign up for an app token at this website, and once you have an app token,
# you can include it with your request either by using the X-App-Token HTTP header, 
# or by passing it via the $$app_token parameter on your URL

# METHOD:
# 1) I used my python script, nyc_open_rests_api.py, to make an API call to 
# https://data.cityofnewyork.us/resource/pitm-atqc.json?$$app_token=[ENTER_APP_TOKEN] for zip codes 10001, 
# 10011, and 10014, which created a # json file, nyc_open_rests_2.json
# 2) Then, I used the python script, json_to_csv.py, to pull just the restaurant names and their 
# respective addresses from the json file and write it all into a csv file
# 3) Then, I used my R script, geocode_nyc_rests_10001.R, to geocode all the locations into latitudes 
# and longitudes and create a csv file, w_village_10014_rests_w_lats_longs
# 4) Then, I brought the file into OpenRefine and fixed issues with the addresses. See below under 
# "ISSUES" for all instances that required editing. 
# 5) Then, I combined all data from all three zip codes into one csv file by copy and pasting, and 
# went line by line and deleted restaurants that were permanently closed as well as duplicate addresses
# 6) Then, I imported the file into Tableau Public and created a map: 
# https://public.tableau.com/app/profile/sara.kim3820/viz/NearbyRestaurantswOutdoorSeatingAlcohol/100011001110014. Only certain restaurant names appear 
# initially when zoomed out and more show up as you zoom in. It's best to click on each dot to 
# see the restaurant name and address

# ISSUES
# Data had to be cleaned for 
# 1) incorrect addresses, such as some whose street number appear twice as in "12 12 32nd St" 
# instead of "12 43nd St"
# 2) lack of "E" (East) or "W" (West) before the street name
# 3) lack of "St" or "Ave" at the end of the address
# 4) Spacing issues within the address such as "2W 32nd St" instead of "2 W 32nd St"
# 5) duplicate entries, such as Hanbat Restaurant's appearing twice
# 4) permanently closed restaurants

### Pretty cool up-to-date open restaurants dashboard: https://experience.arcgis.com/experience/ba953db7d541423a8e67ae1cf52bc698
