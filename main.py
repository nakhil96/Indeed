import requests
from bs4 import BeautifulSoup
import pandas as pd
cmpInfoList=[]
cmpInputList=['Walmart','Tesla']


def extract(companyName):
    url = 'https://www.indeed.com/cmp/' + companyName
    headers = {'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
    r = requests.get(url, headers)
    print(r.status_code)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

def transform(soup):
    companyName = soup.find('div', class_='css-10nw9rq-Flex e37uo190').find('div').string
    ceo  = soup.find('li',{"data-testid" : 'companyInfo-ceo'}).find('div', class_ ='css-1t023bs-Text e1wnkr790').text
    foundingYear = soup.find('li', {"data-testid" : 'companyInfo-founded'}).find('div',class_='css-1t023bs-Text e1wnkr790').text
    size  = soup.find('li',{"data-testid" : 'companyInfo-employee'}).find('span').text
    revenue = soup.find('li', {"data-testid": 'companyInfo-revenue'}).find('span').text
    industryInfo = soup.find('li',{"data-testid": 'companyInfo-industry'}).find('div',class_='css-1t023bs-Text e1wnkr790').text
    #summary = soup.find('div', class_ = 'css-5xsqqw-Box eu4oa1w0').find('p').text.strip().replace('\n', '')
    overAllRating = soup.find('div',class_='css-fbbfmw-Box eu4oa1w0').find('g',class_='css-1vg6q84').find('text').text
    cmpInfoList.append(companyName)
    cmpInfoList.append(ceo)
    cmpInfoList.append(foundingYear)
    cmpInfoList.append(size)
    cmpInfoList.append(revenue)
    cmpInfoList.append(industryInfo)
    cmpInfoList.append(overAllRating)
    summary = soup.find('div', class_='css-5xsqqw-Box eu4oa1w0')
    items = soup.findAll('div',class_='css-1mvdiu2-Box eu4oa1w0')
    print(items)
    print(len(items))


    return cmpInfoList



if __name__ == '__main__':
    cmp = extract('Walmart')
    cmpInfoList = transform(cmp)
    print(cmpInfoList)
    df = pd.DataFrame([cmpInfoList],columns=['Company Name','CEO Name','Founded','size','Revenue','Industry Info','OverAll Rating'])

    df.to_csv('cmpInfo.csv')


