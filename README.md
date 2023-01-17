# **Интернет магазин JoYstik** 

#### **Стек**
![python version](https://img.shields.io/badge/Python-3.11-green)
![django version](https://img.shields.io/badge/Django-4.2-green)
![pillow version](https://img.shields.io/badge/Pillow-8.3-green)
![requests version](https://img.shields.io/badge/requests-2.26-green)
![sorl-thumbnail version](https://img.shields.io/badge/thumbnail-12.7-green)
### **Описание**
Проект делается Двумя начинающими разработчиками, просьба не судить строго,
принимаем предложение и критику. Идея максимально проста, Интернет магазин игр и гаджетов, в ходе разработки хотим реализовать:

### **Наши  Цели**

:wrench:(в работе)  Сделать Подкатегории.
 
:heavy_check_mark:(на очереди) оптимизация базы данных  .
 
:white_check_mark:(сделанно)  Сделать описание проекта.
 
:heavy_check_mark:(на очереди)  Корзина.

<details>
<summary>
<b>Запуск проекта в dev-режиме 
</summary>
Инструкция ориентирована на операционную систему windows и утилиту git bash.<br/>
Для прочих инструментов используйте аналоги команд для вашего окружения.

1. Клонируйте репозиторий и перейдите в него в командной строке:

```
git clone git@github.com:Shkitskiy94/Joystick161.git
```

```
cd Joystick161
```

2. Установите и активируйте виртуальное окружение
```
python -m venv venv
``` 
```
source venv/Scripts/activate
```

3. Установите зависимости из файла requirements.txt
```
pip install -r requirements.txt
```

4. В папке с файлом manage.py выполните миграции:
```
python manage.py migrate
```

5. В папке с файлом manage.py запустите сервер, выполнив команду:
```
python manage.py runserver
```



