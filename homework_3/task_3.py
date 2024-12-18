import requests
from bs4 import BeautifulSoup

def main():
    url = 'https://mail.ru'  # URL для получения данных
    response = requests.get(url)  # Получаем данные с веб-сайта

    if response.status_code == 200:  # Проверяем, успешен ли запрос
        print("Данные успешно получены!")
        html_content = response.text  # Получаем HTML-код страницы

        # Парсинг HTML-кода с помощью BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        # Пример: выводим заголовок страницы
        title = soup.title.string
        print(f"Заголовок страницы: {title}")

        # Пример: выводим все ссылки на странице
        links = soup.find_all('a')
        print("Ссылки на странице:")
        for link in links:
            print(link.get('href'))

    else:
        print(f"Ошибка при получении данных: {response.status_code}")

if __name__ == "__main__":
    main()
