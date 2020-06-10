from application import app
import random


@app.route('/randomsetting', methods=['GET'])
def setting():

    list = ['Mountains', 'Stream', 'Waterfall', 'Cliff', 'Beach', 'Volcano', 'Forest', 'Desert']
	
    return list[random.randrange(8)]


@app.route('/randomsetting2', methods=['GET'])
def setting2():
    list = ['Village', 'Tribal settlement', 'Castle', 'City center', 'Holiday resort']
    return list[random.randrange(5)]