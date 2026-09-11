data_anime = []
jumlah_data = 0

print("Selamat datang di Anime Tracker!")
while True:
    daftar_judul = []
    for item in data_anime:
        daftar_judul.append(item[0])

    print("\nJumlah anime yang tercatat:", jumlah_data)
    print("Perintah: tambah / lihat / ubah / hapus / selesai")
    perintah = input("Masukkan perintah: ")

    if perintah == "tambah":
        judul = input("Masukkan judul anime: ")

        if judul in daftar_judul:
            print(judul, "sudah ada di data.")
        else:
            genre = input("Masukkan genre anime: ")
            rating = int(input("Masukkan rating (0-10): "))
            if rating < 0 or rating > 10:
                print("Rating harus antara 0 - 10.")
            else:
                data_anime.append((judul, genre, rating))
                jumlah_data += 1
                print(judul, "berhasil ditambahkan dengan rating", rating)

    elif perintah == "lihat":
        print("\nDAFTAR ANIME:")
        if jumlah_data == 0:
            print("Data masih kosong.")
        else:
            nomor = 1
            for item in data_anime:
                print(str(nomor) + ". " + item[0] + " | Genre:", item[1], "| Rating:", item[2])
                nomor += 1

    elif perintah == "ubah":
        judul = input("Masukkan judul anime yang ingin diubah ratingnya: ")

        if judul in daftar_judul:
            rating_baru = int(input("Masukkan rating baru (0-10): "))
            if rating_baru < 0 or rating_baru > 10:
                print("Rating harus antara 0 - 10.")
            else:
                for i in range(jumlah_data):
                    if data_anime[i][0] == judul:
                        data_anime[i] = (data_anime[i][0], data_anime[i][1], rating_baru)
                        print(judul, "berhasil diubah, rating baru:", rating_baru)
                        break
        else:
            print(judul, "tidak ditemukan di data.")

    elif perintah == "hapus":
        judul = input("Masukkan judul anime yang ingin dihapus: ")

        if judul in daftar_judul:
            for i in range(jumlah_data):
                if data_anime[i][0] == judul:
                    del data_anime[i]
                    jumlah_data -= 1
                    print(judul, "berhasil dihapus dari data.")
                    break
        else:
            print(judul, "tidak ditemukan di data.")

    elif perintah == "selesai":
        break

    else:
        print("Perintah tidak dikenali, coba lagi.")


print("\nRINGKASAN ANIME TRACKER")
if jumlah_data == 0:
    print("Belum ada data anime yang tercatat.")
else:
    for item in data_anime:
        print("-", item[0], "| Genre:", item[1], "| Rating:", item[2])
