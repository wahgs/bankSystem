import json
import bz2
import testaccount

kystring = json.dumps(testaccount.ky)

#working:
with open('accounts.txt', 'w') as outfile:
    json.dump(testaccount.ky, outfile)
#first converts the information into a json.dumps, then converts into a bz2 compression.
def compressConversion(mainput):
    compconvers = json.dumps(mainput)
    bz2.compress(compconvers)

#with open means "computer open, accounts.txt." as an outfile for the json.dump
with open('accounts.txt', 'w') as outfile:
        json.dump(compressConversion(testaccount.ky), outfile)

#ah
