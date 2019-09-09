#!/usr/bin/env python
import os, sys, subprocess
import json
from os.path import expanduser
HOME = expanduser("~")

class HTDataHandler(object):
    def __init__(self, filepath = HOME+'/.ht_database'):
        self.filepath = filepath
        self.data_dict = dict()

        if os.path.exists(self.filepath):
            with open(self.filepath, 'r') as file:
                self.data_dict = json.loads(file.read())

    def addShortcutAlias(self, alias):
        _, path = subprocess.getstatusoutput("pwd")
        self.data_dict[alias] = path
        self.update()

    def removeShortcutAlias(self, alias):
        if alias in self.data_dict:
            self.data_dict.pop(alias)
        self.update()

    def update(self):
        with open(self.filepath, 'w') as file:
            file.write(json.dumps(self.data_dict))

    def showAll(self):
        for key in sorted(self.data_dict):
            path = self.data_dict[key]
            if key == '-':
                print('there', ' => ', path)
            else:
                print('there-'+key, ' => ', path)

    def generateSourceFile(self):
        alias_source = "#!/bin/bash\n"
        for key in sorted(self.data_dict):
            path = self.data_dict[key]
            if key == '-':
                alias_source += "alias there='cd "+path+"; pwd'\n"
            else:
                alias_source += "alias there-"+key+"='cd "+path+"; pwd'\n"

        with open(HOME+'/.there_source', 'w') as file:
            file.write(alias_source)

if __name__ == "__main__":

    if len(sys.argv) == 1:
        data_io = HTDataHandler()
        data_io.addShortcutAlias('-')
        data_io.showAll()
        data_io.generateSourceFile()

 

    if len(sys.argv) == 2:
        data_io = HTDataHandler()
        if sys.argv[1] == '-l':
            data_io.showAll()
        else:
            data_io.addShortcutAlias(sys.argv[1])
            data_io.showAll()
            data_io.generateSourceFile()

    if len(sys.argv) == 3 and sys.argv[1] == '-D':
        data_io = HTDataHandler()
        data_io.removeShortcutAlias(sys.argv[2])
        data_io.showAll()
        data_io.generateSourceFile()
