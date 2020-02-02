<!-- __      __    __               ___
    /  \    /  \__|  | _ __        /   \
    \   \/\/   /  |  |/ /  |  __  |  |  |
     \        /|  |    <|  | |__| |  |  |
      \__/\__/ |__|__|__\__|       \___/

A web service for sharing opinions and avoiding arguments

@file       README.md
@brief      The help file for this project
@copyright  GNU Public License, 2018
@authors    Frank Imeson
-->

Wiki-O Documentation
=======================================

Requirements
============

- Ubuntu 16 (VPS)
- Python 3.5, 3.6
- Django 2.1, 2.2
- Bootstrap 4.1

Ubuntu Packages
::

    $ sudo apt update
    $ sudo apt install git
    $ sudo apt install postgresql
    $ sudo apt install alpine
    $ sudo apt install python3
    $ sudo apt install python3-pip
    $ sudo apt install apache2 
    $ sudo apt install libapache2-mod-wsgi-py3
    $ sudo apt install dnsutils
    $ sudo apt install vim
    $ export LC_ALL=C
    $ pip3 install virtualenv


Virtual Envionment
==================

Step 1: Setup Environment (add config to bashrc)
::

    $ cd /home/wiki-o/code
    $ virtualenv venv
    $ source venv/bin/activate

Step 2: Install Packages
::

  To install requirments:

    $ pip3 install -r /home/wiki-o/config/pip.requirements

  To show the requirments:

    $ pip3 freeze


Postgrsql
============

Step 1: Setup Database
::

    $ cd ~
    $ sudo -u postgres psql -c "create database wiki_o;"
    $ sudo -u postgres psql -c "create user django with encrypted password 'mypass';"
    $ sudo -u postgres psql -c "grant all privileges on database wiki_o to django;"
    $ sudo -u postgres psql -c "alter user django CREATEDB;"



Django
============

Step 1: Migrate
::

    $ cd /home/wiki-o/code/wiki_o
    $ link -s local.django.settings.py settings.py
    $ cd ..
    $ python3 manage.py migrate
    $ python3 manage.py collectstatic

Step 2: Restore Database
::

    $ python3 manage.py loaddata /home/wiki-o/backup.json

Step 3: Test
::

    $ python3 manage.py runserver IP_ADDRESS:8000