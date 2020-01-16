#!/usr/bin/env python3
# coding=utf8
# __version__

from __future__ import print_function
from colorama import Fore,Back,init
import sys
import os
from bullet import Bullet
import subprocess
import pyfiglet

__version__ = "0.2.1"
__createdate__ = "2020-01-16"

HOME = os.environ["HOME"]
CONFIG_PATH = os.path.join(HOME, ".ssh", "config")
user_info = {}
init(autoreset=True)


def gather_ssh_info():
    """
    gather ssh information
    """
    try:
        with open(CONFIG_PATH) as fd:
            for line in fd:
                line = line.strip()
                if line.startswith("Host ") and "*" not in line:
                    hostname = line.split()[1]
                if line.startswith("HostName") and "*" not in line:
                    host = line.split()[1]
                    if hostname and host:
                        user_info[hostname] = host
                    hostname = host = ""
    except Exception as e:
        print(Fore.RED + "Error, %s" %e)
        sys.exit(1)


def colorful_print():
    ascii_banner = pyfiglet.figlet_format("        SSH")
    print(ascii_banner)
    print("version: %s\ndate: %s" % (__version__, __createdate__))
    print(Fore.GREEN + "  {0:>2}   {1:<15}{2:^15}".format("ID", "Hostname", "Host"))
    count = 1
    for hostname, host in user_info.items():
        if count % 2 == 0:
            print(Fore.GREEN + "  {0:>2}   {1:<15}{2:<20}".format(count, hostname, host))
        else:
            print(Fore.MAGENTA + "  {0:>2}   {1:<15}{2:<20}".format(count, hostname, host))
        count += 1
    print()


def single_color_print():
    ascii_banner = pyfiglet.figlet_format("        SSH")
    print(ascii_banner)
    print("version: %s\ndate: %s" % (__version__, __createdate__))
    print("  {0:>2}   {1:<15}{2:^15}".format("ID", "Hostname", "Host"))
    count = 1
    for hostname, host in user_info.items():
        print("  {0:>2}   {1:<15}{2:<20}".format(count, hostname, host))
        count += 1
    print()


def bullet_print():
    info_list = []
    for hostname, host in user_info.items():
        item = "{0:<15} {1:<15}".format(hostname, host)
        info_list.append(item) 
    
    info_list_sorted = sorted(info_list, key=lambda i:i[0])

    ascii_banner = pyfiglet.figlet_format("            SSH")
    cli = Bullet(
            # prompt="\nPlease choose a host: ",
            prompt=ascii_banner,
            choices=info_list_sorted,
            indent=0,        # 缩进
            align=5,
            margin=2,
            shift=0,
            bullet="",      # 前缀
            pad_right=5
        )
    
    result = cli.launch()
    print("You will connect to {}".format(result.split()[0]))

    subprocess.call("ssh {} -o ConnectTimeout=3".format(result.split()[0]), shell=True,
                    stdin=sys.stdin, stdout=sys.stdout)


def run():
    gather_ssh_info()
    try: 
        #single_color_print()
        #colorful_print()
        bullet_print()
    except KeyboardInterrupt:
        print("exit")

if __name__ == "__main__":
    run()
