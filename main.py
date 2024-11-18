import requests as req
from bs4 import BeautifulSoup
import fake_useragent as fu
from requests import session
import multiprocessing
import json


# плюс lxml это используемый парсерhhhhh

def get_js(sp):
    block = sp.find('div', id='javascript_check')
    print(block.find_all('span')[1].text)


def get_cookie(sp):
    block = sp.find('div', id='cookie_check')
    print(block.find_all('span')[1].text)


def get_flash(sp):
    block = sp.find('div', id='flash_version')
    print(block.find_all('span')[1].text)


def main():
    with open('config.json') as file:
        config = json.load(file)

    ans = req.get('https://browser-info.ru/').text
    soup = BeautifulSoup(ans, 'lxml')

    if config['js'] == True:
        get_js(soup)
    if config['cookie'] == True:
        get_cookie(soup)
    if config['flash'] == True:
        get_flash(soup)


if __name__ == '__main__':
    main()

"""
# функция для проверки прокси на валидность
def handler(proxy):
    link = f'https://zastavok.net'

    proxies = {
        'http': f'http//:{proxy}',
        'https': f'http//:{proxy}'
    }

    try:
        ans = req.get(link, proxies=proxies, timeout=2).text
        print(f'IP: {ans.strip()}')
    except:
        print('Прокси не валидный!')

if __name__ == '__main__':

    # берем из файла IP и помещаем в список
    with open('proxiess.txt') as file:
        proxy_base = ''.join(file.readlines()).strip().split('\n')
    
    # подключения процессов для более быстрой обработки
    with multiprocessing.Pool(multiprocessing.cpu_count()) as process:
        process.map(handler, proxy_base)


img_num = 0
num=0
link = f'https://zastavok.net'

user = fu.UserAgent().random

header = {
    'user-agent':user
}


ans = req.get(f'{link}/{num}', headers=header).text
soup = BeautifulSoup(ans, 'lxml')

# находим блок с картинками
block = soup.find('div', class_='block-photo')

all_image = block.find_all('div', class_='short_full')

for img in all_image:

    image_link = img.find('a').get('href')
    download_str = req.get(f'{link}{image_link}', headers=header).text
    download_soup = BeautifulSoup(download_str, 'lxml')
    block_img = download_soup.find('div', class_='image_data').find('div', class_='block_down')
    images = block_img.find('a').get('href')

    # сохраняем картинку в байтах "wb" на компе
    image_bytes = req.get(f'{link}{images}', headers=header).content

    with  open(f'image/{img_num}.jpg', 'wb') as file:
        file.write(image_bytes)

    print(f"Картинка {img_num}.jpg успешна скачена")
    img_num += 1



# Создадим сессию, чтобы каждый раз не регаться заново, а чтобы были куки.
session = req.Session()

# password: FLb-czQ-uFk-ci7, login: test_member1234
# ссылка на сайт для парсинга (сбора данных со страницы сайты)
link = 'https://4pda.to/forum/index.php?act=auth'

user = fu.UserAgent().random

header = {
    'user-agent':user
}

data = {
    'login': 'test_member1234',
    'password': 'FLb-czQ-uFk-ci7'
}

# надо зарегаться
ans = session.post(link, data=data, headers=header)

# надо получить инфу с нашего профиля
link_profile = 'https://4pda.to/forum/index.php?showuser=11901521'

profile_ans = session.get(link_profile, headers=header).text

# наши куки
cookies_dict = [
    {
        'domain': key.domain,
        'name': key.name,
        'path': key.path,
        'value': key.value
    }
    for key in session.cookies
]

session2 = req.Session()

# запись кук из 1 сессии во 2
for cookies in cookies_dict:
    session2.cookies.set(**cookies)

rse_ans = session2.get(link_profile, headers=header).text
print(rse_ans)


# рандом юзеры для парсинга
user = fu.UserAgent().random

# обход обнаружения парсинга сайтом
header = {'user-agent': user}

# получаем контент со страницы (text - указан для получения инфы на странице)
ans = req.get(link, headers=header).text

# проверяем дошёл ли наш запрос до сайта, если 200, то всё ок
print(ans.status_code)

# вывод полученной инфы
print(ans.text)

# запишем ответ в html файл
with open('ans.html', 'w', encoding='utf-8') as file:
   file.write(ans.text)


# для нахождения нужных значений на странице
soup = BeautifulSoup(ans, 'lxml')

# для нахождения определенного блока, если нужны все, то find_all
block = soup.find('div', id='tool_padding')

check_js = block.find('div', id='javascript_check')

types = check_js.find_all('span')[0].text

users_name = block.find('div', id='user_agent').text

print(users_name)

# для получения ссылок
.find('a').get('href')
"""
