from django.core.management.base import BaseCommand
from apotek import helper
from shutil import copy

class Command(BaseCommand):
    help = 'Backup database sqlite'

    def handle(self, *args, **kwargs):
        copy('DATABASE_PKM_YAMTEL.sqlite3', '../BCKP.sqlite3')
