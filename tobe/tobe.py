#!/usr/bin/env python
# coding=utf8
# __version__

from __future__ import print_function
from colorama import Fore,Back,init
import sys
import os

__version__ = "0.1.2"
__createdate__ = "2019-12-21"

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
    print(Fore.RED + "{0:^60}".format("Servers can be connected"))
    print
    print(Fore.GREEN + "  {0:>2}   {1:<15}{2:^15}".format("ID", "Hostname", "Host"))
    count = 1
    for hostname, host in user_info.items():
        if count % 2 == 0:
            print(Fore.GREEN + "  {0:>2}   {1:<15}{2:<20}".format(count, hostname, host))
        else:
            print(Fore.MAGENTA + "  {0:>2}   {1:<15}{2:<20}".format(count, hostname, host))
        count += 1
    print
    print("version: %s\ndate: %s" % (__version__, __createdate__))


def single_color_print():
    print(Fore.RED + "{0:^60}".format("Command Line SSH Quick Link to Server"))
    print
    print(Fore.GREEN + "  {0:>2}   {1:<15}{2:^15}".format("ID", "Hostname", "Host"))
    count = 1
    for hostname, host in user_info.items():
        print(Fore.GREEN + "  {0:>2}   {1:<15}{2:<20}".format(count, hostname, host))
        count += 1
    print


if __name__ == "__main__":
    gather_ssh_info()
    colorful_print()
    #single_color_print()()
