#!/usr/bin/env python
import win32com.client
import winerror

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
    "This is the main liTunes COM object wrapper. \
    3/80 methods complete."
    def __init__(self):
        self.wrapped = win32com.client.Dispatch("iTunes.Application")
        
    def BackTrack(self):
        "Reposition to the beginning of the current track or go to the previous track if already at start of current track."
        returned = self.wrapped.BackTrack()
        if returned != winerror.E_FAIL:
            raise UnexpectedError
        return True
        
    def Play(self):
        "Play the currently targeted track."
        returned = self.wrapped.Play()
        if returned != winerror.E_FAIL:
            raise UnexpectedError
        return True
        
    def PlayPause(self):
        returned = self.wrapped.PlayPause()
        if returned != winerror.E_FAIL:
            raise UnexpectedError
        return True
    
    