"""
backend storage engine
using sqlite3. can switch to any other backend (just keep the same interface)
"""

import sqlite3

class Storage(object):
    """sqlite3 backend stroage
    """
    def __init__(self, dbname='.metadata.sqlite3'):
        """setup sqlite connection.
        use autocommit
        """
        self.__conn__=sqlite3.connect(dbname)
        self.__conn__.isolation_level=None
        self.__cursor__=self.__conn__.cursor()
        self._initdb_()

    def _initdb_(self):
        """init sqlite3 db
        """
        self.__cursor__.execute("create table if not exists data (name text, data char(32) unique)")
        self.__cursor__.execute("create table if not exists metadata (name text unique, data text)")

    def has_key(self, name, data):
        """check if the file with data already exist
        return True if storage already has this data
        return False if data already exist
        """
        try:
            self.__cursor__.execute("insert into data (name, data) values (?, ?)", (name, data))
        except sqlite3.IntegrityError:
            return True
        return False

    def remove_key(self, name=None, data=None):
        """remove a record from storage by name or data or both
        """
        if not name and not data:
            return None
        if name and data:
            self.__cursor__.execute("delete from data where name=? and data=?", (name, data))
        else:
            if name:
                self.__cursor__.execute("delete from data where name=?", (name,))
            else:
                self.__cursor__.execute("delete from data where data=?", (data,))
        return True

    def fetch_key(self, name=None, data=None):
        """fetch record by name or data or both
        return None or sqlite.fetchmany()
        """
        if not name and not data:
            return None
        if name and data:
            self.__cursor__.execute("select name, data from data where name=? and data=?", (name, data))
        else:
            if name:
                self.__cursor__.execute("select name, data from data where name=?", (name, ))
            else:
                self.__cursor__.execute("select name, data from data where data=?", (data, ))
        return self.__cursor__.fetchmany()

    def add_metadata(self, name, data):
        """add metadata
        return True if data saved to stoage
        return False if data already exist
        """
        try:
            self.__cursor__.execute("insert into metadata values (?, ?)", (name, data))
        except sqlite3.IntegrityError:
            return False
        return True

    def remove_metadata(self, name=None, data=None):
        """remove metadata from storage by name, or data or both
        """
        if not name and not data:
            return None
        if name and data:
            self.__cursor__.execute("delete from metadata where name=? and data=?", (name, data))
        else:
            if name:
                self.__cursor__.execute("delete from metadata where name=?", (name,))
            else:
                self.__cursor__.execute("delete from metadata where data=?", (data,))
        return True

    def fetch_metadata(self, name=None, data=None):
        """fetch metadata by name or data or both
        return None or sqlite.fetchmany()
        """
        if not name and not data:
            return None
        if name and data:
            self.__cursor__.execute("select name, data from metadata where name=? and data=?", (name,data))
        else:
            if name:
                self.__cursor__.execute("select name, data from metadata where name=?", (name,))
            else:
                self.__cursor__.execute("select name, data from metadata where data=?", (data,))
        return self.__cursor__.fetchmany()

    def close(self):
        self.__cursor__.close()
        self.__conn__.close()
