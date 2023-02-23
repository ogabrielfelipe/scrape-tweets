import pandas as pd
import snscrape.modules.twitter as sntwitter
from datetime import datetime
import os, calendar, itertools

# Abreviações dos intitutos a serem buscados
institutes_abbreviations = [
    'IFF',
    "IFSUDESTEDEMINAS",
    'IFRJ',    
    "IFSP",
    "IFMG",
    "IFNMG",
    "IFUSULDEMINAS",
    "IFTM",
    "IFES"
]

# Demais parâmetros que será acrescentado na busca com as abreviações
others_params = [
    "ensino",
]  

max_items = 500 #Total de itens que vai ser buscado por mês
max_items_consolidated = 500 # Total de itens que será gerado no arquivo: output_tweet_consolidated_sliced.csv 
years = ["2020", "2019", "2018", "2017"] # Total de anos a serem buscados
months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] # Lista dos meses que serão buscados nos anos: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

others_params_text = ' '.join(map(str, others_params))
list_name_csv_consolidated = []

print('🔎 Iniciando a busca por Tweets.......')

for institute in institutes_abbreviations:    
    path = os.path.join(os.getcwd(), institute)
    if not os.path.isdir(path):
        os.mkdir(path)
    tweet_list =[]
    
    print(f'📌 Buscando tweets do instituto: {institute}')

    for year in years:
        for month in months:
            yy = int(year)
            mm = int(month)
            dias = calendar.monthrange(yy, mm)
            inicio = str(yy)+'-'+str(mm)+'-'+str(1)
            fim = str(yy)+'-'+str(mm)+'-'+str(dias[1])
            dateInitial = datetime.strptime(inicio, '%Y-%m-%d').date()
            dateFinal = datetime.strptime(fim, '%Y-%m-%d').date()

            scraped_tweets = sntwitter.TwitterSearchScraper(f'{institute} {others_params_text} since:{dateInitial}  until:{dateFinal} lang:pt-br').get_items()
            sliced_scraped_tweets = itertools.islice(scraped_tweets, max_items)

            df = pd.DataFrame(sliced_scraped_tweets, columns=['date', 'rawContent'])
            df.to_csv(f'{institute}/output_tweet_{institute}_{mm}-{yy}.csv', sep=';', header=['date', 'rawContent'], index=False, encoding='utf-8')
            tweet_list.append(f'{institute}/output_tweet_{institute}_{mm}-{yy}.csv')

    df = pd.concat([pd.read_csv(csv_name, sep=';') for csv_name in tweet_list], ignore_index=True)
    df.to_csv(f'{institute}/output_tweet_{institute}_consolidated.csv', sep=';', header=['date', 'rawContent'], index=False, encoding='utf-8')
    list_name_csv_consolidated.append(f'{institute}/output_tweet_{institute}_consolidated.csv')

df = pd.concat([pd.read_csv(csv_name, sep=';', header=None) for csv_name in list_name_csv_consolidated], ignore_index=True)
df.to_csv('output_tweet_consolidated.csv', sep=';', header=['date', 'rawContent'], index=False, encoding='utf-8')

tweets_consolidated_sliced = pd.DataFrame(pd.read_csv('output_tweet_consolidated.csv',  sep=';'))
tweets_consolidated_sliced = tweets_consolidated_sliced.sample(n=max_items_consolidated)
tweets_consolidated_sliced.to_csv('output_tweet_consolidated_sliced.csv', sep=';', header=['date', 'rawContent'], index=False, encoding='utf-8')

print('✅ Busca Efetuada com sucesso!!')