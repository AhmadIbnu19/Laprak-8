def recursive_power(base, power):
    if power == 0:
        return 1
    return base * recursive_power(base, power - 1)

while True:
    nomor_utama = int(input('Masukkan bilangan: '))
    nomor_atas = int(input('Masukkan bilangan pangkatnya: '))
    result = recursive_power(nomor_utama, nomor_atas)
    print(f"Hasil dari {nomor_utama}**{nomor_atas} adalah {result}")
    keputusan = input('Apakah Anda ingin mengecek lagi? (yes/no): ').lower()
    if keputusan == 'no':
        print('Terima kasih')
        break