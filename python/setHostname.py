#!/usr/bin/python

def doCommands(verb, argument):
    for pref in prefsList:
        scutil_command = "scutil --" + verb + " " + pref + " " + argument
        print(scutil_command)
        os.system(scutil_command)
        print

import os, sys

if len(sys.argv) != 2:
    print "please provide a new hostname"
    sys.exit(1)

prefsList = ["ComputerName", "LocalHostName", "HostName"]

print("machine's current names are:")
print
doCommands("get", "")

print("setting names:")
print
doCommands("set", sys.argv[1])

print("machine's new names are:")
print
doCommands("get", "")
