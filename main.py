from website import create_app
import time
import sys
############################################ end imports


app = create_app()

if __name__ == '__main__':
    #starts app

    app.run(use_reloader=False, debug=True)
    
