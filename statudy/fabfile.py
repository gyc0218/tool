from fabric.api import cd, run, env, hosts, task
env.hosts={'oracle@10.72.14.41:22'}
env.password='oracle'
@task(alias='haohao')
def ff():
    run('ls')
    
def hello():
    print("Hello world!")
    
from fabric.colors import *

def show():
    print green('success')
    print red('fail')
    print yellow('yellow')