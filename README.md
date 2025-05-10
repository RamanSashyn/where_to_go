# 📍 Where to go — Интерактивная карта Москвы

[**Демо-сайт**](https://Roomanhik98.pythonanywhere.com/)

Проект показывает интересные места Москвы на интерактивной карте. Каждая локация имеет краткое и подробное описание, фотогалерею и ссылки на сайты.

---

##  Как запустить локально

1. **Склонируйте репозиторий:**

```bash
git clone https://github.com/RamanSashyn/where_to_go.git
cd where_to_go
```

2. **Создайте и активируйте виртуальное окружение:**

```bash
python -m venv venv
source venv/bin/activate    # Linux/macOS
venv\Scripts\activate      # Windows
```

3. **Установите зависимости:**

```bash
pip install -r requirements.txt
```

4. **Создайте `.env` файл в корне проекта:**

```ini
DEBUG=True
SECRET_KEY=ваш_секретный_ключ
ALLOWED_HOSTS=127.0.0.1,localhost
```

5. **Проведите миграции и создайте суперпользователя:**

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

6. **Соберите статику и запустите сервер**
```bash
python manage.py collectstatic --noinput
python manage.py runserver
```

---

## Функционал

* Интерактивная карта с GeoJSON
* Галерея изображений
* Удобная админка с превью картинок
* Текстовый WYSIWYG-редактор (TinyMCE)
* Перетаскивание фото мышкой (adminsortable2)

---

## Технологии

* Django 3.2
* Leaflet.js
* TinyMCE
* django-admin-sortable2

## Структура проекта
/places/ — приложение с моделями и загрузкой данных

/templates/ — HTML-шаблоны

/static/ — статика (JS, CSS)

/media/places/ — сохраняются изображения

---

## Загрузка данных о локациях при помощи load_place

Для автоматического добавления локаций на сайт из JSON-файлов предусмотрена команда `load_place`.

### Что делает скрипт

- Загружает JSON-файл по указанному URL.
- Создаёт новую локацию (`Place`) в базе данных.
- Загружает изображения и привязывает их к этой локации.

### Использование

Убедитесь, что вы находитесь в виртуальном окружении проекта и в корне Django-проекта (там, где `manage.py`):

```bash
python manage.py load_place <ссылка_на_json>
```

### Пример:
```bash
python manage.py load_place https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/anticafe_bizone.json
```
### Примечания
Если локация с таким названием уже существует — данные повторно не будут загружены.

Фотографии будут автоматически скачаны и сохранены в media/places/.

### Где взять JSON
Вы можете взять JSON-файлы отсюда:
https://github.com/devmanorg/where-to-go-places/tree/master/places
Нажмите на нужный файл, затем Raw — и скопируйте ссылку для передачи в команду.

### Пример JSON-файла
```json
{
  "title": "Антикафе Bizone",
  "imgs": [
    "https://...1.jpg",
    "https://...2.jpg"
  ],
  "description_short": "Короткое описание",
  "description_long": "<p>HTML-описание...</p>",
  "coordinates": {
    "lng": "37.50169",
    "lat": "55.816591"
  }
}
```

## Автор

Raman Sashyn — 2025
[Мой GitHub](https://github.com/RamanSashyn)
