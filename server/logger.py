import json
import logging

from server.config import get_config

def init_logger(name: str):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    logs_path = get_config('logs_path')
    # 建立一个filehandler来把日志记录在文件里，级别为debug以上
    fh = logging.FileHandler(logs_path+name+".log")
    fh.setLevel(logging.DEBUG)
    # 建立一个streamhandler来把日志打在CMD窗口上，级别为error以上
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    # 设置日志格式
    formatter = logging.Formatter(
        "%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s - %(message)s")
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)
    # 将相应的handler添加在logger对象中
    # logger.addHandler(ch)
    logger.addHandler(fh)
    return logger
