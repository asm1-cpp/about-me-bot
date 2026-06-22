import logging
import sys
from config import TOKEN

arg_1 = sys.argv[1] or "NULL"
arg_2 = sys.argv[2] or "NULL"
arg_3 = sys.argv[3] or "NULL"
arg_4 = sys.argv[4] or "NULL"

def starting():
    try:
        if arg_1 == '--debug':
            logging.basicConfig(format = u'%(levelname)-8s [%(asctime)s] %(message)s', level = logging.DEBUG, filename = u'bot_log.log')
            logging.info("Дебаг-режим включен.")
            if arg_2 != "NULL":
                if arg_2 == '--token':
                    TOKEN = arg_3
                    if TOKEN == "NULL":
                        logging.error("ERROR: Где токен?")
                        exit()
                    else:
                        logging.info("Ваш токен присвоен к боту")
                        if arg_4 != "NULL":
                            if arg_4 == '--site':
                                logging.info("Сайт запущен вместе с ботом по адресу 127.0.0.1:8000")
                            else:
                                logging.error("ERROR: Такого флага не существует или ты его уже использовал")
                                exit()
                        else:
                            logging.error("ERROR: Такого флага не существует или ты его уже использовал")
                            exit()
                elif arg_2 == '--site':
                    if arg_3 != "NULL":
                        if arg_4 == "NULL":
                            logging.error("ERROR: Где токен?")
                            exit()
                        else:
                            TOKEN = arg_4
                            logging.info("Ваш токен присвоен к боту")
                else:
                    logging.error("ERROR: Такого флага нету или вы его уже использовали")
                    exit()

        elif arg_1 == '--token':
            if arg_2 != "NULL":
                TOKEN = arg_2
                logging.info("Ваш токен присвоен к боту")
                if arg_3 != "NULL":
                    if arg_3 == '--debug':
                        logging.basicConfig(format = u'%(levelname)-8s [%(asctime)s] %(message)s', level = logging.DEBUG, filename = u'bot_log.log')
                        logging.info("Дебаг-режим включен.")
                        if arg_4 != "NULL":
                            if arg_4 == '--site':
                                logging.info("Сайт запущен вместе с ботом по адресу 127.0.0.1:8000")
                            else:
                                logging.error("ERROR: Такого флага нету или ты его уже использовал")
                                exit()
                    elif arg_3 == '--site':
                        logging.info("Сайт запущен вместе с ботом по адресу 127.0.0.1:8000")
                        if arg_4 != "NULL":
                            if arg_4 =="--debug":
                                logging.basicConfig(format = u'%(levelname)-8s [%(asctime)s] %(message)s', level = logging.DEBUG, filename = u'bot_log.log')
                                logging.info("Дебаг-режим включен.")
                            else:
                                logging.error("ERROR: Такого флага нету или ты его уже использовал")
                                exit()
                    else:
                        logging.error("ERROR: Такого флага нету или вы его уже использовали")
                        exit()
            else:
                logging.error("ERROR: Где токен?")
                exit()
    
        
        elif arg_1 == '--site':
            logging.info("Сайт запущен вместе с ботом по адресу 127.0.0.1")
            if arg_2 != "NULL":
                if arg_2 == '--token':
                    if arg_3 != "NULL":
                        TOKEN = arg_3
                        logging.info("Ваш токен присвоен к боту")
                        if arg_4 != "NULL":
                            if arg_4 == '--debug':
                                logging.basicConfig(format = u'%(levelname)-8s [%(asctime)s] %(message)s', level = logging.DEBUG, filename = u'bot_log.log')
                                logging.info("Дебаг-режим включен.")
                        else:
                            logging.error("ERROR: Такого флага нету или ты его уже использовал")
                            exit()
                    else:
                        logging.error("ERROR: Где токен?")
                        exit()
                elif arg_2 == '--debug':
                    logging.basicConfig(format = u'%(levelname)-8s [%(asctime)s] %(message)s', level = logging.DEBUG, filename = u'bot_log.log')
                    logging.info("Дебаг-режим включен.")
                    if arg_3 != "NULL":
                        if arg_3 == '--token':
                            if arg_4 != "NULL":
                                TOKEN = arg_4
                                logging.info("Ваш токен присвоен к боту")
                            else:
                                logging.error("ERROR: Где токен?")
                                exit()
                else:
                    logging.error("ERROR: Такого флага нету или вы его уже использовали")
                    exit()
        else:
            logging.error("ERROR: Такого флага нету")
            exit()

    except Exception as e:
        logging.error(f"ERROR: {e}")
