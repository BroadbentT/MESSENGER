#!/usr/bin/python
# coding:UTF-8

# -------------------------------------------------------------------------------------
#                     A SIMPLE PYTHON SCRIPT FILE CHAT SERVER
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
from datetime import datetime

# -------------------------------------------------------------------------------------
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub                                                               
# Version : 1.0                                                                
# Details : Display universal header.
# Modified: N/A                                                               
# -------------------------------------------------------------------------------------

os.system("clear")
print "  ____ _   _    _  _____   ____  _____ ______     _______ ____   "
print " / ___| | | |  / \|_   _| / ___|| ____|  _ \ \   / / ____|  _ \  "
print "| |   | |_| | / _ \ | |   \___ \|  _| | |_) \ \ / /|  _| | |_) | "
print "| |___|  _  |/ ___ \| |    ___) | |___|  _ < \ V / | |___|  _ <  "
print " \____|_| |_/_/   \_\_|   |____/|_____|_| \_\ \_/  |_____|_| \_\ "
print "                                                                 "
print "     BY TERENCE BROADBENT BSC CYBER SECURITY (FIRST CLASS)     \n"

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0                                                                
# Details : Initialise program variables.
# Modified: N/A
# -------------------------------------------------------------------------------------

host = sys.argv[1]
port = int(sys.argv[2])
temp = ""
socketList = []
recvBuffer = 4096

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0                                                                
# Details : Create the functions called from main.
# Modified: N/A
# -------------------------------------------------------------------------------------

def timelog(msg):
   now = datetime.now()
   print now.strftime("%x %H:%M"),
   print msg

def chat_server():
   server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
   server_socket.bind((host, port))
   server_socket.listen(10)
   socketList.append(server_socket)
   timelog("- Successfully started chat server on host " + host + ":" + str(port) + ".")

   while 1:
      now = datetime.now()
      ready_to_read,ready_to_write,in_error = select.select(socketList,[],[],0)
      for sock in ready_to_read:
         if sock == server_socket:
            sockfd, addr = server_socket.accept()
            socketList.append(sockfd)
            broadcast(server_socket, sockfd, "\r" + "[%s:%s] entered the chat room...\n" % addr)
            timelog("- Client %s:%s connected." % addr)
         else:
            try:
               data = sock.recv(recvBuffer)
               if data:
                  temp = str(sock.getpeername()).replace("'","").replace("(","").replace(")","").replace(", ",":")
                  broadcast(server_socket, sock, "\r" + "[" + temp + "] " + data)
               else:
                  if sock in socketList:
                     socketList.remove(sock)
                  temp = str(sock.getpeername()).replace("'","").replace("(","").replace(")","").replace(", ",":")
                  broadcast(server_socket, sock, "\r" + "[" + temp + "] has disconnected...\n")
                  timelog("- Client " + temp + " disconnected.")
            except:
               timelog("- Oops!! - Looks like a major error occuried...")
               server_socket.close()
               sys.exit()
    
def broadcast (server_socket, sock, message):
   for socket in socketList:
      if socket != server_socket and socket != sock :
         try :
            socket.send(message)
         except :
            socket.close()
            if socket in socketList:
               socketList.remove(socket)
 
# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0                                                                
# Details : MAIN - Start up the server.
# Modified: N/A
# -------------------------------------------------------------------------------------

sys.exit(chat_server())

#Eof
