import requests as req
from bs4 import BeautifulSoup
import fake_useragent as fu
from requests import session

# плюс lxml это используемый парсер

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

# надо получить инфу с нащего профиля
link_profile = 'https://4pda.to/forum/index.php?showuser=11901521'
profile_ans = session.get(link_profile, headers=header).text

# наши куки
cookies_dict = [key for key in session.cookies]

"""
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