from rasa_nlu.converters import load_data
from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Metadata, Interpreter

sentence = [ "What can you tell about movie The Godfather?",
             "Any information about movie GoodFellas?",
             "What can you tell me about movie Forrest Gump?",
             "Can you tell me details of Gladiator movie?",
             "Do you know details of movie Back to the Future?",
             "How about movie Apocalypse Now details?",
             "Could you tell me details of The Shining?",
             "What do you know about Titanic?",
             "What can you tell me about movie Inception?",
             "What do you know about The Matrix?",
             "I am looking for information about movie Se7en.",
             "Can you tell me more about movie Spirited Away?",
             "Do you know something about Interstellar?",
             "I heard The Intouchables is great movie, what can you tell me about it?",
             "Tell me something about movie Whiplash.",
             "Can you tell me about movie Memento?",
             "I want to know more about WALL·E.",
             "What can you tell me about movie Princess Mononoke?",
             "I need information on Citizen Kane movie.",
             "Tell me all about Braveheart movie." ]

interpreter = Interpreter.load('./models/nlu/default/movienlu', RasaNLUConfig('./config_spacy.json'))

right = 0
wrong = 0
seventyfive = 0
average = 0

for x in range (0, len(sentence)):
    print(sentence[x])
    result = interpreter.parse(sentence[x])
    average += result['intent']['confidence']
    if result['intent']['name'] == 'movie_info':
        right += 1
        print('right')
        print(result['intent']['confidence'])
        print()
        if result['intent']['confidence'] >= 0.75:
            seventyfive += 1
    else :
        wrong += 1
        print('wrong')
        print()

average = average / len(sentence)

response = """right intent detection: {},
wrong intent detection: {},
above 75% confidence in {} of right intent""".format(
right, wrong, seventyfive)

print(response)
print("average right intent detected:")
print(right / len(sentence))
print("average confidence on correct intent is:")
print(average)