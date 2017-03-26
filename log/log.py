# -*- coding: utf-8 -*-

import logging

class Log(logging.Logger):
    def __init__(self, name, level=logging.NOTSET):
        logging.Logger(name, level)
        # logging.basicConfig(filename='logger.log', level=logging.INFO)


