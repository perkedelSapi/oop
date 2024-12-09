# view/mahasiswa.py

class ViewMahasiswa:
    @staticmethod
    def tampilkan_daftar(data_mahasiswa):
        print("Daftar Mahasiswa:")
        for m in data_mahasiswa:
            print(m)

    @staticmethod
    def tampilkan_detail(mahasiswa):
        if mahasiswa:
            print("Detail Mahasiswa:")
            print(mahasiswa)
        else:
            print("Mahasiswa tidak ditemukan.")
