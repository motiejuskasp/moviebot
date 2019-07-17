from rasa_nlu.converters import load_data
from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Metadata, Interpreter

sentence = [ "What good action movies can you tell me?",
             "Can you tell me best horror movies?",
             "Do you know any good history movies?",
             "What comedy movies can you recommend?",
             "Any animation movies you would recommend?",
             "What drama movies should i watch?",
             "Any westerns i should watch?",
             "What comedies would you recommend to watch?",
             "Do you know good sci-fi movies?",
             "What are best fantasy movies?",
             "Can you tell me best dramas?",
             "Would you recommend any crime movies?",
             "What romance movies are best?",
             "Tell me best action movies.",
             "Any adventure movies that are really good?",
             "What are some of best comedies?",
             "Tell me some western movies to watch.",
             "What are best thrillers?",
             "I am looking for good hitorical movies.",
             "Any good animation movies?" ]

interpreter = Interpreter.load('./models/nlu/default/movienlu', RasaNLUConfig('./config_spacy.json'))

right = 0
wrong = 0
seventyfive = 0
average = 0

for x in range (0, len(sentence)):
    print(sentence[x])
    result = interpreter.parse(sentence[x])
    average += result['intent']['confidence']
    if result['intent']['name'] == 'popular_search':
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

response = """\nright intent detection: {},
wrong intent detection: {},
above 75% confidence in {} of right intent""".format(
right, wrong, seventyfive)

print(response)
print("average right intent detected:")
print(right / len(sentence))
print("average confidence on correct intent is:")
print(average)