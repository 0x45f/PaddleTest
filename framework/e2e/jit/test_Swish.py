#!/bin/env python
# -*- coding: utf-8 -*-
# encoding=utf-8 vi:ts=4:sw=4:expandtab:ft=python
"""
test jit cases
"""

import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(os.getcwd())))
sys.path.append(os.path.join(os.path.abspath(os.path.dirname(os.getcwd())), "utils"))

from utils.yaml_loader import YamlLoader
from jittrans import JitTrans

yaml_path = os.path.join(os.path.abspath(os.path.dirname(os.getcwd())), "yaml", "nn.yml")
yml = YamlLoader(yaml_path)


def test_Swish_base():
    """test Swish_base"""
    jit_case = JitTrans(case=yml.get_case_info("Swish_base"))
    jit_case.jit_run()


def test_Swish_0():
    """test Swish_0"""
    jit_case = JitTrans(case=yml.get_case_info("Swish_0"))
    jit_case.jit_run()


def test_Swish_1():
    """test Swish_1"""
    jit_case = JitTrans(case=yml.get_case_info("Swish_1"))
    jit_case.jit_run()
