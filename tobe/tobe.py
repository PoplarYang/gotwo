#!/usr/bin/env python3
# coding=utf8
# __version__

from __future__ import print_function
from colorama import Fore,Back,init
from sshconf import read_ssh_config
import sys
import os
from bullet import Bullet
import subprocess
import pyfiglet


__version__ = '0.3.1'
__createdate__ = '2020-02-08'

max_config_file_size_M = 10
HOME = os.environ['HOME']
CONFIG_PATH = os.path.join(HOME, '.ssh', 'config')
init(autoreset=True)


def preflight():
    '''
    preflight
    '''
    config_file_size_byte = os.path.getsize(CONFIG_PATH)
    if config_file_size_byte > max_config_file_size_M * 1024 * 1024:
        print('{}Config: {} size is more than {}M.'.format(Fore.RED, CONFIG_PATH, max_config_file_size_M))
        sys.exit(1)


def bullet_print():
    info_list = []
    config = read_ssh_config(CONFIG_PATH)
    for host in config.hosts():
        if host != '*':
            item = '{0:<15} {1:<15.15} {2:<10.10}'.format(
                    host,
                    config.host(host)['hostname'],
                    config.host(host).get('user', config.host('*').get('user', 'root'))
                    )
            info_list.append(item)

    info_list_sorted = sorted(info_list, key=lambda i:i[0])

    ascii_banner = pyfiglet.figlet_format('            SSH')
    cli = Bullet(
            # prompt='\nPlease choose a host: ',
            prompt=ascii_banner,
            choices=info_list_sorted,
            indent=0,        # 缩进
            align=5,
            margin=2,
            shift=0,
            bullet='',       # 前缀
            pad_right=5
        )
    
    result = cli.launch()
    print('You will connect to {}'.format(result.split()[0]))

    subprocess.call('ssh {} -o ConnectTimeout=3'.format(result.split()[0]), shell=True,
                    stdin=sys.stdin, stdout=sys.stdout)


def run():
    try: 
        preflight()
        bullet_print()
    except KeyboardInterrupt:
        print('exit')

if __name__ == '__main__':
    run()
