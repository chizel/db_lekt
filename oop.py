import shutil
import time
import os
import sys
import getopt

class db:
    data = []
    def __init__(self, path):
        self.path = path

    def add_item(self, key, value):
        """add item to list"""
        new_item = {'key':key, 'value':value}
        self.data.append(new_item)
        log = 'add "' + key + '" "' + value + '"\n'
        self.write_log(log)

    def remove_item(self, type_to_remove, what_remove):
        """Remove first entry"""
        #type_to_remove can be key or value
        #is type exist
        if type_to_remove not in self.data[0]:
            return 0
        for i in range(0, len(self.data)):
            if self.data[i][type_to_remove] == what_remove:
                del self.data[i]
                log = 'remove "' + type_to_remove + '"="' + what_remove + '"\n'
                self.write_log(log)
                return 1
        return 0

    def view_items(self, what_type, what_need):
        '''view all items 
        what_type can be "key" or "value"'''
        #is type exist
        if what_type not in self.data[0]:
            return 0
        for item in self.data:
            if item[what_type] == what_need:
                print item
        return 1

    def search_item(self, type_need, what_need):
        """Search string in list"""
        #is type exist
        if type_to_remove not in data[0]:
            return 0
        for i in range(0, len(data)):
            if data[0][type_need] == what_need:
                return 1
        return 0

    def parse(self, str_data):
        """Parse input string to commands"""
        commands = str_data.split()
        if commands[0] == 'add':
            #add "key" "value"
            self.add_item(commands[1][1:-1], commands[2][1:-1])
        elif commands[0] == 'remove':
            #remove "name"="Tom"
            commands = commands[1].split('"')
            self.remove_item(commands[1], commands[3])
        #update where "name"="Tom" set "name"="Tin"
        #elif commands[0] == 'update':
            #print 'update'
        else:
            print 'ERROR! Not exist command: "' + commands[0] + '"!\n'
            return 0
        return 1

    def write_log(self, log):
        '''write changes in log-file'''
        full_file_name = self.path + 'db_log.txt'
        if os.path.exists(full_file_name):
            f = file(full_file_name, 'a')
        else:
            try:
                f = file(full_file_name, 'w')
            except IOError:
                print "Error! Can't open '" + full_file_name + "'!\n"
                return 0
        f.write(log)
        f.close()
        return 1

    def restore_data_from_log(self):
        '''restore data from log file'''
        print 'Warning! All database will be replaced by log file!(y/n)'
        answer = raw_input()
        if answer.lower() != 'y':
            return 0
        date = time.strftime("%Y-%m-%d_%H:%M:%S")
        full_file_name = self.path + 'db_log.txt'
        log_backup = self.path + 'db_log_copied_' + date + '.txt'
        if os.path.exists(full_file_name):
            #make copy of log
            shutil.copy(full_file_name, log_backup)
        else:
            print 'Error! File "' + full_file_name + '" doesn\'t exist!\n'
            return 0
        #delete all date from db
        self.data = []
        f = open(full_file_name, 'w')
        f.close()
        f = open(log_backup, 'r')
        for line in f:
            self.parse(line)
        f.close()
        return 1

    def write_backup(self):
        date = time.strftime("%Y-%m-%d_%H:%M:%S")
        full_file_name = self.path + 'backup.txt'
        #make copy of previous backup 
        if os.path.exists(full_file_name):
            shutil.copy(full_file_name, self.path + 'backup_copied_' + date + '.txt')
        f = open(full_file_name, 'w')
        for i in self.data:
            str_data = 'add "' + i['key'] + '" "' + i['value'] + '\n'
            f.write(str_data)
        f.close()
        return 1

    #!!!add posibility to choose backup version
    def restore_data_from_backup(self):
        print 'Warning! All database will be erased  and restored from last backup file!(y/n)'
        answer = raw_input()
        if answer.lower() != 'y':
            return 0
        full_file_name = self.path + 'backup.txt'
        #is backup exist?
        if os.path.exists(full_file_name):
            f = file(full_file_name, 'r')
        else:
            print "Error! Can't open '" + full_file_name + "'!\n"
            return 0
        date = time.strftime("%Y-%m-%d_%H:%M:%S")
        self.data = []
        f = open(full_file_name, 'r')
        for line in f:
            self.parse(line)
        f.close()
        return 1

    def console_input(self):
        print 'Type command (key and values must be in quotes:\n'
        string = raw_input()
        self.parse(string)

    def http_input(self):
        print 'later :)'


PATH = '/home/d/Dropbox/git/python/db/'
PARENT = 1

#try:
    #opts, args = getopt.getopt(sys.argv[1:], 'c')
    #print opts
    #print 'ddddd'
    #print args
#except getopt.GetoptError:
    #print 'Error!'
#if PARENT:
    #PARENT = 0
    #print 'I\'m parent!'
    #os.system('oop.py')
##run childs
#chekcing is children alive
#select whom send data
mydb = db(PATH)
mydb.add_item('ggg', 'hhh')
mydb.console_input()
print mydb.data
mydb.view_items('key', 'ggg')

#print str(sys.argv)
