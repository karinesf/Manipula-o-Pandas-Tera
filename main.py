#importação das bibliotecas necessárias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Fazendo a leitura de cada dataframe e armazenando em uma variável
df_aa = pd.read_csv('AAPL.csv', encoding='utf-8', parse_dates=['Date']) #já passando a data para o dtype datatime
#adicionando uma coluna Id com o código de cada ação
for i in range(len(df_aa['Date'])):
    df_aa['Id'] = 'AAPL'
#transformando a data em index
df_aa.set_index('Date', inplace=True)

df_am = pd.read_csv('AMZN.csv', encoding='utf-8', parse_dates=['Date'])
for i in range(len(df_am['Date'])):
    df_am['Id'] = 'AMZN'
df_am.set_index('Date', inplace=True)

df_go = pd.read_csv('GOOG.csv', encoding='utf-8', parse_dates=['Date'])
for i in range(len(df_go['Date'])):
    df_go['Id'] = 'GOOG'
df_go.set_index('Date', inplace=True)

df_nf = pd.read_csv('NFLX.csv', encoding='utf-8', parse_dates=['Date'])
for i in range(len(df_nf['Date'])):
    df_nf['Id'] = 'NFLX'
df_nf.set_index('Date', inplace=True)

df_ts = pd.read_csv('TSLA.csv', encoding='utf-8', parse_dates=['Date'])
for i in range(len(df_ts['Date'])):
    df_ts['Id'] = 'TSLA'
df_ts.set_index('Date', inplace=True)

#juntando todos os arquivos em um só
ar_all = pd.concat([df_aa, df_am, df_go, df_nf, df_ts]) #concatenando todos os df em um só
df_all = pd.DataFrame(ar_all)

#Qual das 5 ações teve a maior média de fechamento no período de julho a setembro de 2019?
df_pedaco = df_all.loc['2019-07-01': '2019-09-30']#delimitando as datas
df_final = df_pedaco.groupby('Id')['Adj Close'].max() #selecionando o grupo desejado
#pegando apenas o maior fechamento de cada ação por meio da coluna Adj Close.
print(df_final)
#plotando os dados para visualização da ação com a maior média de fechamento do período
df_final.plot(kind='bar')
plt.show()

