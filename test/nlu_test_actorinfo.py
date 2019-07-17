from rasa_nlu.converters import load_data
from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Metadata, Interpreter

sentence = [ "I want to know more about Brad Pitt.",
             "What information do you have on Michael Douglas?",
             "Can you tell me information on Judi Dench?",
             "I want to know more about Anne Hathaway.",
             "What can you tell me about Dustin Hoffman?",
             "Do you have any infomation about Woody Allen?",
             "Tell me what you know about Mark Wahlberg.",
             "I would like to know more information on Arnold Schwarzenegger.",
             "What information do you have on Hugo Weaving?",
             "Can you tell me something about James Caan?",
             "What do you know about Ben Stiller?",
             "Do you have any information on Willem Dafoe?",
             "What so you know about Winona Ryder?",
             "Can you tell me about Jennifer Lawrence?",
             "What can you tell me about Charlize Theron?",
             "Do you have information on Marion Cotillard?",
             "Tell me more about Reese Witherspoon.",
             "Do you know anything about Kevin Bacon?",
             "What do you know about Michael Caine?",
             "Can you get some information on Robert Duvall?" ]

interpreter = Interpreter.load('./models/nlu/default/movienlu', RasaNLUConfig('./config_spacy.json'))

right = 0
wrong = 0
seventyfive = 0
average = 0

for x in range (0, len(sentence)):
    print(sentence[x])
    result = interpreter.parse(sentence[x])
    average += result['intent']['confidence']
    if result['intent']['name'] == 'actor_info':
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