# This program find changes in data.db file after regular intervals and if change found then do specific task


import os, time
from md5hash import scan
import json


# empty file hash 
# D41D8CD98F00B204E9800998ECF8427E
old_hash = ""
new_hash = ""

def parsing():
	print("Task to perform after detect changes")

def hash_find():
	hash_value = scan('data.db')
	return hash_value

def hash_write(hash_value):
	hash_write = open('hash.txt','w')
	hash_write.write(hash_value)
	hash_write.close()

def hash_compare():
	global old_hash
	global new_hash

	obj = open('hash.txt','r')
	old_hash = obj.readline()
	new_hash = hash_find()

	if old_hash == new_hash:
		print("SAME HASH")
		print(old_hash, new_hash) 
		# hash_write(new_hash)

	else:
		parsing()
		hash_write(new_hash)


def main():
	hash_compare()

new_hash = hash_find()
hash_write(new_hash)

while True:
	main()
	time.sleep(10)
