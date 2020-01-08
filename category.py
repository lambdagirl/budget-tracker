import csv;
import sys;
def boa_csv(filename):
    card_ending=filename[-8:-4]
    results = []
    with open(filename,'r') as csvinput:
        with open('output.csv', 'w') as csvoutput:
            writer = csv.writer(csvoutput, lineterminator='\n')
            reader = csv.reader(csvinput)


            all = []
            row = next(reader)
            row.append('Category')
            all.append(row)

            for row in reader:
                row.append(to_category(row[2]))
                all.append(row)

            writer.writerows(all)

        # for row in reader:
        #     results.append(row)
        #     print(to_category(row["Payee"]),row["Payee"],"BOA-"+card_ending)

def to_category(description):
    dic={
    "Merchandise & Supplies-Groceries" : ["SAFEWAY","SUPERMARKET","WHOLEFOODS","MARKET","HELLOFRESH","WAL-MART","DAISO","JL PRODUCE","99 RANCH","ROSS STORES","7-ELEVEN","MITSUWA","MARSHALLS","WHOLEFDS"],
    "Dinning":["IN N OUT BURGER","MAISON ALYZEE","PARIS BAGUETTE","K-POT & GRILL","GRILL","RAMEN","HOUSE","CRAB"],
    "Coffee":["PEET'S","STARBUCKS","COFFEE","SUBWAY","CHIPOTLE","THAI","CAFFE","HUNAN"],
    "Transportation":["VALERO","CARNICERIA","UBER","LYFT"],
    "Pets" : ["CHEWY","PETCO","ANIMAL"],
    "Clothing" :["ASOS","ZARA","NIKE","HM","ConverseUS","PATAGONIADIRECTINC","UNDER ARMOUR DIRECT","EASY SPIRIT","MACY","UNIQLO","GUCCI"],
    "Skin Care" : ["CLINIQUE","SHISEIDO","SEPHORA","NORDSTROM"],
    "Babys" :["TARGET","BABIES","CARTERS","THE HONEST COMPANY"],
    "Laundry":["WASH"],
    "Mobil":["AT&T","VZWRLS","TELE"],
    "Fitness":["GYM","MARATHONPHOT","RACE CENTRAL"],
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
    
boa_csv("December2019_7810.csv")