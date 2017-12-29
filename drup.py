#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

import os 
import sys
import json

#https://www.cleancss.com/router-default/

RED = "\033[1;31m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
END = "\033[0m"
WHITE = "\033[1;37m"

def Usage(e=False):
	Banner()
	print "$ python "+sys.argv[0]+" router_name\n"
	print "Example: $ python "+sys.argv[0]+" cisco\n"
	if e: exit()

def Banner():
	print ""
	print "#"*45
	print "# Default Router,Modem,IP Cam Credentials"
	print "#     by "+YELLOW+"Momo Outaadi"+END+" ("+GREEN+"M4ll0k"+END+")"
	print "#"*45+"\n"

def Print():
	return "%s[%s]%s %s%s%s %s%s%s"

def SearchRouter(Router):
	abspath = os.path.abspath(os.path.curdir)
	allrouters = os.listdir(abspath+"/db")
	for router in allrouters:
		if Router == router.split('.')[0]:
			return abspath+"/db/"+router

def ReadJson(Path):
	if Path == None:
		print"%sNot found any vendors with this name!!%s"%(RED,END)
		exit()
	db = open(Path,'rb')
	content = [line.split('\n') for line in db]
	return json.loads(content[0][0],encoding="utf-8")

def Output(Json):
	print Print()%(GREEN,"+",END,RED,"N. Brand:",END,WHITE,Json['info']['name'],END)
	print Print()%(GREEN,"+",END,RED,"Username:",END,WHITE,Json['info']['user'],END)
	print Print()%(GREEN,"+",END,RED,"Password:",END,WHITE,Json['info']['pass'],END)
	print Print()%(GREEN,"+",END,RED,"IP Addrs:",END,WHITE,Json['info']['ip'],END)

def Main(RouterName):
	RouterName = RouterName.lower()
	Banner()
	Output(ReadJson(SearchRouter(RouterName)))

if __name__ == "__main__":
	try:
		Main(sys.argv[1])
	except Exception,e:
		raise
		Usage(True)