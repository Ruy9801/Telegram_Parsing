import requests
from bs4 import BeautifulSoup as BS
import csv


def get_html(url: str) -> str:
    response = requests.get(url)
    return response.text


def get_in(html):
    soup = BS(html, 'lxml')
    catalog = soup.find('div', class_='Tag--articles')
    cars = catalog.find_all('a', class_='ArticleItem--image')

    urls = []

    for link in cars:

        try:
            link_in = link.get('href')
            urls.append(link_in)
        except:
            link_in = ''

  
        
        
    return urls
        
       


def get_data(html):
    
    soup = BS(html, 'lxml')
    catalog = soup.find('div', class_='Tag--articles')
    nuws = catalog.find_all('div', class_='Tag--article')
    titles = {}

    for nuw in nuws:
        try:
            title = nuw.find('a', class_='ArticleItem--name').text.strip()
        except:
            title = ''
        try:
            img = nuw.find('a', class_='ArticleItem--image').find('img').get('src')
            titles.setdefault(title,img)
        except:
            img = ''
        
        if len(titles) == 20:
            break
    
    return titles


#     try:
#         info = catalog.find('div', class_='Article--info').find('time', class_='Article--createAt').text.strip()
#     except:
#         info = ''
#     try:
#         title = catalog.find('div', class_='Article--text').find('div', class_='BbCode').text.strip().replace('  ','')
#     except:
#         title = ''
#     try:
#         call = catalog.find('div', class_='Article--callCenter').text.strip()
#     except:
#         call = ''

#     media = f'\t{meida}\n\n\n {title}\n\t {info}\n\t {call}'
#     return media

def title_img():
    url = 'https://kaktus.media/?lable=8&date=2023-09-21&order=time'
        
    html = get_html(url)
        
    data = get_data(html)
    return data


def main():

   
    for page in range(1,2):
        url = f'https://kaktus.media/?lable=8&date=2023-09-21&order=time'
        print(f'Парсинг {page} страницы!!')
        html = get_html(url)
        

        login = get_in(html)


        medias = []
        for url in login:

            # html = get_html(url)
            # media = get_data(html)
            medias.append(url)
            if len(medias) == 20:
                break

        print(f'Парсинг {page} страницы завершен!!')
        return medias


main()





# touch .gitignore
# code .gitignore   внутри  /venv
# git init 