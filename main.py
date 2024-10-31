import requests as req

# ссылка на сайт для парсинга(сбора данных со страницы сайты)
link = 'https://browser-info.ru/'

# получаем контент со страницы (text - указан для получения инфы на странице)
ans = req.get(link)

# проверяем дошёл ли наш запрос до сайта, если 200, то всё ок
print(ans.status_code)

# вывод полученной инфы
print(ans.text)

# запишем ответ в html файл
with open('ans.html', 'w', encoding='utf-8') as file:
    file.write(ans.text)