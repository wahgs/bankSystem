import gzip

#Creates a GZIP database for the BankSystem Server Client developed by grizhe
#:D
fileNotThere = bool
print("please type the directory that you would like to have the file in")
inp = input('example: C:/user/grizhe/database\n')
while fileNotThere:
    try: gzip.open(inp, compresslevel=9, encoding=None , errors=None, newline=None)
    finally: print("No gzip file detected in directory established")
    gzip.GzipFile(filename=inp, mode=None)
