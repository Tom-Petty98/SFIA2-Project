from application import app
import random
import requests


@app.route('/randomword', methods=['GET'])
def sentence():
    setting = requests.get('http://localhost:5001/randomphrase')
    noun = requests.get('http://localhost:5002/randomphrase')

    a = random.randrange(2)

    if a == 0:
        return setting.text + " " + noun.text + " Happy theme"
    else:
        return setting.text + " " + noun.text + " Dark theme"

def tempo():
    setting = requests.get('http://localhost:5001/randomphrase')
    noun = requests.get('http://localhost:5002/randomphrase')

    a = random.randrange(2)

    if a == 0:
        return setting.text + " " + noun.text + " UPBEAT"
    else:
        return setting.text + " " + noun.text + " Descriptive, slow"

# I want all settings and nouns to be able to pair with theme/tempo 
# if i have to use logic based on the result of service 2 and 3 then I can have a list containing 
# all the alphabet in CAPS (as my first letter is always caps). Then my random number genearator will decide which half of the
# alphabet is which outcome. Thus achieving the same thing as done here so is a bit pointless. 