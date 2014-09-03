# -*- coding: utf-8 -*-
from PyQt4 import QtCore


def save_platform_keys(keys):
    keys_content = '# -*- coding: utf-8 -*-\n[\n'
    for key in keys:
        keys_content += (str(key) + ",\n")
    keys_content = keys_content[0:keys_content.rindex(',')] + '\n'
    keys_content += ']'
    file = open('config/platform_keys.py', 'w')
    file.write(keys_content)
    file.close()
    return None


def read_config_keys():
    file = open('config/platform_keys.py', 'r')
    all_keys_text = file.read()
    return eval(all_keys_text)
