# pocket2vec
Codes to learn and test word2vec and sintax learning implementations using tweets from the president of brazil

.main.py: main code, uses 'text.csv' and other .py (for functions);  
  input: the 'palavras' variable is a list of the words which the code will use to search for context  
  output: a dictionary of words and weights around the searched words + a wordcloud image of those words

.probability.py: contains the weight function as described by word2vec implementation

.subsampler.py: contains a function that recieves a list and a number of neighbors and returns an iterable and the index of main element  
  e.g. multiIter([a,b,c,d,e], 2) -> ([a,b,c], 0) , ([a,b,c,d],1) , ([a,b,c,d,e], 2) , ([b,c,d,e], 3) , ([c,d,e], 4)

.cleanTweets.py: filters much of the "twitter language", links, symbols and outputs a "clean" csv
