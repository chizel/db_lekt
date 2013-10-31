import shutil
import time
import os

PATH = '/home/d/Dropbox/git/python/db/'

def add_item(list_of_items, key, value):
    """add item to list"""
    new_item = {'key':key, 'value':value}
    list_of_items.append(new_item)
    data = 'add "' + key + '" "' + value + '"\n'
    write_log(data)

def remove_item(list_of_items, type_to_remove, what_remove):
    """Remove first entry"""
    #type_to_remove can be key or value
    #is type exist
    if type_to_remove not in list_of_items[0]:
        return 0
    for i in range(0, len(list_of_items)):
        if list_of_items[i][type_to_remove] == what_remove:
            del list_of_items[i]
            data = 'remove "' + type_to_remove + '"="' + what_remove + '"\n'
            write_log(data)
            return 1
    return 0

def search_item(list_of_items, type_need, what_need):
    """Search string in list"""
    #is type exist
    if type_to_remove not in list_of_items[0]:
        return 0
    for i in rage(0, len(list_of_items)):
        if list_of_items[0][type_need] == what_need:
            return 1
    return 0

def parse(list_of_items, data):
    """Parse input string to commands"""
    commands = data.split()
    if commands[0] == 'add':
        #add "key" "value"
        add_item(list_of_items, commands[1][1:-1], commands[2][1:-1])
    elif commands[0] == 'remove':
        #remove "name"="Tom"
        commands = commands[1].split('"')
        remove_item(list_of_items, commands[1], commands[3])
    #update where "name"="Tom" set "name"="Tin"
    #elif commands[0] == 'update':
        #print 'update'
    else:
        print 'ERROR! Not exist command: "' + commands[0] + '"!\n'
        return 0
    return 1

def write_log(data):
    '''write changes in log-file'''
    full_file_name = PATH + 'db_log.txt'
    if os.path.exists(full_file_name):
        f = file(full_file_name, 'a')
    else:
        try:
            f = file(full_file_name, 'w')
        except IOError:
            print "Error! Can't open '" + full_file_name + "'!\n"
            return 0
    f.write(data)
    f.close()
    return 1

def restore_data_from_log(list_of_items):
    '''restore data from log file'''
    print 'Warning! All database will be replaced by log file!(y/n)'
    answer = raw_input()
    if answer.lower() != 'y':
        return 0
    date = time.strftime("%Y-%m-%d_%H:%M:%S")
    full_file_name = PATH + 'db_log.txt'
    log_backup = PATH + 'db_log_copied_' + date + '.txt'
    if os.path.exists(full_file_name):
        #make copy of log
        shutil.copy(full_file_name, log_backup)
    else:
        print 'Error! File "' + full_file_name + '" doesn\'t exist!\n'
        return 0
    #delete all date from db
    list_of_items = []
    f = open(full_file_name, 'w')
    f.close()
    f = open(log_backup, 'r')
    for line in f:
        parse(list_of_items, line)
    f.close()
    return list_of_items

def write_backup(list_of_items):
    date = time.strftime("%Y-%m-%d_%H:%M:%S")
    full_file_name = PATH + 'backup.txt'
    #make copy of previous backup 
    if os.path.exists(full_file_name):
        shutil.copy(full_file_name, PATH + 'backup_copied_' + date + '.txt')
    f = open(full_file_name, 'w')
    for i in list_of_items:
        data = 'add "' + i['key'] + '" "' + i['value'] + '\n'
        f.write(data)
    f.close()
    return 1

#!!!add posibility to choose backup version
def restore_data_from_backup(list_of_items):
    print 'Warning! All database will be erased  and restored from last backup file!(y/n)'
    answer = raw_input()
    if answer.lower() != 'y':
        return 0
    full_file_name = PATH + 'backup.txt'
    #is backup exist?
    if os.path.exists(full_file_name):
        f = file(full_file_name, 'r')
    else:
        print "Error! Can't open '" + full_file_name + "'!\n"
        return 0
    date = time.strftime("%Y-%m-%d_%H:%M:%S")
    list_of_items = []
    f = open(full, 'r')
    for line in f:
        parse(line, list_of_items)
    f.close()
    return list_of_items

def console(list_of_items):
    print 'Type command (key and values must be in quotes:\n'
    string = raw_input()
    parse(list_of_items, string)

list_of_items = []
console(list_of_items)
#add_item(list_of_items, 'a', 'b')
#add_item(list_of_items, 'c', 'd')
#add_item(list_of_items, 'e', 'f')
#parse(list_of_items, "add 'den' '21'")
#parse(list_of_items, "add 'need' 'cola'")
#parse(list_of_items, "add 'wish' 'vacation'")
#print list_of_items
#remove_item(list_of_items, 'key','c')
#print list_of_items
#remove_item(list_of_items, 'value','f')
#print list_of_items
#parse(list_of_items, "remove 'value'=='vacation'")
#list_of_items = restore_data_from_log(list_of_items)
#write_backup(list_of_items)
#list_of_items = restore_data_from_backup(list_of_items)
#string_for_search = raw_input("Type what you search:\n")
#if search_item(list_of_items, string_for_search):
    #print "Find!\n"
#else:
    #print "Can`t find!\n"
