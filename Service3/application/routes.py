from application import app
import random

# random noun profession adjective 2nd half of scenario
# requires to different implemantations 
@app.route('/randomnoun', methods=['GET'])
def dark():
    list = ['Blood', 'Dead body', 'Gun', 'Gunshot', 'Bleeding man', 'screeming']
    return list[random.randrange(6)]

def light():
    list = ['£50 note', 'Wallet with £200', 'Wedding ring', 'Glimmering rock', 'Diamond']