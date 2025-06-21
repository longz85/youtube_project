import sys
import os
import ctypes

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    # Re-run the script with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    sys.exit()

import subprocess
def clear():
    subprocess.run("cls", shell=True)

def liet_ke():
    clear()
    subprocess.run("net user", shell=True)
    menu()

def xoa():
    clear()
    u = input("ten(username): ")
    subprocess.run(f"net user {u} /delete", shell=True)
    clear()
    print("complete")
    menu()
 
def tao():
    clear()
    u = input("ten(username): ")
    p = input("mat khau(password): ")
    subprocess.run(f"net user {u} {p} /add", shell=True)
    clear()
    print("complete")
    menu()
    
def thay_doi():
    clear()
    u = input("ten(username): ")
    p = input("mat khau moi(new password): ")
    subprocess.run(f"net user {u} {p}", shell=True)
    clear()
    print("complete")
    menu()


def menu():
    print("-------MENU-------")
    print("1) liet ke nguoi dung")
    print("2) tao tai khoan")
    print("3) thay doi mat khau")
    print("4) xoa mat khau")
    print("ctrl + C de thoat")
    choice = int(input(">>"))
    
    if choice == 1:
        liet_ke()
    elif choice == 2:
        tao()
    elif choice == 3:
        thay_doi()
    elif choice == 4:
        xoa()
    else:
        menu()

clear()      
menu()