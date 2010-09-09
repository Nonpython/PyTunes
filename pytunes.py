#!/usr/bin/env python
import win32com.client
import winerror
import support.singleton as singleton

class UnexpectedError(Exception):
    pass

class ReadOnlyError(Exception):
    pass


class __Base(object):
    pass

class Object(__Base):
    "This wraps IITObject."
    ROSlices = {
        'Index': lambda: str(self.wrapped.Index),
        'PlaylistID': lambda: str(self.wrapped.PlaylistID),
        'SourceID': lambda: str(self.wrapped.SourceID),
        'TrackDatabaseID': lambda: str(self.wrapped.TrackDatabaseID),
        'TrackID': lambda: str(self.wrapped.TrackID)
        }
    
    def _nameslice(self, x):
        if x is not None:
            self.wrapped.Name = x
            return self.wrapped.Name
        else:
            return self.wrapped.Name
    
    RWSlices = {'Name': lambda x: self._nameslice}
    
    def __getitem__(self, key):
        try:
            return ROSlices[key]()
        except KeyError:
            raise KeyError, "'%s' is not a valid property." % (key)
    
    def __setitem__(self, key, value):
        try:
            RWSlices[key](value)
            return ROSlices[key]()
        except KeyError:
            raise KeyError, "'%s' is not a valid property or it is read only." % (key)

class LibraryPlaylist(Object):
    "This is a wrapper for IITLibraryPlaylist. \
    0/0"
    


class iTunes(__Base, singleton.Singleton):
    "This is the main liTunes COM object wrapper. \
    4/80 methods complete."
    def __init__(self):
        self.wrapped = win32com.client.Dispatch("iTunes.Application")
        
    def BackTrack(self):
        "Reposition to the beginning of the current track or go to the previous \
track if already at start of current track."
        returned = self.wrapped.BackTrack()
        if returned == winerror.E_FAIL:
            raise UnexpectedError
        return True
        
    def Play(self):
        "Play the currently targeted track."
        returned = self.wrapped.Play()
        if returned == winerror.E_FAIL:
            raise UnexpectedError
        return True
        
    def PlayPause(self):
        returned = self.wrapped.PlayPause()
        if returned == winerror.E_FAIL:
            raise UnexpectedError
        return True
    
    def LibraryPlaylist(self):
        return LibraryPlaylist(self.wrapped.LibraryPlaylist())