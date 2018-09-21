#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 9/22/18 1:53 AM

import chardet


class Compatibility(object):

    @staticmethod
    def str2byte(string):
        encode_type = chardet.detect(string)
        # 进行相应解码，赋给原标识符（变量）
        return string.decode(encode_type['encoding'])

    @staticmethod
    def byte2str(byte):
        encode_type = chardet.detect(byte)
        # 进行相应编码，赋给原变量
        return byte.encode(encode_type['encoding'])
