#!/usr/bin/env python
# -*- coding: utf-8 -*-

while True:
    command = input(">")
    if command == 'version':
        print('1.0')
    elif command == 'help':
        print('commands: version, help. exit')
    elif command == 'exit:':
        break
    else:
        print("unknown command")
