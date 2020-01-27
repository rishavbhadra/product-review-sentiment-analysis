# importing csv module 
import csv
import re
from textblob import TextBlob

def analys(x):
    analysis = TextBlob(x) 
        # set sentiment 
    if analysis.sentiment.polarity > 0: 
        return 2
    elif analysis.sentiment.polarity == 0: 
        return 1
    else: 
        return 0
  
# csv file name 
filename = "amazonreviews.csv"
  
# initializing the titles and rows list 
fields = [] 
rows = [] 
  
# reading csv file 
with open(filename, 'r') as csvfile: 
    # creating a csv reader object 
    csvreader = csv.reader(csvfile) 
    for row in csvreader: 
        rows.append(row) 
p_rev=0
n_rev=0
ne_rev=0
for row in rows[:]: 
    # parsing each column of a row 
    for col in row: 
        if(analys(col)==2):
            p_rev+=1
        elif(analys(col)==1):
            ne_rev+=1
        else:
            n_rev+=1
tot=p_rev+n_rev+ne_rev
prev=(p_rev/tot)*100
nrev=(n_rev/tot)*100
nerev=(ne_rev/tot)*100
print("positive review: "+str(p_rev)+" percentage= "+str(prev),end="\n")
print("negative review: "+str(n_rev)+" percentage= "+str(nrev),end="\n")
print("neutral review: "+str(ne_rev)+" percentage= "+str(nerev),end="\n")

