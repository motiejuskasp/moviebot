from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import logging

from rasa_core.agent import Agent
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy

if __name__ == '__main__':
    logging.basicConfig(level='INFO')
    
    training_data_file = './data/stories.md'
    model_path = './models/dialogue'
    
    agent = Agent('movie_domain.yml', policies = [MemoizationPolicy(), KerasPolicy()])
    
    agent.train(
            training_data_file,
            augmentation_factor = 50, # creates more stories from existing examples
            max_history = 2,          # number of states to remembers
            epochs = 400,             # forward and backward passes of training data in training process 
            batch_size = 20,          # training samples used in each pass
            validation_split = 0.2)   # % of data used to validate model
            
    agent.persist(model_path)
