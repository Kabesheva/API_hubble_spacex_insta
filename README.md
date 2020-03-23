# Космический Инстаграм

В проекте находятся три скрипта:
1. скрипт `fetch_spacex.py`:
- обращается к [API SpaceX](https://github.com/r-spacex/SpaceX-API) и получает изображения с последнего запуска SpaceX
- обрезает полученные изображения до квадрата и изменяет размер изображений до 1080*1080 px
- конвертирует обработанные изображения в формат JPEG и сохраняет в папке "images" по шаблону (spacex_{id}_{имя файла первоисточника}_crop.jpg)

2. скрипт `fetch_hubble.py`:
- обращается к [API Hubble](http://hubblesite.org/api/documentation) и получает изображения из коллекций телескопа Hubble
- обрезает полученное изображение до квадрата и изменяет размер изображения до 1080*1080 px
- конвертирует обработанные изображения в формат JPEG и сохраняет в папке "images" по шаблону (images_{id}_crop.jpg)

3. скрипт `autopost_images.py`:
- публикует изображения из папки "images" в аккаунт Инстаграм
- опубликованные изображения после успешной загрузки будут переименованы {name}.REMOVE_ME, а изначальные изображения будут удалены
- при неудачной загрузке изображения остаются в папке "images" для целей отладки.
- названия загруженных файлов хранятся в файле `upload_images.txt`

---

### Как установить
Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

---

### Как пользоваться
Чтобы получить изображения от SpaceX запустите скрипт fetch_spacex.py
```python
python3 fetch_spacex.py
```

---

Чтобы получить изображения с телескопа Hubble запустите скрипт fetch_hubble.py и укажите название коллекции, фотографии из которой хотите сохранить

Примеры коллекций:
- holiday_cards
- wallpaper
- spacecraft
- news
- printshop
- stsci_gallery

```python
python3 fetch_hubble.py stsci_gallery
```

---
Чтобы опубликовать сохраненные фотографии запустите скрипт autopost_images.py
```python
python3 autopost_images.py
```
- частота размещения определяется
`timeout = 24*60*60 # 24 hours`

---

### Логин и пароль аккаунта Инстаграм
В файл `.env` положите данные в глобальные переменные:
- USER_NAME - логин от аккаунта в Инстаграм
- PASSWORD - пароль от аккаунта в Инстаграм

---
### Лицензия (License)
Это проект лицензирован по лицензии MIT - подробности см. в файле [LICENSE](./LICENSE)

---
### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).


Фото с телескопа Hubble![Фото с телескопа Hubble](./image_3883.png)