from collections import Counter
# my functions start
from subsampler import multiIter
from probability import peso
from cleanTweets import palavras_comuns
# my functions end
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
from PIL import Image
pd.set_option('display.max_rows', 10000)

df = pd.read_csv("texto.csv")
first = []               # uma lista com todas as palavras dos tweets
subsamples = {}          # palavras vizinhas(por tweet) e conta as aparicoes
for text in df.text:
    each = text.split()
    for word in each:
        # uma lista com todas as palavras dos tweets
        first.append(word)
    for samples in multiIter(each, 5):
        # multiIter function from subsampler.py, gera vizinhos
        for i in range(len(samples[0])):
            if i != samples[1]:
                # adiciona palavras vizinhas(por tweet) e conta as aparicoes
                subsamples.setdefault(samples[0][samples[1]], {}).setdefault(samples[0][i], 0)
                subsamples[samples[0][samples[1]]][samples[0][i]] += 1


# CONTADORES
Counter = Counter(first)
n = round(len(Counter)/100) # um porcento das palavras para exibir as mais comuns
most = Counter.most_common(n)
least = Counter.most_common()[:-n-1:-1]
total = sum(Counter.values())


# BLOCO DE BUSCA PELO CONTEXTO DE UMA PALAVRA
palavras = ['eua']
dados_finais = pd.DataFrame(columns=['palavra', 'frequencia', 'peso'])
for w in palavras:
    pesquisa = subsamples[w]
    print("A palavra **{}** aparece {} vezes nos tweets de bolsonaro".format(w, Counter.get(w)))
    print("Palavras associadas:")
    for k in pesquisa:
        position = dados_finais['palavra'].eq(k)
        if position.any():
            dados_finais.loc[position, ['frequencia']] += pesquisa[k]
            dados_finais.loc[position, ['peso']] += peso(Counter.get(k), total) * pesquisa[k]
        else:
            if k not in palavras_comuns:
                dados_finais = dados_finais.append({'palavra': k,
                                                    'frequencia': pesquisa[k],
                                                    'peso': peso(Counter.get(k),
                                                                 total) * pesquisa[k]},
                                                   ignore_index=True)
print(dados_finais.sort_values('peso', ascending=False))



# PALAVRAS MAIS E MENOS COMUNS
'''
print("De {} palavras distintas, seguem as {} mais e menos comuns:".format(len(Counter), n))
print(most)
print(least)
print(total)
'''

dicionario_dados = dict(pd.Series(dados_finais.peso.values, index=dados_finais.palavra).to_dict())
print(dicionario_dados)
#mask = np.array(Image.open("pt.png"))
wc = WordCloud(background_color='white',
               width=1000,
               height=2000,
               max_words=100,
               max_font_size=90,
               random_state=50,
               normalize_plurals=False,
               #mask=mask
               ).generate_from_frequencies(dicionario_dados)
#image_colors = ImageColorGenerator(mask) #.recolor(color_func=image_colors)
plt.figure()
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()