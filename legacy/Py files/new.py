import numpy as np
import keras
from keras.models import Sequential
from keras.layers.core import Dense
from keras.layers import Dropout,Conv2D
from sklearn.model_selection import train_test_split
import csv
import pandas as pd
import matplotlib.pyplot as plt
from keras.preprocessing.text import Tokenizer
tok = Tokenizer()

#LOADING DATA USING PANDAS
teams = ['ATL','BOS','BRK', 'CHO', 'CHI', 'CLE', 'DAL', 'DEN', 'DET', 'GSW', 'HOU','IND','LAC','LAL','MEM', 'MIA','MIL','MIN','NOP','NYK','OKC','ORL','PHI','PHO','POR','SAC','SAS','TOR','UTA','WAS']
# tok.fit_on_texts(teams)
# tok.texts_to_sequences(teams)
points = pd.read_csv('dataset/nba_games_stats.csv',usecols=['TeamPoints','OpponentPoints','WINLOSS','FieldGoals','Opp.FieldGoals','X3PointShots','Opp.3PointShots']).values
teamStats = pd.read_csv('dataset/nba_games_stats.csv',usecols=['Team','Home','Opponent']).values
X_train, X_test, y_train, y_test = train_test_split(teamStats, points, test_size=0.23)

#Making the neural network
model = Sequential()
keras.optimizers.adam(lr=0.1)
model.add(Dense(60, activation='relu',input_dim=3))
model.add(Dropout(0.25))
# model.add(Dense(46, activation='relu'))
# model.add(Dense(30, activation='relu'))
# model.add(Dense(20, activation='relu'))
model.add(Dense(30, activation='relu'))


#CNN

model.add(Dense(7, activation = 'relu'))

model.compile(loss='mean_squared_error',
              optimizer='rmsprop',
              metrics=['accuracy'])

model.fit(np.asarray(X_train), np.asarray(y_train), epochs=150)
model.evaluate(X_test,y_test)