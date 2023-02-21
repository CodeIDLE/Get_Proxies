import requests
import os
import colorama
import time
from colorama import Fore
colorama.init(autoreset=True)

def cls():
    linux = 'clear'
    windows = 'cls'
    os.system([linux,windows][os.name == 'nt'])
def makefile():
    linux1 = 'mkdir OUTPUT'
    windows1 = 'mkdir OUTPUT'
    os.system([linux1,windows1][os.name == 'nt'])

def welcome():
    print(Fore.BLUE + fr"""

 __     __     ______     __         __         ______     ______     __    __     ______    
/\ \  _ \ \   /\  ___\   /\ \       /\ \       /\  ___\   /\  __ \   /\ "-./  \   /\  ___\   
\ \ \/ ".\ \  \ \  __\   \ \ \____  \ \ \____  \ \ \____  \ \ \/\ \  \ \ \-./\ \  \ \  __\   
 \ \__/".~\_\  \ \_____\  \ \_____\  \ \_____\  \ \_____\  \ \_____\  \ \_\ \ \_\  \ \_____\ 
  \/_/   \/_/   \/_____/   \/_____/   \/_____/   \/_____/   \/_____/   \/_/  \/_/   \/_____/ 
                                                                                                                    """)
    print(Fore.GREEN + fr"                                   Code By Code Idle")
    print(Fore.CYAN + fr"=============================================================================================")
    print(Fore.RED + fr"[0] EXIT")
    print(Fore.YELLOW + fr"[1] Get Proxy For Windows")
    print(Fore.YELLOW + fr"[2] Get Proxy For Kali Linux, Parrot OS,..")


# welcome()

def bannerW():

    print(Fore.GREEN + fr"""
  .oooooo.                   .o8                 ooooo       .o8  oooo            
 d8P'  `Y8b                 "888                 `888'      "888  `888            
888           .ooooo.   .oooo888   .ooooo.        888   .oooo888   888   .ooooo.  
888          d88' `88b d88' `888  d88' `88b       888  d88' `888   888  d88' `88b 
888          888   888 888   888  888ooo888       888  888   888   888  888ooo888 
`88b    ooo  888   888 888   888  888    .o       888  888   888   888  888    .o 
 `Y8bood8P'  `Y8bod8P' `Y8bod88P" `Y8bod8P'      o888o `Y8bod88P" o888o `Y8bod8P' 
                                                                                                                        """)
    print(Fore.CYAN + fr"====================================================================================")
    print("\n")
    print(Fore.RED + fr"[0] Back To Menu")
    print(Fore.YELLOW + fr"[1] Proxy HTTP")
    print(Fore.YELLOW + fr"[2] Proxy Socks 4")
    print(Fore.YELLOW + fr"[3] Proxy Socks 5")
    print(Fore.YELLOW + fr"[4] Get All Proxys: Socks5, Socks4 and HTTP")

# bannerW()

def get_proxyW():
    cls()
    bannerW()
    you = int(input("\n >>>  "))
    path = os.getcwd()
    filep = os.path.join(path)

    if you==3:
        
        url = 'https://openproxylist.xyz/socks5.txt'
        url_1 = 'https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=1250&country=all&simplified=true'
        a = requests.get(url,url_1, allow_redirects=True)
        with open(filep + '\OUTPUT\socks5.txt','wb') as file1:
            file1.write(a.content)
            time.sleep(1)
        #readFile:
        line = open(filep + '\\OUTPUT\\socks5.txt')
        lines = line.readlines()
        line.close()
        for socks5 in lines:
            socks5 = socks5.strip()
            print(Fore.GREEN + socks5)
        print(Fore.GREEN + "\n[+] Succesfully !")
        print(Fore.YELLOW + "\n---> The file was saved as socks5.txt in the 'OUTPUT' folder")

    elif you==2:
        url2 = 'https://openproxylist.xyz/socks4.txt'
        url_2 = 'https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=1250&country=all&simplified=true'
        b = requests.get(url2,url_2, allow_redirects=True)
        with open(filep + '\OUTPUT\socks4.txt','wb') as file2:
            file2.write(b.content)
            time.sleep(1)
        #readFile:
        line2 = open(filep + '\\OUTPUT\\socks4.txt')
        lines2 = line2.readlines()
        line2.close()
        for socks4 in lines2:
            socks4 = socks4.strip()
            print(Fore.GREEN + socks4)
        print(Fore.GREEN + "\n[+] Succesfully !")
        print(Fore.YELLOW + "\n---> The file was saved as socks4.txt in the 'OUTPUT' folder")

    elif you==1:
        # url3 = 'https://openproxylist.xyz/http.txt'
        url_3 = 'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=1250&country=all&simplified=true'
        c = requests.get(url_3, allow_redirects=True)
        with open(filep + '\OUTPUT\http.txt','wb') as file3:
            file3.write(c.content)
            time.sleep(1)
        #readFile:
        line3 = open(filep + '\\OUTPUT\\http.txt')
        lines3 = line3.readlines()
        line3.close()
        for http in lines3:
            http = http.strip()
            print(Fore.GREEN + http)
        print(Fore.GREEN + "\n[+] Succesfully !")
        print(Fore.YELLOW + "\n---> The file was saved as http.txt in the 'OUTPUT' folder")

    elif you==4:
        url_socks5 = 'https://openproxylist.xyz/socks5.txt'
        url_socks5_1 = 'https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=1250&country=all&simplified=true'
        
        url_socks4 = 'https://openproxylist.xyz/socks4.txt'
        url_socks4_1 = 'https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=1250&country=all&simplified=true'

        url_http = 'https://openproxylist.xyz/http.txt'
        url_http_1 = 'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=1250&country=all&simplified=true'

        all1 = requests.get(url_socks5,url_socks4, allow_redirects=True)
        all2 = requests.get(url_socks5_1,url_socks4_1, allow_redirects=True)
        all3 = requests.get(url_http,url_http_1)
        with open(filep + '\\OUTPUT\\All-Proxy.txt','wb') as file4:
            file4.write(all1.content)
            file4.write(all2.content)
            file4.write(all3.content)
            time.sleep(1)
        #readFile:
        line4 = open(filep + '\\OUTPUT\\All-Proxy.txt')
        lines4 = line4.readlines()
        line4.close()
        for all_proxy in lines4:
            all_proxy = all_proxy.strip()
            print(Fore.GREEN + all_proxy)
        print(Fore.GREEN + "\n[+] Succesfully !")
        print(Fore.YELLOW + "\n---> The file was saved as All-Proxy.txt in the 'OUTPUT' folder")
    elif you == 0:
       select()
        
    else:
        print(Fore.RED + 'ERROR !!!')

def get_proxyLinux():
    cls()
    bannerW()
    you = int(input("\n >>>  "))
    path = os.getcwd()
    filep = os.path.join(path)

    if you==3:
        url = 'https://openproxylist.xyz/socks5.txt'
        url_1 = 'https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=1250&country=all&simplified=true'
        a = requests.get(url,url_1, allow_redirects=True)
        with open(filep + '/OUTPUT/socks5.txt','wb') as file1:
            file1.write(a.content)
            time.sleep(1)
        #readFile:
        line = open(filep + '/OUTPUT/socks5.txt')
        lines = line.readlines()
        line.close()
        for socks5 in lines:
            socks5 = socks5.strip()
            print(Fore.GREEN + socks5)
        print(Fore.GREEN + "\n[+] Succesfully !")
        print(Fore.YELLOW + "\n---> The file was saved as socks5.txt in the 'OUTPUT' folder")

    elif you==2:
        url2 = 'https://openproxylist.xyz/socks4.txt'
        url_2 = 'https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=1250&country=all&simplified=true'
        b = requests.get(url2,url_2, allow_redirects=True)
        with open(filep + '/OUTPUT/socks4.txt','wb') as file2:
            file2.write(b.content)
            time.sleep(1)
        #readFile:
        line2 = open(filep + '/OUTPUT/socks4.txt')
        lines2 = line2.readlines()
        line2.close()
        for socks4 in lines2:
            socks4 = socks4.strip()
            print(Fore.GREEN + socks4)
        print(Fore.GREEN + "\n[+] Succesfully !")
        print(Fore.YELLOW + "\n---> The file was saved as socks4.txt in the 'OUTPUT' folder")

    elif you==1:
        # url3 = 'https://openproxylist.xyz/http.txt'
        url_3 = 'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=1250&country=all&simplified=true'
        c = requests.get(url_3, allow_redirects=True)
        with open(filep + '/OUTPUT/http.txt','wb') as file3:
            file3.write(c.content)
            time.sleep(1)
        #readFile:
        line3 = open(filep + '/OUTPUT/http.txt')
        lines3 = line3.readlines()
        line3.close()
        for http in lines3:
            http = http.strip()
            print(Fore.GREEN + http)
        print(Fore.GREEN + "\n[+] Succesfully !")
        print(Fore.YELLOW + "\n---> The file was saved as http.txt in the 'OUTPUT' folder")

    elif you==4:
        url_socks5 = 'https://openproxylist.xyz/socks5.txt'
        url_socks5_1 = 'https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=1250&country=all&simplified=true'
        
        url_socks4 = 'https://openproxylist.xyz/socks4.txt'
        url_socks4_1 = 'https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=1250&country=all&simplified=true'

        url_http = 'https://openproxylist.xyz/http.txt'
        url_http_1 = 'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=1250&country=all&simplified=true'

        all1 = requests.get(url_socks5,url_socks4, allow_redirects=True)
        all2 = requests.get(url_socks5_1,url_socks4_1, allow_redirects=True)
        all3 = requests.get(url_http,url_http_1)
        with open(filep + '/OUTPUT/All-Proxy.txt','wb') as file4:
            file4.write(all1.content)
            file4.write(all2.content)
            file4.write(all3.content)
            time.sleep(1)
        #readFile:
        line4 = open(filep + '/OUTPUT/All-Proxy.txt')
        lines4 = line4.readlines()
        line4.close()
        for all_proxy in lines4:
            all_proxy = all_proxy.strip()
            print(Fore.GREEN + all_proxy)
        print(Fore.GREEN + "\n[+] Succesfully !")
        print(Fore.YELLOW + "\n---> The file was saved as All-Proxy.txt in the 'OUTPUT' folder")

    elif you == 0:
       select()

    else:
        print(Fore.RED + 'ERROR !!!')

def select():
    while True:
        linux = 'clear'
        windows = 'cls'
        os.system([linux,windows][os.name == 'nt'])
        makefile()
        welcome()
        you = int(input("\n>>> "))
        if you==1:
            get_proxyW()
            exit()
        elif you==2:
            get_proxyLinux()
            exit()
        elif you == 0:
            print(Fore.BLUE + "\n GoodBye, See you again ^^")
            break
        else:
            print(Fore.RED + "\n ERROR !!!")
select()