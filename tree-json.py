#!/usr/bin/env python

import os
import json


def all_files(path):
	target_json = []
	for item in os.listdir(path):
		full_path = os.path.join(path,item)
		new_hash = {}
		new_hash['text'] = item
		if os.path.isdir(full_path):
			new_hash['nodes'] = []
			child_dir = all_files(full_path)
			new_hash['nodes'].append(child_dir)
		else:
			new_hash['href'] = full_path.replace(os.getcwd(),'')
		target_json.append(new_hash)
	return target_json

path = os.getcwd()+'/files'
print(json.dumps(all_files(path)))

