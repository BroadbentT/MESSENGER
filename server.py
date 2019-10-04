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

HOST = ''
SOCKET_LIST = []
RECV_BUFFER = 4096
PORT = 9009

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0                                                                
# Details : Create the functions called from main.
# Modified: N/A
# -------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------
# Main chat server routine with infinite loop.
# -------------------------------------------------------------------------------------

def chat_server():
   server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
   server_socket.bind((HOST, PORT))
   server_socket.listen(10)
   SOCKET_LIST.append(server_socket)
   print "Chat server running on port: " + str(PORT) + ".\n"

   while 1:
      ready_to_read,ready_to_write,in_error = select.select(SOCKET_LIST,[],[],0)
      for sock in ready_to_read:
         if sock == server_socket:
            sockfd, addr = server_socket.accept()
            SOCKET_LIST.append(sockfd)
            print "Client (%s, %s) connected" % addr                 
            broadcast(server_socket, sockfd, "[%s:%s] entered the chat room...\n" % addr)
         else:
            try:
               data = sock.recv(RECV_BUFFER)
               if data:
                  broadcast(server_socket, sock, "\r" + '[' + str(sock.getpeername()) + '] ' + data)  
               else:
                  if sock in SOCKET_LIST:
                     SOCKET_LIST.remove(sock)
                  broadcast(server_socket, sock, "Client (%s, %s) is offline...\n" % addr) 
            except:
               broadcast(server_socket, sock, "Client (%s, %s) is offline...\n" % addr)
               continue
   server_socket.close()
    
# -------------------------------------------------------------------------------------
# Broadcast chat messages to all connected clients and tidy up any redundant clients.
# -------------------------------------------------------------------------------------

def broadcast (server_socket, sock, message):
   for socket in SOCKET_LIST:
      if socket != server_socket and socket != sock :
         try :
            socket.send(message)
         except :
            socket.close()
            if socket in SOCKET_LIST:
               SOCKET_LIST.remove(socket)
 
# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0                                                                
# Details : MAIN - Start up the server.
# Modified: N/A
# -------------------------------------------------------------------------------------

sys.exit(chat_server())    

#Eof
