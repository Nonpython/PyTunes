#!/usr/bin/env python
import win32com.client
import winerror

class BaseClassOnlyError(Exception):
    "This exception is used for classes that are not for actual use, only \
    as a template for subclassing."

class UnexpectedError(Exception):
    pass

class ReadOnlyError(Exception):
    pass


class __Base(object):
    def __init__(self, wrapped=None):
        self.wrapped = wrapped

class Object(__Base):
    "This wraps IITObject."
    def __getattr__(self, attr):
        if attr == 'Name':
            return str(self.wrapped.Name)
        elif attr == 'Index':
            return str(self.wrapped.Index)
        elif attr == 'PlaylistID':
            return str(self.wrapped.PlaylistID)
        elif attr == 'SourceID':
            return str(self.wrapped.SourceID)
        elif attr == 'TrackDatabaseID':
            return str(self.wrapped.TrackDatabaseID)
        elif attr == 'TrackID':
            return str(self.wrapped.TrackID)
        else:
            raise AttributeError, "'%s' does not exist.".format(attr)
    
    def __setattr__(self, attr, value):
        if attr == 'Name':
            if isinstance(value, basestring):
                self.wrapped.Name = value
            else:
                raise TypeError, "The value of Name must be a 'str' or a \
                'unicode'."
        else:
            raise AttributeError, "'%s' does not exist or it is read only."

class LibraryPlaylist(Object):
    "This is a wrapper for IITLibraryPlaylist. \
    0/0"


class iTunes(__Base):
    "This is the main liTunes COM object wrapper. \
    4/80 methods complete."
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
    
    def LibraryPlaylist(self):
        return LibraryPlaylist(self.wrapped.LibraryPlaylist())