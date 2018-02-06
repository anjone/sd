from getpass import getpass
from fabric.api import settings, run, env, prompt

def remote_server():
    env.hosts = ['127.0.0.1']
    env.user = prompt('Enter user name: ')
    env.password = getpass('Enter password: ')

def install_package():
    run('pip install numpy')