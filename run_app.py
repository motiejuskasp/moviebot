from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput

nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/movienlu')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

# enter your own token codes
input_channel = SlackInput('OAuthAccessToken',
                            'BotUserOAuthAccessToken',
                            'VerificationToken', True)

agent.handle_channel(HttpInputChannel(5004, '/', input_channel))

