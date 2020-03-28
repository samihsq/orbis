import pandas as pd
from textblob import TextBlob
import datetime
from samplebase import SampleBase
import os
import sys
from rgbmatrix import RGBMatrix, RGBMatrixOptions



numbers = []
store = []
place = []
dict = []
full = []
filetime = []

NA = []
NAsent = None
NAnumbers = []

SA = []
SAsent = None
SAnumbers = []

EU = []
EUsent = None
EUnumbers = []

AF = []
AFsent = None
AFnumbers = []

AS = []
ASsent = None
ASnumbers = []

OC = []
OCsent = None
OCnumbers = []

AN = []
ANsent = None
ANnumbers = []

inc = 0
# global d
d = datetime.datetime.today()
now = datetime.datetime.now()
hr = now.hour
minu = now.minute
inthr = int(hr)
intmin = int(minu)
done = 0
print(os.listdir("twitter-data"))

# while done == 0:
#     while inthr >= 0:
#         try:
#
#             time = os.path.getmtime('twitter_data-'+ str(d.strftime('%m')) + '-' + str(d.strftime('%d')) + '-' + str(d.strftime('%y'))
#                                     + '-' + str(hr) + ':' + str(minu) + '.json')
#             # print(time)
#             # filetime.append(time)
#             filetime.append('twitter_data-'+ str(d.strftime('%m')) + '-' + str(d.strftime('%d')) + '-' + str(d.strftime('%y'))
#                                     + '-' + str(hr) + ':' + str(minu) + '.json')
#             hr = int(hr)
#             done = 1
#
#         except:
#             inthr = int(hr)
#             minu = int(minu)
#             hr = int(hr)
#             minu -= 1
#             intmin = int(minu)
#             if intmin < 0:
#                 minu = 60
#                 hr -= 1
#             if hr < 10:
#                 hr = str(0) + str(hr)
#             if minu < 10:
#                 minu = str(0) + str(minu)
#             if hr and minu == '00':
#                 break
#              print('twitter_data-' + str(d.strftime('%m')) + '-' + str(d.strftime('%d')) + '-' + str(d.strftime('%y')) + \
#              '-' + str(hr) + '.json')
#              print(hr)
#              if hr <= 0:
#                 sys.exit()

# print(filetime)

while done == 0:
    try:
        # yinput = input("Year please")
        Minput = input("zero padded month please: ")
        dinput = input("zero padded day please: ")
        hinput = input("zero-padded hour please: ")
        minput = input("zero-padded minute please: ")
        debug = input("debug(y/n): ")

        name = 'twitter-data/twitter_data-' + Minput + '-' + dinput + '-' + str(d.strftime('%y')) +\
               '-' + hinput + ':' + minput + '.json'

        global customers_json
        customers_json = pd.read_json(name, lines=True)


        done = 1
    except ValueError:
        print("Please put in correct values \n")


x = 0
g = 0
# print(list(customers_json))
# print(customers_json.at[1, 'text'])

# print(x)


# customers_json = pd.read_json(name, orient="records")
# with open(name, 'r') as customers_json:
amt = customers_json.shape[0]
for y in range(amt):

    z = customers_json.at[y, 'place']
    # ext = customers_json.at[y, 'extended_tweet']
    if not z:
        continue
    else:
        place.insert(g, z)
        place = list(filter(None, place))
# for h in range(g):
        n = place[g]
        # j = ext
        if n != n:
            continue

        else:
            # j = ext[g]
            CC = [n.get('country_code')]
            # text = [j.get('full_text')]
            # twit_text =
            dict.append(CC)
            sent = TextBlob(str(customers_json.at[y, 'text'])).sentiment.polarity
            text = str(customers_json.at[y, 'text'])
            sent = round(sent, 3)
            numbers.append(sent)
            store.append(CC)
            store.append(sent)
            store.append(text)
            if CC in (['BS'],['BB'],['BM'],['CA'],['CR'],['CU'],['DO'],['SV'],['GL'],['GT'],['HT'],['HN'],['JM'],['MX'],['NI'],['PA'],['PR'],['TT'],['US']):
                NAnumbers.append(sent)
                NA.append(store)
            if CC in (['AR'],['BO'],['BR'],['CL'],['CO'],['EC'],['FK'],['GF'],['GY'],['PY'],['PE'],['SR'],['UY'],['VE']):
                SAnumbers.append(sent)
                SA.append(store)
            if CC in (['AL'],['AD'],['AT'],['BY'],['BE'],['BA'],['BG'],['HR'],['CY'],['CZ'],['DK'],['EE'],['FI'],['FR'],['DE'],['GI'],['GR'],['HU'],['IS'],['IE'],['IT'],['LV'],['LI'],['LT'],['LU'],['MK'],['MD'],['MC'],['ME'],['NL'],['NO'],['PL'],['PT'],['RO'],['RU'],['SM'],['RS'],['SK'],['SI'],['ES'],['SE'],['CH'],['UA'],['GB'],['VA'],['RS']):
                EUnumbers.append(sent)
                EU.append(store)
            if CC in (['DZ'],['AO'],['SH'],['BJ'],['BW'],['BF'],['BI'],['CM'],['CV'],['CF'],['TD'],['KM'],['CG'],['CD'],['DJ'],['EG'],['GQ'],['ER'],['SZ'],['ET'],['GA'],['GM'],['GH'],['GN'],['GW'],['CI'],['KE'],['LS'],['LR'],['LY'],['MG'],['MW'],['ML'],['MR'],['MU'],['YT'],['MA'],['MZ'],['NA'],['NE'],['NG'],['ST'],['SN'],['SC'],['SL'],['SO'],['ZA'],['SS'],['SH'],['SD'],['SZ'],['TZ'],['TG'],['TN'],['UG'],['CD'],['ZM'],['TZ'],['ZW']):
                AFnumbers.append(sent)
                AF.append(store)
            if CC in (['AF'],['AM'],['AZ'],['BH'],['BD'],['BT'],['BN'],['KH'],['CN'],['CX'],['CC'],['IO'],['GE'],['HK'],['IN'],['ID'],['IR'],['IQ'],['IL'],['JP'],['JO'],['KZ'],['KW'],['KG'],['LA'],['LB'],['MO'],['MY'],['MN'],['MM'],['NP'],['KP'],['OM'],['PK'],['PS'],['PH'],['QA'],['SA'],['SG'],['KR'],['LK'],['SY'],['TW'],['TJ'],['TH'],['TR'],['TM'],['AE'],['UZ'],['VN'],['YE']):
                ASnumbers.append(sent)
                AS.append(store)
            if CC in (['AS'],['AU'],['NZ'],['CK'],['TL'],['FM'],['FJ'],['PF'],['GU'],['KI'],['MP'],['MH'],['UM'],['NR'],['NC'],['NZ'],['NU'],['NF'],['PW'],['PG'],['MP'],['WS'],['SB'],['TK'],['TO'],['TV'],['VU'],['UM'],['WF']):
                OCnumbers.append(sent)
                OC.append(store)
            if CC == ['AQ']:
                ANnumbers.append(sent)
                AN.append(store)
            full.append(store)
            store = []
            # print(full[g])
            g += 1

def colorcalc():
    if not NAnumbers:
        NA_avg_sent = 0
    else:
        NA_avg_sent = round(sum(NAnumbers)/len(NAnumbers), 3)
    print()
    print("North America")
    if NA_avg_sent > 0.0:
        NAcolor = "0,255,0"
    elif NA_avg_sent < 0.0:
        NAcolor = "255,0,0"
    else:
        NAcolor = "211,211,211"
    if debug == "y":
        print(NA)
    else:
        pass
    print(NA_avg_sent)
    print(NAcolor)

    if not SAnumbers:
        SA_avg_sent = 0
    else:
        SA_avg_sent = round(sum(SAnumbers)/len(SAnumbers), 3)
    print()
    print("South America")
    if SA_avg_sent > 0.0:
        SAcolor = "0,255,0"
    elif SA_avg_sent < 0.0:
        SAcolor = "255,0,0"
    else:
        SAcolor = "211,211,211"
    if debug == "y":
        print(SA)
    else:
        pass
    print(SA_avg_sent)
    print(SAcolor)


    if not EUnumbers:
        EU_avg_sent = 0
    else:
        EU_avg_sent = round(sum(EUnumbers)/len(EUnumbers), 3)
    print()
    print('Europe')
    if EU_avg_sent > 0.0:
        EUcolor = "0,255,0"
    elif EU_avg_sent < 0.0:
        EUcolor = "255,0,0"
    else:
        EUcolor = "211,211,211"
    if debug == "y":
        print(EU)
    else:
        pass
    print(EU_avg_sent)
    print(EUcolor)

    if not AFnumbers:
        AF_avg_sent = 0
    else:
        AF_avg_sent = round(sum(AFnumbers)/len(AFnumbers), 3)
    print()
    print('Africa')
    if AF_avg_sent > 0.0:
        AFcolor = "0,255,0"
    elif AF_avg_sent < 0.0:
        AFcolor = "255,0,0"
    else:
        AFcolor = "211,211,211"
    if debug == "y":
        print(AF)
    else:
        pass
    print(AF_avg_sent)
    print(AFcolor)

    if not ASnumbers:
        AS_avg_sent = 0
    else:
        AS_avg_sent = round(sum(ASnumbers)/len(ASnumbers), 3)
    print()
    print('Asia')
    if AS_avg_sent > 0.0:
        AScolor = "0,255,0"
    elif AS_avg_sent < 0.0:
        AScolor = "255,0,0"
    else:
        AScolor = "211,211,211"
    if debug == "y":
        print(AS)
    else:
        pass
    print(AS_avg_sent)
    print(AScolor)

    if not OCnumbers:
        OC_avg_sent = 0
    else:
        OC_avg_sent = round(sum(OCnumbers)/len(OCnumbers), 3)
    print()
    print('Australia and Oceania')
    if OC_avg_sent > 0.0:
        OCcolor = "0,255,0"
    elif OC_avg_sent < 0.0:
        OCcolor = "255,0,0"
    else:
        OCcolor = "211,211,211"
    if debug == "y":
        print(OC)
    else:
        pass
    print(OC_avg_sent)
    print(OCcolor)

    if not ANnumbers:
        AN_avg_sent = 0
    else:
        AN_avg_sent = round(sum(ANnumbers)/len(ANnumbers), 3)
    print()
    print('Antarctica')
    if AN_avg_sent > 0.0:
        ANcolor = "0,255,0"
    elif AN_avg_sent < 0.0:
        ANcolor = "255,0,0"
    else:
        ANcolor = "211,211,211"
    if debug == "y":
        print(AN)
    else:
        pass
    print(AN_avg_sent)
    print(ANcolor)
    
colorcalc()

print()
try:
    print("Avg sent: " + str(round(sum(numbers)/len(numbers), 3)))
except ZeroDivisionError:
    print("Avg sent: 0")

options = RGBMatrixOptions()
options.rows = 32
options.chain_length = 2
options.hardware_mapping = 'adafruit-hat'
matrix = RGBMatrix(options = options)

class SimpleSquare(SampleBase):
    def __init__(self, *args, **kwargs):
        super(SimpleSquare, self).__init__(*args, **kwargs)

    def run(self):
        offset_canvas = self.matrix.CreateFrameCanvas()
        while True:
            for x in range(0, self.matrix.width):
                offset_canvas.SetPixel(x, x, 255, 255, 255)
                offset_canvas.SetPixel(offset_canvas.height - 1 - x, x, 255, 0, 255)

            for x in range(0, offset_canvas.width):
                offset_canvas.SetPixel(x, 0, 255, 0, 0)
                offset_canvas.SetPixel(x, offset_canvas.height - 1, 255, 255, 0)

            for y in range(0, offset_canvas.height):
                offset_canvas.SetPixel(0, y, 0, 0, 255)
                offset_canvas.SetPixel(offset_canvas.width - 1, y, 0, 255, 0)
            offset_canvas = self.matrix.SwapOnVSync(offset_canvas)


# Main function
if __name__ == "__main__":
    simple_square = SimpleSquare()
    if (not simple_square.process()):
        simple_square.print_help()

# print(amt)
# print (sum(numbers)/len(numbers))
# print(dict)
#print(full)
