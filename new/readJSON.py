import pandas as pd
from textblob import TextBlob
import datetime
import glob
import os
import sys

numbers = []
store = []
place = []
dict = []
full = []
filetime = []

inc = 0
# global d
d = datetime.datetime.today()
now = datetime.datetime.now()

hr = now.hour
minu = now.minute
inthr = int(hr)
intmin = int(minu)

done = 0
print(glob.glob("*.json"))
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

done = 0

while done == 0:
    try:
        # yinput = input("Year please")
        Minput = input("zero padded month please: ")
        dinput = input("zero padded day please: ")
        hinput = input("zero-padded hour please: ")
        minput = input("zero-padded minute please: ")

        name = 'twitter_data-' + Minput + '-' + dinput + '-' + str(d.strftime('%y')) +\
               '-' + hinput + ':' + minput + '.json'

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
            full.append(store)
            store = []
            print(full[g])
            g += 1

# print(amt)
print (sum(numbers)/len(numbers))

# print(dict)
#print(full)
