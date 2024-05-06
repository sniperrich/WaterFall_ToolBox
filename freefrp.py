import os
import re
import requests
import subprocess
import time
import random
import uuid
import tkinter as tk
from tkinter import messagebox
def extract_value(filename, key):
    with open(filename, 'r') as file:
        for line in file:
            match = re.search(rf'{key}\s*=\s*(.*)', line)
            if match:
                return match.group(1).strip('"')

def extract_ip_address(filename):
    with open(filename, 'r') as file:
        for line in file:
            match = re.search(r'serverAddr\s*=\s*"([\d\.]+)"', line)
            if match:
                return match.group(1)

def run_cmd_Popen_fileno(cmd_string):
    return subprocess.Popen(cmd_string, shell=True, stdout=None, stderr=None).wait()

def is_string_in_file(filename, search_string):
    try:
        with open(filename, 'r') as file:
            for line in file:
                if search_string in line:
                    return True
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

def alter(file, old_content, new_content):
    content = read_file(file)
    content = content.replace(old_content, new_content)
    rewrite_file(file, content)

def read_file(file):
    with open(file, encoding='UTF-8') as f:
        read_all = f.read()
    return read_all

def rewrite_file(file, data):
    with open(file, 'w', encoding='UTF-8') as f:
        f.write(data)

def download_file(url, file_name):
    try:
        T1 = time.time()
        res = requests.get(url, stream=True)
        with open(file_name, "wb") as f:
            for chunk in res.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        T2 = time.time()
        tb1.insert("6.0", f"下载完成，用时{int((T2 - T1)*1000)}毫秒\n")

    except Exception as e:
        tb1.insert("6.0", f"下载失败: {e}\n")

def runfrp():
    try:
        tb1.insert("1.0","你正在运行清Tool工具箱,官方Q群705801382\n")
        tb1.insert("2.0", "爱发电:https://afdian.net/a/qqqqqf\n")
        tb1.insert("3.0", "(我知道你会让我喝一杯咖啡的对吧嘿嘿)")
        tb1.insert("4.0", "---------------------------------------------------------------------\n")

        folder_path = os.getcwd()
        frpc_exe_path = os.path.join(folder_path, "frpc.exe")
        if not os.path.exists(frpc_exe_path):
            tb1.insert("5.0", "frpc.exe 文件不存在。自动下载 frpc.exe\n")

            download_file('http://154.7.180.249/frpc.exe', 'frpc.exe')

        frpc_toml_path = os.path.join(folder_path, "frpc.toml")
        if not os.path.exists(frpc_toml_path):
            tb1.insert("5.0", "frpc.toml 文件不存在。自动下载 frpc.toml")

            download_file('http://154.7.180.249/frpc.toml', 'frpc.toml')
        if is_string_in_file("frpc.toml", "client"):
            temp = 1
            if temp == "1":
                download_file('http://154.7.180.249/frpc.toml', 'frpc.toml')
            else:

                tb1.insert("7.0", "远程IP:", extract_ip_address("frpc.toml")+"\n")
                tb1.insert("8.0", "本地IP:", extract_value("frpc.toml", "localIP")+"\n")
                tb1.insert("9.0", "远程端口:", extract_value("frpc.toml", "remotePort")+"\n")
                tb1.insert("10.0", "连接{}{}{}就可以进入服务器啦".format(extract_ip_address("frpc.toml"),":",extract_value("frpc.toml", "remotePort"))+"\n")
                tb1.insert("11.0", "---------------------------------------------------------------------\n")
                tb1.insert("12.0", "温馨提醒:如果出现报错(error)或无法连接请尝试重启程序并重置配置文件使用随机端口\n")
                tb1.insert("13.0", "(来Q群找我也可以哦~)\n")
                tb1.insert("14.0", "---------------------------------------------------------------------\n")
                run_cmd_Popen_fileno(r".\frpc.exe -c frpc.toml")
                tb1.insert("15.0", "---------------------------------------------------------------------")
                tb1.insert("16.0", "Frp奇怪的停止了运行~\n")
                tb1.insert("17.0", "frpc.exe 文件不存在。自动下载 frpc.exe\n")
                tb1.insert("18.0", "或许你需要加入Q群705801382来寻求帮助\n")
        game_port = input("请输入游戏端口号(默认25565)：") or "25565"
        game_ip = input("请输入游戏IP(默认127.0.0.1)：") or '"127.0.0.1"'
        remote_port = input("请输入远程端口(默认随机):") or str(random.randint(10000, 40000))
        connect_type = input("请输入传输方式(默认tcp)：") or '"tcp"'
        alter("frpc.toml", "nap", '"{}"'.format("client" + str(uuid.uuid4())))
        alter("frpc.toml", "loi", game_ip)
        alter("frpc.toml", "lop", game_port)
        alter("frpc.toml", "rmp", str(remote_port))
        alter("frpc.toml", "cnt", connect_type)
        print("远程IP:", extract_ip_address("frpc.toml"))
        print("远程端口:", extract_value("frpc.toml", "remotePort"))
        print("本地IP:", extract_value("frpc.toml", "localIP"))
        print("连接方式:", extract_value("frpc.toml", "type"))
        print("连接{}{}{}就可以进入服务器啦".format(extract_ip_address("frpc.toml"),":",extract_value("frpc.toml", "remotePort")))
        print("启动Frp")
        print("---------------------------------------------------------------------")
        print("温馨提醒:如果出现报错(error)请尝试重启程序并重置配置文件使用随机端口")
        print("(来Q群找我也可以哦~)")
        print("---------------------------------------------------------------------")
        run_cmd_Popen_fileno(r".\frpc.exe -c frpc.toml")
        print("Frp奇怪的停止了运行~")
        print("或许你需要加入Q群705801382来寻求帮助")
        input("按下Enter退出程序")
        os._exit(0)
    except Exception as e:
        tk.messagebox.showerror("Error:{}".format(e))
        tk.messagebox.showinfo("请加Q1684773595上报Bug~谢谢你")

root=tk.Tk()
root.geometry("800x500")
tb1=tk.Text(root,height=30,width=50)
tb1.pack()
b1=tk.Button(root,text="start",command=runfrp)
b1.pack()


root.mainloop()