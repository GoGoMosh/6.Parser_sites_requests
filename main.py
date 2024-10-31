import requests as req
from bs4 import BeautifulSoup
# плюс lxml это используемый парсер

# ссылка на сайт для парсинга(сбора данных со страницы сайты)
link = 'https://browser-info.ru/'

# получаем контент со страницы (text - указан для получения инфы на странице)
ans = req.get(link).text
#
# # проверяем дошёл ли наш запрос до сайта, если 200, то всё ок
# print(ans.status_code)
#
# # вывод полученной инфы
# print(ans.text)
#
# # запишем ответ в html файл
# with open('ans.html', 'w', encoding='utf-8') as file:
#    file.write(ans.text)

# для нахождения нужных значений на странице
soup = BeautifulSoup(ans, 'lxml')

# для нахождения определенного блока, если нужны все, то find_all
block = soup.find('div', id='tool_padding')

check_js = block.find('div', id='javascript_check')

types = check_js.find('class', id='option_title')

print(check_js)