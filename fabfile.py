from fabric.api import cd, run, env, local

env.hosts = ['dima@fignuts']
env.forward_agent = True


def deploy():
    local('git push origin master')
    with cd('/tmp/tuna'):
        run('git pull', pty=False)
