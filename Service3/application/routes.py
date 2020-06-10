from application import app
import random

 
@app.route('/randomnoun', methods=['GET'])
def dark():
    list = ['Blood', 'Dead body', 'Gun', 'Gunshot', 'Bleeding man', 'screeming']
    return list[random.randrange(6)]


@app.route('/randomnoun2', methods=['GET'])
def light():
    list = ['£50 note', 'Wallet with £200', 'Wedding ring', 'Glimmering rock', 'Diamond']
    return list[random.randrange(5)]