from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput

nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/movienlu')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

input_channel = SlackInput('xoxp-366026811859-365582762801-366266745605-4af5546fae51fc8cb936be5e2203a6a8',
                            'xoxb-366026811859-366128665410-YSgFCjBueDOVQIvhB2L1OlxL',
                            'vaUyndScYTpL6Jn7ShfscHOd', True)

agent.handle_channel(HttpInputChannel(5004, '/', input_channel))

