#!/usr/bin/python
# coding:UTF-8

# -------------------------------------------------------------------------------------
#                     A SIMPLE PYTHON SCRIPT FILE - CHAT CLIENT
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
# Details : Display universal banner.
# Modified: N/A                                                               
# -------------------------------------------------------------------------------------

os.system("clear")
print "  ____ _   _    _  _____    ____ _     ___ _____ _   _ _____  "
print " / ___| | | |  / \|_   _|  / ___| |   |_ _| ____| \ | |_   _| "
print "| |   | |_| | / _ \ | |   | |   | |    | ||  _| |  \| | | |   "
print "| |___|  _  |/ ___ \| |   | |___| |___ | || |___| |\  | | |   "
print " \____|_| |_/_/   \_\_|    \____|_____|___|_____|_| \_| |_|   "
print "                                                              "
print "   BY TERENCE BROADBENT BSC CYBER SECURITY (FIRST CLASS)    \n"

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0                                                                
# Details : Initialise program variables.
# Modified: N/A
# -------------------------------------------------------------------------------------

if(len(sys.argv) < 3):
   print "Usage : python client.py host port"
   sys.exit()
else:
   host = sys.argv[1]
   port = int(sys.argv[2])
   user = "[Me] "

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0                                                                
# Details : Create the functions called from main.
# Modified: N/A
# -------------------------------------------------------------------------------------

def log(msg):
   sys.stdout.write(msg)
   sys.stdout.flush()
 
def client():
   client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   client.settimeout(2)
   try:
      client.connect((host, port))
      log("Sucessfully connected to remote host, you can now start sending messages...\n\n")
      log(user)
   except:
      log("Unable to connect?...\n")
      sys.exit()

   while 1:
      socket_list = [sys.stdin, client]
      ready_to_read,ready_to_write,in_error = select.select(socket_list , [], [])
      for sock in ready_to_read:
         if sock == client:
            data = sock.recv(4096)			# Use 2048 for quicker responce
            if not data:
               log("\n\nDisconnected from chat server?...\n\n")
               sys.exit()
            else :
               log(data)
               log(user)
         else :
            msg = sys.stdin.readline()
            client.send(msg)
            log(user)

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0                                                          	      
# Details : MAIN - Start the client interface.
# Modified: N/A
# -------------------------------------------------------------------------------------

sys.exit(client())

#Eof
