from .models import DataObat
from pendaftaran.models import DataPasien, Resep
import datetime
import csv

def dumpdataobat():
    data_obat = open('./datamentah/dataobat.csv')
    for obat in data_obat:
        a = obat.replace('\n', '').split('|')
        b = DataObat(nama_obat=a[0], jumlah=a[1], tanggal_kadaluwarsa=a[2])
        b.save()
        print(a[0] + " sudah masuk")
        #print(a[0] + " " + a[1] + " " + a[2])

def dumpdatapasien():
    data_pasien = open('./datamentah/dp.csv')
    for p in data_pasien:
        a = p.replace('\n', '').split('|')
        #print(a[0] + " " + a[1].upper() + " " + a[2] + " " + a[3] + " " + a[4])
        b = DataPasien(no_bpjs=a[0], nama_pasien=a[1], tanggal_lahir=a[2], alamat=a[3], jenis_kelamin=a[4])
        b.save()
        print("%s sudah masuk" % a[1])

def datapenggunaanmentah(a, b):
    #tanggal_awal = str(input("Masukkan tanggal awal (dengan format TTTT-BB-HH): "))
    tanggal_awal = a
    tanggal_akhir = b
    #tanggal_akhir = str(input("Masukkan tanggal akhir (dengan format TTTT-BB-HH): "))
    output_file = open("data_penggunaan_mentah.csv", "w")
    wr = csv.writer(output_file)
    data_grabbed = Resep.objects.filter(nama_pasien__tanggal_kunjungan__range=(tanggal_awal, tanggal_akhir)).order_by('nama_pasien__tanggal_kunjungan')
    wr.writerow(("Tanggal Kunjungan", "Nama Pasien", "No BPJS", "Jenis Kelamin",  "Alamat", "Tanggal Lahir",  "Diagnosa", "Tensi(mmHg)", "Berat Badan(kg)", "Kadar Hb", "Kadar Gula Darah Sewaktu", "Kadar Kolesterol", "Kadar Asam Urat", "Nama Obat", "Jumlah", "Aturan Pakai"))
    for data in data_grabbed:
        wr.writerow((str(data.nama_pasien.tanggal_kunjungan), data.nama_pasien.nama_pasien.nama_pasien.upper(), data.nama_pasien.nama_pasien.no_bpjs, data.nama_pasien.nama_pasien.jenis_kelamin, data.nama_pasien.nama_pasien.alamat.upper(), data.nama_pasien.nama_pasien.tanggal_lahir, data.nama_pasien.diagnosa, data.nama_pasien.tensi, data.nama_pasien.berat_badan, data.nama_pasien.kadar_hb, data.nama_pasien.gula_darah, data.nama_pasien.kolesterol, data.nama_pasien.asam_urat, data.nama_obat.nama_obat.upper(), data.jumlah, data.aturan_pakai))
        print("Memproses -> %s - %s - %s: %s " % (str(data.nama_pasien.tanggal_kunjungan), data.nama_pasien.nama_pasien.nama_pasien.upper(), data.nama_obat.nama_obat.upper(), data.jumlah))
    #print("Data telah disimpan dalam file data_penggunaan_mentah.csv")
    output_file.close()

def datapenggunaantotal(a, b):
    x = 2
    #tanggal_awal = str(input("Masukkan tanggal awal (dengan format TTTT-BB-HH): "))
    tanggal_awal = a
    tanggal_akhir = b
    #tanggal_akhir = str(input("Masukkan tanggal akhir (dengan format TTTT-BB-HH): "))
    output_file = open("data_penggunaan_total.csv", "w")
    wr = csv.writer(output_file)
    data_grabbed = Resep.objects.filter(nama_pasien__tanggal_kunjungan__range=(tanggal_awal, tanggal_akhir)).order_by('nama_obat__nama_obat')
    wr.writerow(("Tanggal Obat Keluar", "Nama Obat", "Jumlah", "Jumlah Total"))
    for data in data_grabbed:
        wr.writerow((str(data.nama_pasien.tanggal_kunjungan), data.nama_obat.nama_obat.replace("(", "").replace(")", "").upper(), data.jumlah, "=sumif(B2:B" + str(len(data_grabbed) + 1) +",B" + str(x) + ",C2:C" + str(len(data_grabbed) + 1) + ")"))
        print("Memproses -> %s: %s" % (data.nama_obat.nama_obat.upper(), data.jumlah))
        x = x + 1
    #print("Data telah disimpan dalam file data_penggunaan_total.csv")
    output_file.close()

def sorteddatatotal():
    berkas = open("data_penggunaan_total.csv", "r")
    berkas2 = open("data_penggunaan_total_sorted.csv", "w")
    rdberkas = csv.reader(berkas)
    wrberkas2 = csv.writer(berkas2)
    index1 = 0
    listkontainer = []
    for baris in rdberkas:
        listkontainer.append(baris)
    for i in range(0, len(listkontainer)-1):
        if listkontainer[i][1] == listkontainer[i+1][1]:
            print("same value: passed")
        else:
            wrberkas2.writerow((listkontainer[i][1], listkontainer[i][3]))
            print("%s: %s" % ((listkontainer[i][1], listkontainer[i][3])))
    wrberkas2.writerow((listkontainer[-1][1], listkontainer[-1][3]))
    print("Data disimpan dalam data_penggunaan_total_sorted.csv")
    berkas.close()
    berkas2.close()
