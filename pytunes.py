#!/usr/bin/env python
import win32com.client as com

class BaseClassOnlyError(Exception):
    "This exception is used for classes that are not for actual use, only \
    as a template for subclassing."

class UnexpectedError(Exception):
    pass

