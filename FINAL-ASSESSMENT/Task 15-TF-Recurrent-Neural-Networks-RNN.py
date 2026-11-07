import warnings
from tensorflow.keras.utils import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow import keras
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import numpy as np
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from keras.metrics import Precision, Recall

import re
import nltk
nltk.download('all')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
lemm = WordNetLemmatizer()

warnings.filterwarnings("ignore")

# load data
data = pd.read_csv(r'E:\neskill\NexSkill course AI bin\FINAL-ASSESSMENT\10-diamonds.csv', index_col='Unnamed: 0')
data.head(7)
print(data.shape)

data = data[data['cut'].isnull() == False]

sns.countplot(data=data, x='cut')
plt.xticks(rotation=90)
plt.show()

plt.subplots(figsize=(12, 5))
plt.subplot(1, 2, 1)
sns.countplot(data=data, x='color')

plt.subplot(1, 2, 2)
sns.countplot(data=data, x="clarity")
plt.show()

fig = px.histogram(data, marginal='box',
                   x="carat", title="Carat Group",
                   color="cut",
                   nbins=65-18)
fig.update_layout(bargap=0.2)

fig = px.histogram(data,
                   x="carat",
                   marginal='box',
                   title="Carat Group",
                   color="cut",
                   nbins=65-18,
                   color_discrete_sequence\
                   =['black', 'green', 'blue', 'red', 'yellow'])
fig.update_layout(bargap=0.2)

# 1 if price is more than the median price
median_price = data['price'].median()

def filter_score(price):
    return int(price > median_price)

features = ['cut', 'color', 'clarity']

X = data[features]
y = data['price']
y = y.apply(filter_score)


def toLower(data):
    if isinstance(data, float):
        return '<UNK>'
    else:
        return data.lower()

def remove_punctuation_func(text):
    return re.sub(r'[^a-zA-Z0-9]', ' ', text)

X['cut'] = X['cut'].apply(toLower)
X['color'] = X['color'].apply(toLower)
X['clarity'] = X['clarity'].apply(toLower)

X['cut'] = X['cut'].apply(lambda x: lemm.lemmatize(x))
X['color'] = X['color'].apply(lambda x: lemm.lemmatize(x))
X['clarity'] = X['clarity'].apply(lambda x: lemm.lemmatize(x))

X['cut'] = X['cut'].apply(remove_punctuation_func)
X['color'] = X['color'].apply(remove_punctuation_func)
X['clarity'] = X['clarity'].apply(remove_punctuation_func)

X['Text'] = list(X['cut']+' '+X['color']+' '+X['clarity'])


X_train, X_test, y_train, y_test = train_test_split(
    X['Text'], y, test_size=0.25, random_state=42)


tokenizer = Tokenizer(num_words=10000, oov_token='<OOV>')
tokenizer.fit_on_texts(X_train)


train_seq = tokenizer.texts_to_sequences(X_train)
test_seq = tokenizer.texts_to_sequences(X_test)

train_pad = pad_sequences(train_seq,
                          maxlen=5,
                          truncating="post",
                          padding="post")
test_pad = pad_sequences(test_seq,
                         maxlen=5,
                         truncating="post",
                         padding="post")


model = keras.models.Sequential()
model.add(keras.layers.Embedding(10000, 128))
model.add(keras.layers.SimpleRNN(64, return_sequences=True))
model.add(keras.layers.SimpleRNN(64))
model.add(keras.layers.Dense(128, activation="relu"))
model.add(keras.layers.Dropout(0.4))
model.add(keras.layers.Dense(1, activation="sigmoid"))


METRICS = metrics=['accuracy', 
                   Precision(name='precision'),
                   Recall(name='recall')]


model.compile("rmsprop",
              "binary_crossentropy",
               metrics = METRICS)
history = model.fit(train_pad,
                    y_train,
                    epochs=5)

print("Summary:                  \n" , model.summary())