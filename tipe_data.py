# ---------- BELAJAR TIPE DATA PADA PTYHON ---------


# --- 1 tipe data string
# tipe data string isinya adalah karakter, bisa teks atapun simbol, yang penting bukan angka
# penulisan data string harus diapit oleh tanda petik ("")
nama = "nama saya Ardiyanto"
print(nama)
print(type(nama)) # ini merupakan cara mengecek tipe data kita, menunjukkan hasil "str" yang artinya string
kegiatan = "saya sedang belajar python"
print(kegiatan)
simbol = "/,;,,,;l,"
print(simbol)
angka = "123010" #dapat juga dilakukan untuk mengubah angka menjadi tipe data string
print(angka)
print(type(angka)) #terbukti kita bisa melihat angka menjadi bertipe data string

# selain itu apabila data string kita memuat banyak sekali kata, kita dapat mengakses sebagiannya saja untuk dimunculkan
print(nama[0]) # angka 0 menunjukkan kita ingin mencetak karakter ke 0 
print(nama[1]) # perlu diingat dalam python huruf "n" bukan dianggap sebagai karakter pertama, melainkan karakter ke-0. sehingga saat kita ingin mencetak karakter pertama harus menggunakan indeks 0 
print(nama[0:4]) # ini merupakan cara jika kita ingin mencetak beberapa karakter sekaligus

# tidak hanya itu, kita juga bisa memecah tipe data string menjadi beberapa baris. caranya adalah dengan menggunakan kutip atau petik 3 kali (""" """)
kampus = """Universitas 
Sebelas
Maret """
print(kampus)