from website import create_app
import datetime
import time
import sys
############################################ end imports

logFileName="bankSystem-log"
dtime = str(time.strftime("%Y-%m-%d--%H-%M-%S"))
logName = str(logFileName + '-' + str(dtime) + '.txt')
f=open(logName, "x")

#logging sequence
def log(inp):
    dateAndTime = str(time.strftime("%Y-%m-%d--%H-%M-%S"))
    msg = f'[Server] - {dateAndTime} - {inp}'
    f.write(msg)
    print(msg)
log(f'Logging initialized @ \'{str(logName)}\'')


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)