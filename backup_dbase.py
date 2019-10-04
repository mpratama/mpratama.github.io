from django.core.management.base import BaseCommand
from apotek import helper
from shutil import copy
from time import sleep

class Command(BaseCommand):
    help = 'Backup database sqlite'

    def handle(self, *args, **kwargs):
        copy('DATABASE_PKM_YAMTEL.sqlite3', '../downloads/BCKP.sqlite3')
        print("Backup database berhasil")
        sleep(2)
