from bs4 import BeautifulSoup
import requests
from flask import Flask

HEADERS = {
    'User-Agent': 'Mozilla/5.0'
    '(Macintosh; Intel Mac OS X 10_10_1)'
    'AppleWebKit/437.36 (KHTML, like Gecko)'
    'Chrome/39.0.2171.95 Safari/437.36'
          }

#app = Flask(__name__)

def news_grab(name, search_url):  # only one page
    
    response = requests.get('https://'+search_url+name, headers=HEADERS)
    assert response.status_code == 200, print('Banned')
    
    soup = BeautifulSoup(response.text, 'lxml')
    return soup

def vc_parse(name, soup, scrapped_info):

    for item in soup.find_all('div', class_=lambda x: x and x.startswith('l-mb-28 lm-mb-20')):

        container = item.find('div', class_="content-container").text.split('\n')
        title, *_trash, short_text = [x.strip() for x in container if x!='']
        if name.lower() in title.lower():
            scrapped_info['main_idea'] += 1
            scrapped_info['main_art'].append((title, short_text))
        else:
            scrapped_info['nmain_art'].append((title, short_text))

        #date = item.find('time', class_='time').get('title')
        #scrapped_info['old_date'] = date
        #if scrapped_info['new_date'] == '':
        #    scrapped_info['new_date'] = date
            
        scrapped_info['n_articles'] += 1
    return scrapped_info

def ya_parse(name, soup, scrapped_info):
   
    feed = soup.find('div', class_='mg-grid__col mg-grid__col_xs_8 mg-grid__col_sm_6')
    for item in feed:
        title = item.find('div', 'mg-snippet__title')
        short_text = item.find('span', 'mg-snippet__text')
        if title == None:
            break
        
        title = title.text
        short_text = short_text.text
        if name.lower() in title.lower():
            scrapped_info['main_idea'] += 1
            scrapped_info['main_art'].append((title, short_text))
        else:
            scrapped_info['nmain_art'].append((title, short_text))

        #date = item.find('span', 'mg-snippet-source-info__time').text
        #scrapped_info['old_date'] = date
        #if scrapped_info['new_date'] == '':
        #    scrapped_info['new_date'] = date
      
        scrapped_info['n_articles'] += 1
  
    return scrapped_info

#@app.route('/')
def index():
    return 'index page'


#@app.route('/grab/<name>')
def search_info(name, max_len=3):
    ya_url = 'newssearch.yandex.ru/news/search?flat=1&text='
    vc_url = 'vc.ru/search/v2/all/new?query='
    
    scrapped_info = {
            'main_idea':0,
            'n_articles':0,
            'main_art': [],
            'nmain_art': [],
            }

    ya_soup = news_grab(f'"{name}"', ya_url)
    vc_soup = news_grab(name, vc_url)

    ya_parse(name, ya_soup, scrapped_info)
    vc_parse(name, vc_soup, scrapped_info)  
    
    if scrapped_info['main_art']:
        return ''.join([f'{title}: {text};\n' for title, text in scrapped_info['main_art'][:max_len]])
    elif scrapped_info['nmain_art']:
        return ''.join([f'{title}: {text};\n' for title, text in scrapped_info['nmain_art'][:max_len]])
    else:
        return 'Упоминаний в СМИ не найдено'



#if __name__== '__main__':
   # app.run(host='127.0.0.1', port=5000, debug=True)
    