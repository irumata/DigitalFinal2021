# DigitalFinal2021
# (c) Copyright Использование данных материалов разрешается исключительно в целях хакатона и только до 05/12/2021


Cервис работы с карточками стартапов и решний, включающий умный поиск по карточкам решениям, проверку новостей в интернете
Умный поиск реализован c помощью нейросети alexnet и сравнениями эмбеддингов запроса и частей документа с целью найти подходящую часть. 

1. Поиск по организациям;
2. Отображение карточки организации;
3. Поиск по новостям, связанным с организацияй

Особенность проекта в следующем:

1. Нейронная сеть, ищущая необходимые проекты и организации по смыслу запроса
2. Поиск в интеренете новостей связанных с организацией и обогащение информации о проекте
3. Продумана работа разных пользователей: Заказчика, администратора, члена организации

Основной стек технологий:

Python, Flask
tensorflow, keras
HTML, CSS, JavaScript, TypeScript.
Git, GitHub.
Демо

Доступно по адресу http://ailine.softline.com:8501

Пользователь testuser
Пароль 4680

R
СРЕДА ЗАПУСКА

развертывание сервиса производится на debian-like linux (debian 9+);
требуется установленный python, flask, streamlit, другие пакеты указанные в requirements.txt


Выполнить:
Запуск ноутбука для создания словарей, базы данных
Запуск сервера streamlit run proj_search.py

РАЗРАБОТЧИКИ

Князев Николай fullstack Data Scientist
Александр Веретенников Data Scientist
Владислав Глебов  подготовка данных
Артемий Гушин backend


