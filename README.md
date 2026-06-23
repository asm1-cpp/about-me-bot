# AboutMe AI Bot & Real-Time Log Server

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/License-MIT-success?style=for-the-badge" alt="License">
  <img src="https://img.shields.io/badge/Status-Active-111111?style=for-the-badge" alt="Status">
</p>

> Telegram-бот-портфолио с интеграцией ИИ, работающий параллельно с FastAPI веб-сервером для потоковой передачи логов в режиме реального времени.

---

## О проекте

**AboutMe AI Bot & Real-Time Log Server** — это Telegram-бот, построенный на **aiogram 3.x**, который одновременно запускает локальный веб-сервер на **FastAPI** для просмотра логов приложения.

Главная особенность проекта заключается в том, что **логи полностью находятся в оперативной памяти**. Вместо записи на диск сообщения журнала перехватываются собственным `logging.Handler`, помещаются в `asyncio.Queue` и мгновенно отправляются в браузер через **Server-Sent Events (SSE)**.

Такой подход позволяет наблюдать за состоянием приложения в реальном времени без создания файлов логов.

---

## Стек технологий

<p align="center">
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="56" alt="Python"/>
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/fastapi/fastapi-original.svg" width="56" alt="FastAPI"/>
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/jinja2/jinja2-original.svg" width="56" alt="Jinja2"/>
</p>

| Компонент | Используется |
|-----------|--------------|
| Язык программирования | Python 3.13 |
| Telegram Bot API | aiogram 3.x |
| Веб-сервер | FastAPI |
| ASGI-сервер | Uvicorn |
| HTML-шаблоны | Jinja2 |
| Потоковая передача | Server-Sent Events (SSE) |
| Очередь сообщений | asyncio.Queue |
| CLI | argparse / sys.argv |

---

## Возможности

- Telegram-бот-портфолио с интеграцией ИИ.
- Одновременный запуск Telegram-бота и FastAPI веб-сервера.
- Потоковая передача логов в режиме реального времени.
- Полное отсутствие записи логов на жесткий диск.
- Использование собственного `logging.Handler` для перехвата сообщений.
- Передача логов через `asyncio.Queue`, расположенную в оперативной памяти.
- Минималистичный веб-интерфейс в стиле терминала.
- Разделение сообщений по вкладкам:
  - `INFO`
  - `DEBUG`
  - `ERROR`
- Управление режимами работы через параметры командной строки.

---

# Установка

## Требования

| Необходимое ПО | Версия |
|----------------|---------|
| Python | 3.13 |
| pip | Рекомендуется последняя версия |

---

## Linux (Arch / Debian)

Создайте виртуальное окружение и установите зависимости.

```bash
python3 -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt
```

---

## macOS

Для **zsh** и **bash** используются одинаковые команды.

```bash
python3 -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt
```

---

## Windows

Создайте виртуальное окружение.

```powershell
python -m venv .venv
```

Активируйте его.

```powershell
.venv\Scripts\activate
```

Установите зависимости.

```powershell
pip install -r requirements.txt
```

---

# Настройка окружения

В корне проекта необходимо создать файл `.env`.

```env
TOKEN=ВАШ_ТОКЕН_БОТА
```

Если при запуске используется параметр `--token`, то значение из командной строки имеет приоритет над переменной `TOKEN` из файла `.env`.

---

# Запуск

## Обычный запуск

```bash
python main.py
```

Бот запускается с использованием токена из файла `.env`.

---

## Запуск с уровнем логирования DEBUG

```bash
python main.py --debug
```

Все сообщения уровня `DEBUG` начинают отображаться в журнале.

---

## Запуск веб-сервера

```bash
python main.py --site
```

Дополнительно запускается FastAPI-сервер в фоновом потоке.

После запуска веб-интерфейс будет доступен по адресу:

```text
http://127.0.0.1:8000
```

---

## Запуск веб-сервера с DEBUG

```bash
python main.py --site --debug
```

После запуска откройте браузер и перейдите по адресу:

```text
http://127.0.0.1:8000
```

Все новые сообщения будут появляться в веб-интерфейсе практически мгновенно благодаря технологии **Server-Sent Events (SSE)**.

Интерфейс содержит три вкладки:

- `INFO`
- `DEBUG`
- `ERROR`

---

## Передача токена через терминал

```bash
python main.py --token ВАШ_ТОКЕН
```

В этом случае токен будет использован напрямую, без чтения переменной `TOKEN` из `.env`.

---

## Комбинирование параметров

Все параметры можно использовать одновременно.

```bash
python main.py --site --debug --token ВАШ_ТОКЕН
```

| Параметр | Назначение |
|----------|------------|
| `--site` | Запускает веб-сервер на `http://127.0.0.1:8000` в фоновом потоке. |
| `--debug` | Включает уровень логирования `DEBUG`. |
| `--token <ТОКЕН>` | Передает токен напрямую через командную строку. |

---

# Архитектура

> Telegram-бот и веб-сервер работают одновременно внутри одного процесса, а обмен логами осуществляется через очередь в оперативной памяти.

```text
Telegram
    │
    ▼
aiogram Bot
    │
    ▼
Python logging
    │
    ▼
Custom logging.Handler
    │
    ▼
asyncio.Queue
    │
    ▼
FastAPI
    │
    ▼
Server-Sent Events (SSE)
    │
    ▼
Web Terminal
```

После формирования сообщения модуль `logging` передает его в собственный `logging.Handler`. Обработчик помещает запись в `asyncio.Queue`, не создавая файлов на диске. FastAPI получает новые элементы очереди и транслирует их в браузер через **Server-Sent Events**, где они отображаются в минималистичном веб-терминале с вкладками `INFO`, `DEBUG` и `ERROR`.

---

# Лицензия

Проект распространяется по лицензии **MIT**.

Подробные условия использования находятся в файле `LICENSE`.
````
