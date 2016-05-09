#!/usr/bin/env python
import os
import subprocess

if __name__ == "__main__":
    new_env = os.environ
    new_env['PYTHONPATH'] = '/Users/himanshu/Documents/django-testing-ddp/src/'
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_ddp.settings")
    subprocess.call(['dddp'], env=new_env)
