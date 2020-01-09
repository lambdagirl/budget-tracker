import csv;
import sys;
import os
# os.chdir("boa")

def boa_csv(filename):
    card_ending=filename[-8:-4]
    with open(filename,'r') as csvinput:
        with open('new_'+filename, 'w') as csvoutput:
            writer = csv.writer(csvoutput, lineterminator='\n')
            reader = csv.reader(csvinput)
            all = []
            header = ['Post Date','Amount', 'Description','Category',"Account"]
            all.append(header)
            row = next(reader)
            for row in reader:
                row[4]=-float(row[4])
                row.append(to_category(row[2]))
                row.append("BOA_"+card_ending)
                all.append([row[0],row[4],row[2],row[5],row[6]])
            writer.writerows(all)

def chase_csv(filename):
    card_ending=filename[0:9]
    with open(filename,'r') as csvinput:
        with open('new_'+filename, 'w') as csvoutput:
            writer = csv.writer(csvoutput, lineterminator='\n')
            reader = csv.reader(csvinput)
            all = []
            header = ['Post Date','Amount', 'Description','Category',"Account"]
            all.append(header)
            row = next(reader)
            for row in reader:
                row[5]=-float(row[5])
                row[3]=(to_category(row[2]))
                row.append(card_ending)
                all.append([row[0],row[5],row[2],row[3],row[6]])
            writer.writerows(all)


def ae_csv(filename):
    with open(filename,'r') as csvinput:
        with open('new_'+filename, 'w') as csvoutput:
            writer = csv.writer(csvoutput, lineterminator='\n')
            reader = csv.reader(csvinput)
            all = []
            #Date,Reference,Description,Card Member,Card Number,Amount,Category,Type
            header = ['Post Date','Amount', 'Description','Category',"Account"]
            all.append(header)
            row = next(reader)
            for row in reader:
                row[6]=(to_category(row[2]))
                all.append([row[0],row[5],row[2],row[6],"AE"+row[4]])
            writer.writerows(all)
def to_category(description):
    dic={
    "Groceries" : ["SAFEWAY","SUPERMARKET","WHOLEFOODS","MARKET","HELLOFRESH","WAL-MART","DAISO","JL PRODUCE","99 RANCH","ROSS STORES","7-ELEVEN","MITSUWA","MARSHALLS","WHOLEFDS"],
    "Dinning Out":["IN N OUT BURGER","MAISON ALYZEE","PARIS BAGUETTE","K-POT & GRILL","GRILL","RAMEN","HOUSE","CRAB","DENNY'S","HUNAN","MCDONALD'S"],
    "Coffee":["PEET'S","STARBUCKS","COFFEE","SUBWAY","CHIPOTLE","THAI","CAFFE","TEA","JAMBA JUICE","PEETS"],
    "Transportation":["VALERO","CARNICERIA","UBER","LYFT","TOLL","76"],
    "Pets" : ["CHEWY","PETCO","ANIMAL"],
    "Clothes" :["ASOS","ZARA","NIKE","HM","ConverseUS","PATAGONIADIRECTINC","UNDER ARMOUR DIRECT","EASY SPIRIT","MACY","UNIQLO","GUCCI","LEVI'S","SHOES"],
    "Skin Care" : ["CLINIQUE","SHISEIDO","SEPHORA","NORDSTROM"],
    "Babys" :["TARGET","BABIES","CARTERS","THE HONEST COMPANY"],
    "Laundry":["WASH"],
    "Mobil":["AT&T","VZWRLS","TELE"],
    "Fitness":["GYM","MARATHONPHOT","RACE CENTRAL","SPORTS"],
    "Travel":["FIRESIDE LODGE","HOTEL"],
    "Furniture":["IKEA","WAYFAIR"],
    "Subscription":["WIX","GODADDY","MICROSOFT","TREEHOUSE"],
    "Medical":["WALGREENS","CVS"],
    "Online shopping" :["WWW","COM","PAYPAL","ONLINE","AMZN","GROUPON"],
    "Entertain":["WALL-ST-JOURNAL"],
    "Credit":["THANK YOU","CREDIT"]
    }
    for k,v in dic.items():
        for i in v:
            if i in description.upper():
                return k
    
ae_csv("ae.csv")
boa_csv("December2019_7810.csv")
boa_csv("January2020_0673.csv")
chase_csv("Chase1908_Activity20200108.csv")