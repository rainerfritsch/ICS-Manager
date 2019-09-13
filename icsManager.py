# ICS Manager
# seperate calendar File according to categories
# create new file for every category
#
# Autor: Rainer Fritsch
# Date: 2019-07-22

import os

filename="C:/calendar.ics"
newEvent=False
category=""
event=""
outfile=""

with open(filename) as f:
    lines = f.readlines()

files = set()

for l in lines:
    if newEvent:
        event=event+l
        if l.startswith("CATEGORIES"):
            category=l.strip().split(':')[1]
        if l.startswith("END:VEVENT"):

            outfile=filename[:-4]+'-'+category+'.ics'
            if not os.path.isfile(outfile):
                with open(outfile,"a") as file:
                    file.write('BEGIN:VCALENDAR \n')
                    files.add(outfile)
            with open(outfile, "a") as myfile:
                myfile.write(event)
            event=""
            newEvent=False
    if l.startswith("BEGIN:VEVENT"):
        newEvent=True
        category="standard"
        event=event+l

for filename in files:
    with open(filename, "a") as file:
        file.write('END:VCALENDER')
