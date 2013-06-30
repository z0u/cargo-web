from __future__ import with_statement
from fabric.api import cd, run, local, env

env.hosts = ['lille.sturm.com.au']

PROJECT_DIR = "/home/web/cargo"
SITE_NAME = "cargo"

def deploy(initial=False):
    """Install or deploy updates this website.

    Use install=True for installing a new site.
    """
    transfer_files()
    #prepare_virtualenv(initial)
    #prepare_django()
    #reload_gunicorn()
    flush_memcached()
    update_nginx()


def initialise():
    deploy(initial=True)


def transfer_files():
    local("bzr push bzr+ssh://{user}@{host}{project_dir}".format(
            user=env.user, host=env.host, project_dir=PROJECT_DIR),
          capture=False)

    with cd(PROJECT_DIR):
        run("bzr checkout || bzr up")


def prepare_virtualenv(initial=False):
    """Initialise a virtualenv and install required Python modules."""

    if initial:
        run("virtualenv /home/web/.virtualenvs/{site_name}".format(site_name=SITE_NAME))
    with cd(PROJECT_DIR):
        run("/home/web/.virtualenvs/{site_name}/bin/pip install -r project/requirements.txt --download-cache=/home/web/.virtualenvs/cache".format(site_name=SITE_NAME))


def prepare_django():
    with cd(PROJECT_DIR):
        run("cp project/settings.py.live project/settings.py")
        run('/home/web/.virtualenvs/{site_name}/bin/python manage.py collectstatic -v0 --noinput'.format(site_name=SITE_NAME))


def reload_gunicorn():
    # Not most efficient
    run('sudo supervisorctl restart {site_name}_django'.format(site_name=SITE_NAME))

    #run('kill -HUP `cat %s`' % PID_FILE)


def flush_memcached():
    """Clear cache by restarting the memcached server.

    By design, any user on the system can issue commands to memcached, including
    to flush the whole cache. Alternately, we could install libmemcached-tools
    and run `memcflush --servers localhost`.

    """
    run("echo flush_all | nc -w1 localhost 11211")


def update_nginx():
    run("sudo ln -s --force {project_dir}/deploy/nginx.conf /etc/nginx/sites-available/{site_name}".format(
            project_dir=PROJECT_DIR, site_name=SITE_NAME))
    run("sudo ln -s --force /etc/nginx/sites-available/{site_name} /etc/nginx/sites-enabled/{site_name}".format(
            site_name=SITE_NAME))
    run("sudo /etc/init.d/nginx reload")
