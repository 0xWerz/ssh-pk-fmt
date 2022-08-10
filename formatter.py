#!/usr/bin/python3

import os, sys, stat, subprocess
from colorama import Fore
y = Fore.LIGHTYELLOW_EX
b = Fore.LIGHTBLUE_EX
r = Fore.RED
g = Fore.GREEN

if len(sys.argv) > 3:
    print(f'{r}You have specified too many arguments')
    sys.exit()
if len(sys.argv) < 2:
    print(f'{r}You need to specify a file | {g}-h or --help for help page')
    sys.exit()
misformatted_file = sys.argv[1]
if misformatted_file == '-h'or misformatted_file == '--help':
        print(f'{g}./sshfix.py mis_formatted_file.txt output_file\n\nExample: ./sshfix.py id_rsa id_rsa')
        exit()
else:
    pass
try:
    output_file = sys.argv[2]
except:
    output_file = misformatted_file
    pass
if not os.path.isfile(misformatted_file):
    print(f'{r}The file or path specified does not exist |{g} -h or --help for help page')

def space_by_70_char(content):
    return '\n'.join([content[i:i + 70] for i in range(0, len(content), 70)])
try:
    with open(misformatted_file, encoding='utf8') as f:
        content = f.read().replace('-----BEGIN OPENSSH PRIVATE KEY-----', '').replace('-----END OPENSSH PRIVATE KEY-----', '').replace('\n', '').replace(' ', '').replace('  ', '')
        key = space_by_70_char(content)
        with open(output_file,'w', encoding='utf8') as output_file:
            first_line = '-----BEGIN OPENSSH PRIVATE KEY-----'
            last_line = '-----END OPENSSH PRIVATE KEY-----'
            output_file.write(first_line +'\n' + key + '\n' + last_line)
            print(f'{b}File formatted and ready for use.')
            cmd = f'chmod 600 {output_file.name}'
            os.system(cmd)
except:
    exit()
