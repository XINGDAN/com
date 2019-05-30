#! /usr/bin/env python
#coding=utf-8

import sys
import logging
import os
import pytest

# Add src root dirctory to PYTHONPATH by extend sys.path
sys.path.append(os.path.dirname(sys.modules[__name__].__file__))
from initialization import sysconfig #这个必须放在这里的位置

fileHandler = logging.FileHandler(filename="../log/auto.log",encoding="utf-8")
logging.getLogger().setLevel(0)
formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(module)s %(lineno)s')
fileHandler.setFormatter(formatter)

logging.getLogger().addHandler(fileHandler)

if __name__ == '__main__':
    logging.info("Start to execute automation cases")
    #BuildUpDriver.build_up_driver()

    pytest.main(['-sq','testcases/contact/department/test_create_dep.py'])






