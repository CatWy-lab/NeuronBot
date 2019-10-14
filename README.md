![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![code-style](https://img.shields.io/badge/code--style-black-%23000000)

<h1>Генерация текста на основе сообщений в беседе Вконтакте с помощью цепей Маркова</h1>

> Вдохновлен [Witless](https://vk.com/witless)

<p align="center">Для корректной работы бота установите самую последнюю версию api.
  
### Установка:
```
$ git clone https://github.com/kesha1225/NeuronBot.git

$ pip3 install -r requirements.txt
```
### Настройка(конфиг .env):

###### Отправка случайных сообщений
```python
RANDOM_SEND = 1 
```
###### Размер предложения
```
words = generator.generate(count=random.randint(1, 10)) 
```

###### Токен и айди группы
```python
gid = 123123 #  Айди группы
token = "token" #  Токен
```




## Запуск
```
$ python3 bot.py
```


