from rasa_nlu.converters import load_data
from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Metadata, Interpreter

sentence = [ "In what movies Jack Nicholson took a part?",
             "What movies featuring Meril Streep you know?",
             "Can you tell me some movies with Marlon Brando?",
             "Do you know any movies Jodie Foster acting in?",
             "Could you tell me movies featuring Dustin Hoffman?",
             "What movies can you tell me with Hilary Swank acting?",
             "How about movies where Anthony Hopkins is acting?",
             "Tell me movies with Shirley MacLaine.",
             "Can you tell me movies with Colin Farrell?",
             "What movies do you know featuring Jared Leto?",
             "Tell me some movies with Jude Law?",
             "What are movies with Liam Neeson?",
             "Any movies with Matt Damon?",
             "Do you know some movies with Michael Fassbender?",
             "Can you find movies with Kate Hudson?",
             "I am looking for movies with Cameron Diaz.",
             "Could you tell movies with Lena Headey?",
             "What movies you know with Emma Watson?",
             "Can you tell me some Kurt Russell movies?",
             "Any movies with Jake Gyllenhaal?" ]

interpreter = Interpreter.load('./models/nlu/default/movienlu', RasaNLUConfig('./config_spacy.json'))

right = 0
wrong = 0
seventyfive = 0
average = 0

for x in range (0, len(sentence)):
    print(sentence[x])
    result = interpreter.parse(sentence[x])
    average += result['intent']['confidence']
    if result['intent']['name'] == 'movie_search':
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