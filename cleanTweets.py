import pandas as pd
import re

'''
Limpa tweets, tira virgulas, pontuacoes, converte para minuscula
'''
df = pd.read_csv("pocketText.csv", parse_dates=["created_at"])

df_tweets = df.text
df_tweets = df_tweets.str.lower()
#print(df_tweets[0].split())
links = re.compile(r'\bhttps?://\w+.+\w+/\w+\b')
urls = re.compile(r'\bcom/\w+\b')
padrao = re.compile(r'[!?,.:;…“”()[\]{}\"\'*\-]+', re.UNICODE)

df_tweets = df_tweets.str.replace('amp;', '')
df_tweets = df_tweets.str.replace(links, ' ')
df_tweets = df_tweets.str.replace(urls, ' ')
df_tweets = df_tweets.str.replace(padrao, ' ')
df_tweets = df_tweets.str.replace('pic twitter', '*imagem*')
df_tweets = df_tweets.str.replace('/', ' / ')
df_tweets = df_tweets.str.replace('estados unidos', 'eua')
#print(df_tweets[0].split())
df['text'] = df_tweets
df.to_csv('texto.csv', index=False, quoting=1)


palavras_comuns = ['de', 'a', 'o', 'que', 'e', 'do', 'da', 'em', 'um',
                   'para', 'é', 'com', 'não', 'uma', 'os', 'no', 'se',
                   'na', 'por', 'mais', 'as', 'dos', 'como', 'mas',
                   'foi', 'ao', 'ele', 'das', 'tem', 'à', 'seu',
                   'sua', 'ou', 'ser', 'quando', 'muito', 'há', 'nos',
                   'já', 'está', 'eu', 'também', 'só', 'pelo', 'pela',
                   'até', 'isso', 'ela', 'entre', 'era', 'depois',
                   'sem', 'mesmo', 'aos', 'ter', 'seus', 'quem',
                   'nas', 'me', 'esse', 'eles', 'estão', 'você',
                   'tinha', 'foram', 'essa', 'num', 'nem', 'suas',
                   'meu', 'às', 'minha', 'têm', 'numa', 'pelos',
                   'elas', 'havia', 'seja', 'qual', 'será', 'nós',
                   'tenho', 'lhe', 'deles', 'essas', 'esses', 'pelas',
                   'este', 'fosse', 'dele', 'tu', 'te', 'vocês',
                   'vos', 'lhes', 'meus', 'minhas', 'teu', 'tua',
                   'teus', 'tuas', 'nosso', 'nossa', 'nossos',
                   'nossas', 'dela', 'delas', 'esta', 'estes',
                   'estas', 'aquele', 'aquela', 'aqueles', 'aquelas',
                   'isto', 'aquilo', 'estou', 'está', 'estamos',
                   'estão', 'estive', 'esteve', 'estivemos',
                   'estiveram', 'estava', 'estávamos', 'estavam',
                   'estivera', 'estivéramos', 'esteja', 'estejamos',
                   'estejam', 'estivesse', 'estivéssemos',
                   'estivessem', 'estiver', 'estivermos',
                   'estiverem', 'hei', 'há', 'havemos', 'hão',
                   'houve', 'houvemos', 'houveram', 'houvera',
                   'houvéramos', 'haja', 'hajamos', 'hajam',
                   'houvesse', 'houvéssemos', 'houvessem',
                   'houver', 'houvermos', 'houverem', 'houverei',
                   'houverá', 'houveremos', 'houverão', 'houveria',
                   'houveríamos', 'houveriam', 'sou', 'somos',
                   'são', 'era', 'éramos', 'eram', 'fui', 'foi',
                   'fomos', 'foram', 'fora', 'fôramos', 'seja',
                   'sejamos', 'sejam', 'fosse', 'fôssemos', 'fossem',
                   'for', 'formos', 'forem', 'serei', 'será', 'seremos',
                   'serão', 'seria', 'seríamos', 'seriam', 'tenho',
                   'tem', 'temos', 'tém', 'tinha', 'tínhamos', 'tinham',
                   'tive', 'teve', 'tivemos', 'tiveram', 'tivera',
                   'tivéramos', 'tenha', 'tenhamos', 'tenham',
                   'tivesse', 'tivéssemos', 'tivessem', 'tiver',
                   'tivermos', 'tiverem', 'terei', 'terá', 'teremos',
                   'terão', 'teria', 'teríamos', 'teriam']


