#!/usr/bin/env python3
# coding=utf-8
"""/usr/bin/python"""
import os
import sys
import subprocess

BASE_ROOT = "/home/adriana/www/dashboard_customerheartbeat_com"

PYTHON_EXEC = "/usr/bin/python"


def setup_django():
    """
    setup_django
    """
    sys.path.append("/home/adriana/www/dashboard_customerheartbeat_com/server")
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.settings")

    import django
    django.setup()
    from django.conf import settings
    from server.utils import logger

    # import * only allowed at module level
    from server.models import Model1, Model2


def main():
    """
    main
    """
    setup_django()
    jobs = Job.objects.filter(state='WAITING_FOR_PROCESS')


if __name__ == "__main__":
    main()
