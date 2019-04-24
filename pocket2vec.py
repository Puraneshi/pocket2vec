import multiprocessing

import gensim.models.word2vec as w2v
import pandas as pd
from nltk.tokenize import TweetTokenizer

from cleanTweets import palavras_comuns

corpus_raw = u''
token = TweetTokenizer()
temp_df = pd.read_csv('pocketText.csv', encoding='utf-8', quoting=2)
index = 2
text = temp_df.text.str.lower()

# remove urls
text = text.str.replace(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '')

# remove symbols but # and @
text = text.str.replace(r'[^\w@#\s]', '')
text = text.str.replace('ñ', 'não')
text = text.str.replace('estados unidos', 'eua')
print(text[index])
for stopword in palavras_comuns:
    text = text.str.replace(r'\b'+stopword+r'\b', '')
print(text[index])
# store tokenized tweets ( a list of lists)
tweets = []
for tweet in text:
    lista_token = token.tokenize(tweet)
    tweets.append(lista_token)
# total number of words
token_count = sum([len(tweet) for tweet in tweets])


# start word2vec
num_features = 200
min_word_count = 1
num_workers = multiprocessing.cpu_count()
context_size = 7
downsampling = 1e-3
seed = 42

# train and save
pocket2vec = w2v.Word2Vec(
    sg=1,
    seed=seed,
    workers=num_workers,
    min_count=min_word_count,
    window=context_size,
    sample=downsampling
)

pocket2vec.build_vocab(tweets)
print(len(pocket2vec.wv.vocab))
pocket2vec.train(tweets, total_examples=token_count, epochs=100)
pocket2vec.save("trained_pocket2vec.w2v")
