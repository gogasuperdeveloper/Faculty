## Сайт факультету

НаУКМА не має окремого факультету міжнародних відносин та врядування. При аналізі бачимо що цей факультет
розбито між декількома:

- **Кафедра міжнародних відносин** входить до Факультету соціальних наук і
  соціальних технологій (ФСНСТ);
- **Києво-Могилянська школа врядування імені Андрія Мелешевича** — до Факультету
  правничих наук.

## Стек

- Python, Django 5.2
- SQLite
- Server-Side Rendering (Django Template Language)

## Сторінки

- `/` — головна (опис факультету, інформація, контакти)
- `/programs/` — список спеціальностей
- `/programs/<id>/` — сторінка спеціальності
- `/departments/` — список кафедр
- `/departments/<id>/` — сторінка кафедри
- `/exchange/` — програми академічного обміну 

## Запуск

```bash
python -m venv venv
venv\Scripts\activate          
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```


