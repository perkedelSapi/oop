class InputForm:
    @staticmethod
    def input_mahasiswa():
        #melihat data 
        print("Masukkan data mahasiswa:")
        nim = input("NIM: ")
        nama = input("Nama: ")
        jurusan = input("Jurusan: ")
        return nim, nama, jurusan
