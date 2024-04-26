# TestTask Readme

## Install poetry

```sh
curl -sSL https://install.python-poetry.org | python3 -
```

## Create .env file with:
```sh
DB_NAME="DB_NAME"
DB_USER="DB_USER"
DB_PASSWORD="DB_PASSWORD"
DB_HOST="DB_HOST"
DB_PORT="DB_PORT"
```

## Run project
```sh
$ poetry shell; poetry install
$ poetry run python ./internal/run.py
```

## Описание задания
Необходимо написать программу, которая будет получать данные контакта (ID, Имя) из Битрикс24 по Webhook проверять имя контакта на наличие его в БД (PostgreSQL) 

- Женские имена таблица names_woman
- Мужские имена таблица names_man

Далее, если нашел имя в **БД мужчин** ставить пол **Мужчина**, если нашел имя в **БД женщин** ставить **Женщина**

Далее передавать данные по гендеру обратно в контакт по ID
