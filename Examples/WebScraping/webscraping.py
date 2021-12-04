import requests
from bs4 import BeautifulSoup
import urllib
#requests==2.13.0
#beautifulsoup4==4.5.3
#

def run():
    for i in range(1, 1501):
        response = requests.get('https://xkcd.com/{}'.format(i))
        soup = BeautifulSoup(response.content, 'html.parser')
        image_container = soup.find(id='comic')

        image_url = image_container.find('img')['src']
        image_name = image_url.split('/')[-1]#obtiene el ultimo string separado por /
        print('Descargando la imagen {}'.format(image_name))
        urllib.urlretrieve('https:{}'.format(image_url), image_name)#descarga la imagen


if __name__ == '__main__':
    run()