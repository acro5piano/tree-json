#!/usr/bin/env python

import os
import json

def json_tree(path):
    target_json = []
    for item in os.listdir(path):
        full_path = os.path.join(path,item)
        new_hash = {}
        new_hash['text'] = item
        if os.path.isdir(full_path):
            #new_hash['nodes'] = []
            child_dir = json_tree(full_path)
            new_hash['nodes'] = child_dir
        else:
            new_hash['href'] = full_path.replace(os.getcwd(),'')
        target_json.append(new_hash)
    return target_json

if __name__ == '__main__':
    path = os.getcwd()+'/files'
    print(json.dumps(json_tree(path)))

