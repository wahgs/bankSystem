from website import create_app
from datetime import date, datetime
from time import sleep
import sys
############################################ end imports

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)