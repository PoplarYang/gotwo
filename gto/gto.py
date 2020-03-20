#!/usr/bin/env python3
# coding=utf8


from __future__ import print_function
from colorama import Fore,Back,init
from sshconf import read_ssh_config
import sys
import os
from bullet import Bullet
import subprocess
import pyfiglet


max_config_file_size_M = 10
HOME = os.environ['HOME']
CONFIG_PATH = os.path.join(HOME, '.ssh', 'config')


class ISSH:
    __str = '{0:<15} {1:<15.15} {2:<10.10}'
    __tip = '''
🌻 Up/Down - Move selection up/down
🌴 Enter   - Ssh to current selection
🌵 Ctrl+c  - Quit
🚀 Connecting to ...
'''
    def __init__(self, config_path):
        self.config_path = config_path
        init(autoreset=True)

    def run(self):
        try: 
            self.__check_if_ssh_config_exists()
            self.__screen_print()
        except KeyboardInterrupt:
            self.__shutdown()

    def __check_if_ssh_config_exists(self):
        config_file_size_byte = os.path.getsize(self.config_path)
        if config_file_size_byte > max_config_file_size_M * 1024 * 1024:
            print('{}Config: {} size is more than {}M.'.format(
                Fore.RED, 
                CONFIG_PATH, 
                max_config_file_size_M))
            self.__shutdown()
    
    def __shutdown(self):
        print(Fore.RED + '🐳Exit.')
        sys.exit(1)

    def __host_info(self):
        info_list = []
        config = read_ssh_config(self.config_path)
        default_user = config.host("*").get('user', 'None')

        for host in config.hosts():
            if host != '*':
                item = self.__str.format(
                        host,
                        config.host(host)['hostname'],
                        config.host(host).get('user', default_user)
                        )
                info_list.append(item)
    
        self.host_info_sorted = sorted(info_list, key=lambda i:i[0])

    def __screen_print(self):
        '''
        screen print used by bullet
        '''
        self.__host_info()

        banner = Fore.YELLOW + pyfiglet.figlet_format('         GOTO') + \
                Fore.GREEN + self.__tip + \
                Fore.BLUE + self.__str.format('HostName', 'Address', 'User')
        cli = Bullet(
                # prompt='\nPlease choose a host: ',
                prompt=banner,
                choices=self.host_info_sorted,
                indent=0,        # 缩进
                align=0,
                margin=0,
                shift=0,
                bullet='',       # 前缀
                pad_right=5
            )

        result = cli.launch()
        print(Fore.GREEN + 'You will connect to {}.'.format(result.split()[0]))
        print()
        subprocess.call('ssh {} -o ConnectTimeout=3'.format(result.split()[0]),
                        shell=True,
                        stdin=sys.stdin, 
                        stdout=sys.stdout)


if __name__ == '__main__':
    ssh = ISSH(CONFIG_PATH)
    ssh.run()
