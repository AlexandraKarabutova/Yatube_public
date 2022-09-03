## Описание проекта:
Проект социальной сети через фреймворк Django.

### В проекте реализованы следующие возможности:
* Анонимным пользователям доступны просмотр публикаций авторов в формате ленты, просмотр подробной информации о каждой публикации, групп, страниц авторов, поиск по сайту. 

* Регистрация, авторизация на сайте, изменение, восстановление пароля от учетной записи с подтверждением через почтовый ящик.

* Авторизованные пользователи могут публиковать и удалять собственные записи, оставлять комментарии, подписываться на других авторов (добавлять их в избранное).

* При добавлении записей обязательно указать текст записи, группа и картинка добавляются по желанию.

## Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/AlexandraKarabutova/yatube.git
```
```
cd yatube
```
Cоздать и активировать виртуальное окружение:
```
python3 -m venv venv
```
```
source venv/scripts/activate
```
Установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
Выполнить миграции:
```
python3 manage.py migrate
```
Запустить проект:
```
python3 manage.py runserver
```