# MountainPass Project
___

## Описание проекта MountainPass

Проект представляет собой систему учёта горных перевалов, включая их создание, обновление, и просмотр. В проекте используются следующие модели:

1. **User**: Пользователь, который может создавать и обновлять перевалы.
2. **Coordinates**: Координаты, связанные с перевалом.
3. **Image**: Изображения, связанные с перевалом.
4. **Level**: Уровни сложности перевала в зависимости от времени года.
5. **Status**: Статус обработки заявки на добавление перевала.
6. **Pass**: Основная модель, представляющая перевал, которая связывает все вышеперечисленные модели.

## Возможности проекта

Проект предоставляет API для работы с этими данными, включая возможность создания, обновления и получения списка всех перевалов с полной информацией о них.

### Проект позволяет:

* **Создавать объект перевала**:
  - Отправка всех данных о перевале. 
  - Автоматически выставляется статус `new`, который в дальнейшем будет изменён после рассмотрения заявки.
  - При создании объекта пользователь идентифицируется по email. 
  - Невозможно создать второго пользователя с аналогичным email. 

* **Редактировать отправленные на сервер данные о перевале**, если они в статусе `new`:
  - Редактировать можно все поля, кроме тех, что содержат в себе ФИО, адрес почты и номер телефона. 
  - Если поле `status` имеет значение, отличное от `new`, редактировать данные об таком объекте нельзя.

* **Просматривать статус модерации для объекта**:
  - Кроме статуса `new`, после рассмотрения возможно присвоение следующих статусов: `pending`, `accepted`, `rejected`.

* **Просматривать список всех перевалов**.

* **Просматривать список перевалов, внесённых одним пользователем по email этого пользователя**:
  - Для этого необходимо передать email этого пользователя как параметр в GET запросе.
  - Например: `http://127.0.0.1:8000/api/v1/passes/?email=qwerty@mail.ru`

## Документация и тестирование API

Более полная документация по API была создана с помощью инструмента **Swagger**. 

Зайдите по адресу:
- _ваш_домен/swagger/_
- _ваш_домен/redoc/_

чтобы ознакомиться с возможностями и протестировать функционал данного API.