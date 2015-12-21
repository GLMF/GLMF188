#!/usr/bin/python
# -*- coding: utf-8 -*-

from rivescript import RiveScript

rs = RiveScript(utf8 = True)
rs.load_directory("./cerveau")
rs.sort_replies()

while True:
    msg = raw_input("Vous > ")
    if msg == '/quit':
        quit()
    reply = u"{0}".format(rs.reply("localuser", msg))
    print(u"Aria > {0}".format(reply))

