#!/usr/bin/python
# coding:UTF-8

# -------------------------------------------------------------------------------------
#                      A SIMPLE PYTHON SCRIPT FILE CHAT CLIENT
#               BY TERENCE BROADBENT BSc CYBER SECURITY (FIRST CLASS)
# -------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0                                                                
# Details : Load required imports.
# Modified: N/A
# -------------------------------------------------------------------------------------

import os
import sys
import socket
import select

# -------------------------------------------------------------------------------------
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub                                                               
# Version : 1.0                                                                
# Details : Display my universal header.
# Modified: N/A                                                               
# -------------------------------------------------------------------------------------

os.system("clear")
print "\t\t\t\t  ____ _   _    _  _____    ____ _     ___ _____ _   _ _____  "
print "\t\t\t\t / ___| | | |  / \|_   _|  / ___| |   |_ _| ____| \ | |_   _| "
print "\t\t\t\t| |   | |_| | / _ \ | |   | |   | |    | ||  _| |  \| | | |   "
print "\t\t\t\t| |___|  _  |/ ___ \| |   | |___| |___ | || |___| |\  | | |   "
print "\t\t\t\t \____|_| |_/_/   \_\_|    \____|_____|___|_____|_| \_| |_|   "
print "\t\t\t\t                                                              "
print "\t\t\t\t   BY TERENCE BROADBENT BSC CYBER SECURITY (FIRST CLASS)    \n"

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0                                                                
# Details : Initialise program variables.
# Modified: N/A
# -------------------------------------------------------------------------------------

if(len(sys.argv) < 3):
   print 'Usage : python client.py hostname port'
   sys.exit()
else:
   host = sys.argv[1]
   port = int(sys.argv[2])

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0                                                                
# Details : Create the functions called from main.
# Modified: N/A
# -------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------
# Main chat client with infinite loop.
# -------------------------------------------------------------------------------------
 
def chat_client():   
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   s.settimeout(2)   
   try :
      s.connect((host, port))
   except :
      print 'Unable to connect?...'
      sys.exit()     

   print 'Sucessfully connected to remote host, you can now start sending messages...\n'
   sys.stdout.write('[Me] ')
   sys.stdout.flush()   

   while 1:
      socket_list = [sys.stdin, s]
      ready_to_read,ready_to_write,in_error = select.select(socket_list , [], [])
      for sock in ready_to_read:
         if sock == s:
            data = sock.recv(4096)			# Use 2048 for quicker responce
            if not data :
               print '\nDisconnected from chat server...'
               sys.exit()
            else :
               sys.stdout.write(data)
               sys.stdout.write('[Me] ')
               sys.stdout.flush()
         else :
            msg = sys.stdin.readline()
            s.send(msg)
            sys.stdout.write('[Me] ')
            sys.stdout.flush() 

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0                                                                
# Details : MAIN - Start the client interface.
# Modified: N/A
# -------------------------------------------------------------------------------------

sys.exit(chat_client())

#Eof
