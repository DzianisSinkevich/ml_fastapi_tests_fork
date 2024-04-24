import pandas as pd


url = 'https://www.cbr.ru/currency_base/daily/'


def getrate(code):
    tables = pd.read_html(url)
    df = tables[0]
    mask = df['Цифр. код'] == int(code)
    count = df[mask].iloc[0]['Единиц']
    currency = df[mask].iloc[0]['Валюта']
    rate = df[mask].iloc[0]['Курс']
    return str(count) + ' ' + str(currency) + ' стоит ' + str(rate)[:-4] + ',' + str(rate)[-4:] + ' RUB'
