import numpy
import pygame
import pandas as pd
customer_json_file = 'twitter_data.json'
customers_json = pd.read_json(customer_json_file,convert_dates=True)
customers_json.head()





