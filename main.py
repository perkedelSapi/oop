from data.mahasiswa import Mahasiswa, DataMahasiswa
from view.input_form import InputForm
from view.mahasiswa import ViewMahasiswa

# Inisialisasi data mahasiswa
data_mahasiswa = DataMahasiswa()

def menu_utama():
    """Menampilkan menu utama program"""
    while True:
        print("\nMenu Utama:")
        print("1. Tambah Mahasiswa")
        print("2. Tampilkan Semua Mahasiswa")
        print("3. Cari Mahasiswa")
        print("4. Hapus Mahasiswa")
        print("5. Keluar")
        
        pilihan = input("(T)ambah, (L)ihat, (C)ari, (H)apus, (K)eluar: ")

        if pilihan == "t":
            tambah_mahasiswa()
        elif pilihan == "l":
            tampilkan_semua_mahasiswa()
        elif pilihan == "c":
            cari_mahasiswa()
        elif pilihan == "h":
            hapus_mahasiswa()
        elif pilihan == "k":
            print("Program selesai.")
            break
        else:
            print("Silakan coba lagi.")

def tambah_mahasiswa():
    """Fungsi untuk menambah mahasiswa baru"""
    nim, nama, jurusan = InputForm.input_mahasiswa()
    mahasiswa = Mahasiswa(nim, nama, jurusan)
    data_mahasiswa.tambah_mahasiswa(mahasiswa)
    print("Mahasiswa berhasil ditambahkan!")

def tampilkan_semua_mahasiswa():
    """Fungsi untuk menampilkan semua data mahasiswa"""
    daftar_mahasiswa = data_mahasiswa.tampilkan_semua()
    if daftar_mahasiswa:
        ViewMahasiswa.tampilkan_daftar(daftar_mahasiswa)
    else:
        print("Tidak ada data mahasiswa.")

def cari_mahasiswa():
    """Fungsi untuk mencari data mahasiswa berdasarkan NIM"""
    nim = input("Masukkan NIM mahasiswa yang ingin dicari: ")
    mahasiswa = data_mahasiswa.cari_mahasiswa(nim)
    ViewMahasiswa.tampilkan_detail(mahasiswa)

def hapus_mahasiswa():
    """Fungsi untuk menghapus data mahasiswa berdasarkan NIM"""
    nim = input("Masukkan NIM mahasiswa yang ingin dihapus: ")
    mahasiswa = data_mahasiswa.cari_mahasiswa(nim)
    if mahasiswa:
        data_mahasiswa.hapus_mahasiswa(nim)
        print("Mahasiswa berhasil dihapus.")
    else:
        print("Mahasiswa dengan NIM tersebut tidak ditemukan.")

# Jalankan program
if __name__ == "__main__":
    menu_utama()
