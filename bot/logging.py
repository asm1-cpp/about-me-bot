import logging
import sys
import threading
import uvicorn
import config
from web.server import log_queues

class QueueHandler(logging.Handler):
    def emit(self, record):
        try:
            message = self.format(record)
            level = record.levelname
            
            if level == "DEBUG":
                log_queues["DEBUG"].put_nowait(message)
            elif level == "INFO":
                log_queues["INFO"].put_nowait(message)
                log_queues["DEBUG"].put_nowait(message)
            elif level == "ERROR":
                log_queues["ERROR"].put_nowait(message)
                log_queues["DEBUG"].put_nowait(message)
                log_queues["INFO"].put_nowait(message)
        except Exception:
            self.handleError(record)

def get_arg(index):
    try:
        return sys.argv[index]
    except IndexError:
        return "NULL"

def run_site():
    uvicorn.run("web.server:app", host="127.0.0.1", port=8000, log_level="warning")

def starting():
    arg_1 = get_arg(1)
    arg_2 = get_arg(2)
    arg_3 = get_arg(3)
    arg_4 = get_arg(4)

    log_format = u'%(levelname)-8s [%(asctime)s] %(message)s'
    
    if "--site" in sys.argv:
        site_thread = threading.Thread(target=run_site, daemon=True)
        site_thread.start()
    current_level = logging.INFO

    if len(sys.argv) == 1:
        logging.basicConfig(level=current_level, format=log_format, handlers=[logging.StreamHandler(sys.stdout), QueueHandler()])
        logging.info("Бот запущен в обычном режиме с токеном из .env")
        return

    try:
        if '--debug' in sys.argv:
            current_level = logging.DEBUG

        logging.basicConfig(
            format=log_format, 
            level=current_level, 
            force=True,
            handlers=[
                logging.StreamHandler(sys.stdout),
                QueueHandler()
            ]
        )

        if '--debug' in sys.argv:
            logging.info("Дебаг-режим включен.")

        # Разбор токенов и сайта (твоя оригинальная логика без изменений)
        if arg_1 == '--debug':
            if arg_2 != "NULL" and arg_2 == '--token':
                config.TOKEN = arg_3
                if config.TOKEN == "NULL":
                    logging.error("ERROR: Где токен?")
                    exit()
                else:
                    logging.info("Ваш токен присвоен к боту")
                    if arg_4 != "NULL" and arg_4 != '--site':
                        logging.error("ERROR: Такого флага не существует или ты его уже использовал")
                        exit()
            elif arg_2 == '--site' and arg_3 != "NULL" and arg_4 == "NULL":
                logging.error("ERROR: Где токен?")
                exit()
            elif arg_2 == '--site' and arg_3 != "NULL" and arg_4 != "NULL":
                config.TOKEN = arg_4
                logging.info("Ваш токен присвоен к боту")

        elif arg_1 == '--token':
            if arg_2 != "NULL":
                config.TOKEN = arg_2
                logging.info("Ваш токен присвоен к боту")
                if arg_3 != "NULL":
                    if arg_3 == '--debug':
                        if arg_4 != "NULL" and arg_4 != '--site':
                            logging.error("ERROR: Такого флага нету или ты его уже использовал")
                            exit()
                    elif arg_3 == '--site' and arg_4 != "NULL" and arg_4 != "--debug":
                        logging.error("ERROR: Такого флага нету или ты его уже использовал")
                        exit()
            else:
                logging.error("ERROR: Где токен?")
                exit()
    
        elif arg_1 == '--site':
            logging.info("Сайт запущен вместе с ботом по адресу 127.0.0.1:8000")
            if arg_2 != "NULL":
                if arg_2 == '--token':
                    if arg_3 != "NULL":
                        config.TOKEN = arg_3
                        logging.info("Ваш токен присвоен к боту")
                        if arg_4 != "NULL" and arg_4 != '--debug':
                            logging.error("ERROR: Такого флага нету или ты его уже использовал")
                            exit()
                    else:
                        logging.error("ERROR: Где токен?")
                        exit()
                elif arg_2 == '--debug':
                    if arg_3 != "NULL" and arg_3 == '--token':
                        if arg_4 != "NULL":
                            config.TOKEN = arg_4
                            logging.info("Ваш токен присвоен к боту")
                        else:
                            logging.error("ERROR: Где токен?")
                            exit()
        else:
            logging.error("ERROR: Такого флага нету")
            exit()

    except Exception as e:
        logging.error(f"ERROR: {e}")
        exit()
