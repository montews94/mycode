#!/usr/bin/env python3

## get your monsters data to get ready to duel

import csv


## create file object in "r"ead mode
with open("carddata.csv", "r") as duelmonsters:
    ## use csv.DictReader() tom make dictionary
    duelmonsterlist = csv.DictReader(duelmonsters)
    
## now let player know only his monster card attack and defense stats
    print("Here are your monster cards Attack and Defense points: \n")
    ## for loop to read through each row
    for row in duelmonsterlist:
        if row["ATK"] != "":
            print(f'{row["Name"]} has {row["ATK"]} attack points {row["DEF"]} defense points')
    print("\n It's time to D-D-Duel!")
