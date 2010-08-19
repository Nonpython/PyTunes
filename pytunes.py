#!/usr/bin/env python
import win32com.client as com

class BaseClassOnlyError(Exception):
    "This exception is used for classes that are not for actual use, only \
    as a template for subclassing."

class UnexpectedError(Exception):
    pass

class __Base(object):
    def __init__(self):
        self.wrapped = None
        raise BaseClassOnlyError, "This is just a template class, \
        don't use it except as a template."

class iTunes(__Base):
    "This is the main liTunes COM object wrapper."
    def __init__(self):
        self.wrapped = win32com.client.Dispatch("iTunes.Application")
        

        