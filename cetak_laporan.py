from django.core.management.base import BaseCommand
#from django.utils import timezone
from apotek import helper
from os import rename

class Command(BaseCommand):
    help = 'Cetak laporan'
    #timestamp = timezone.now().strftime('%d_%B_%Y')

    def handle(self, *args, **kwargs):
        a = str(input("Masukkan tanggal awal (TTTT-BB-HH): "))
        b = str(input("Masukkan tanggal akhir (TTTT-BB-HH): "))
        helper.datapenggunaanmentah(a, b)
        helper.datapenggunaantotal(a, b)
        rename('data_penggunaan_mentah.csv', '../downloads/data_penggunaan_mentah_%s_sampai_%s.csv' % (a, b))
        rename('data_penggunaan_total.csv', '../downloads/data_penggunaan_total_%s_sampai_%s.csv' % (a, b))
