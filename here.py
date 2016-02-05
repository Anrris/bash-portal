#!/usr/bin/env python
import sys
import os
import commands

BegThere='# ---- Begin of There operations ----'

def CheckThere(path):
	status, output = commands.getstatusoutput("cat "+path)
	lines = output.split('\n')

	status, pwd = commands.getstatusoutput("pwd")

	is_find=False

	arg='there'
	if len(sys.argv)==2 :
		if sys.argv[1]=="-l":
			print
			for l in xrange(2,len(lines)): print lines[l]
			print
			return lines
		elif sys.argv[1][0]=='-':
			print
			print "Invalid operation: ", sys.argv[1]
			print
			return lines
		else: arg=arg+'-'+sys.argv[1]+'='
	else				:
		arg=arg+'='


	if len(lines)==0:
		lines.append("#!/bin/bash")
		lines.append(BegThere)
		lines.append('alias '+arg+'\'cd '+pwd+'/ ; pwd\'')
	elif len(lines)==1:
		lines[0]="#!/bin/bash"
		lines.append(BegThere)
		lines.append('alias '+arg+'\'cd '+pwd+'/ ; pwd\'')
	elif len(lines)==2:
		lines[0]="#!/bin/bash"
		lines[1]=BegThere
		lines.append('alias '+arg+'\'cd '+pwd+'/ ; pwd\'')
	else:
		for ii in xrange(len(lines)):
			line=lines[ii]
			if line.find(arg) != -1 :
				lines[ii]='alias '+arg+'\'cd '+pwd+'/ ; pwd\''

				print
				for l in xrange(2,len(lines)): print lines[l]
				print

				return lines

		lines.append('alias '+arg+'\'cd '+pwd+'/ ; pwd\'')

		print
		for l in xrange(2,len(lines)): print lines[l]
		print

	return lines


there_path = os.environ.get('PORTAL_PATH')+"/there"
lines=CheckThere(there_path)

there_file=open(there_path,'w')
for line in lines: there_file.write(line+'\n')
there_file.close()

status, output = commands.getstatusoutput("source_there")

