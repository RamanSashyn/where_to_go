# 📍 Where to go — Интерактивная карта Москвы

[**Демо-сайт**](https://Roomanhik98.pythonanywhere.com/)

Проект показывает интересные места Москвы на интерактивной карте. Каждая локация имеет краткое и подробное описание, фотогалерею и ссылки на сайты.

---

## 🚀 Как запустить локально

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

5. **Проведите миграции и запустите сервер:**

```bash
python manage.py migrate
python manage.py runserver
```

---

## 🛠️ Функционал

* Интерактивная карта с GeoJSON
* Галерея изображений
* Удобная админка с превью картинок
* Текстовый WYSIWYG-редактор (TinyMCE)
* Перетаскивание фото мышкой (adminsortable2)

---

## 👨‍💻 Технологии

* Django 3.2
* Leaflet.js
* TinyMCE
* django-admin-sortable2

---

## 📸 Скриншоты

*(Можно добавить сюда скрины главной карты и админки)*

---

## ©️ Автор

Raman Sashyn — 2025
[Мой GitHub](https://github.com/RamanSashyn)
