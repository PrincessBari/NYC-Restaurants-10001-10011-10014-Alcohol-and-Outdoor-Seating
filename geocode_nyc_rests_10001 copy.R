library(dplyr)
library(tidyverse)
library(plyr)
library(ggmap) #Google's Terms of Service: https://cloud.google.com/maps-platform/terms/.
#Please cite ggmap if you use it! See citation("ggmap") for details

rests_10014 <- read.csv("[ENTER FULL FILE PATH]/w_village_rests_alkie_outdoor_seating_10014 - duplicates and closed removed.csv", header=TRUE)
head(rests_10014)
nrow(rests_10014) #210
(colnames(rests_10014))
# [1] name"    "address"

register_google(key = "[ENTERED REGISTERED API KEY]")
??mutate_geocode
lat_longs_rests_10014 <- mutate_geocode(rests_10014, address)
head(lat_longs_rests_10014)
nrow(lat_longs_rests_10014)

write.csv(lat_longs_rests_10014, "[ENTERED DESIRED FILE PATH]/w_village_10014_rests_w_lats_longs.csv", row.names = FALSE)

