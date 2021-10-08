import json
import bz2
import testaccount

kystring = json.dumps(testaccount.ky)

with open('accounts.txt', 'w') as outfile:
    json.dump(data, outfile)
def compressConversion(mainput):
    compconvers = json.dumps(mainput)
    bz2.compress(compconvers)

#with open means "computer open, accounts.txt." as an outfile for the json.dump
with open('accounts.txt', 'w') as outfile:
        json.dump(compressConversion(testaccount.ky), outfile)
