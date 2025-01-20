def garis(panjang=58):
    return "+" + "-" * (panjang) + "+"

def header():
    print(garis())
    print("|{:^58}|".format("TOKO PIAAA"))
    print("|{:^58}|".format("Jl. Pendarungan"))
    print("|{:^58}|".format("Tel. 0812345678"))
    print(garis())

def masukkan_item():
    items = []
    while True:
        nama_barang = input("Masukkan nama barang (ketik 'selesai' untuk mengakhiri): ")
        if nama_barang.lower() == 'selesai':
            break
            
        while True:
            try:
                harga = float(input("Masukkan harga barang: Rp "))
                jumlah = int(input("Masukkan jumlah barang: "))
                break
            except ValueError:
                print("Masukkan angka")
                
        items.append({
            'nama': nama_barang, 
            'harga': harga, 
            'jumlah': jumlah, 
            'total': harga * jumlah 
        })
    return items

def hitung_total_dan_diskon(items):
    total_items = sum(item['jumlah'] for item in items)
    total_harga = sum(item['total'] for item in items)

    if total_items >= 3:
        diskon = total_harga * 0.10  # Diskon 10%
    else:
        diskon = 0

    return total_harga, diskon

def tabel_item(items):
    # Header tabel items
    print(garis())
    print("| {:<20} | {:>5} | {:>12} | {:>10} |".format(
        "Nama Barang", "Qty", "Harga", "Total"))
    print(garis())
    
    # Isi tabel items
    for item in items:
        print("| {:<20} | {:>5} | {:>12,.0f} | {:>10,.0f} |".format(
            item['nama'][:20],
            item['jumlah'],
            item['harga'],
            item['total']
        ))
    print(garis())

def tabel_hasil(total_harga, diskon, uang_bayar):
    # Tabel ringkasan
    print("| {:<35} | {:>18,.0f} |".format("Total Belanja", total_harga))
    print("| {:<35} | {:>18,.0f} |".format("Diskon (10%)", diskon))
    print("| {:<35} | {:>18,.0f} |".format("Total Setelah Diskon", total_harga - diskon))
    print("| {:<35} | {:>18,.0f} |".format("Tunai", uang_bayar))
    print("| {:<35} | {:>18,.0f} |".format("Kembalian", uang_bayar - (total_harga - diskon)))
    print(garis())

def footer():
    print("|{:^58}|".format("Terima Kasih Atas Kunjungan Anda"))
    print(garis())

def main():
    print("-" * 40)
    
    # Input barang-barang
    items = masukkan_item()
    
    if not items:
        print("Tidak ada barang yang diinput")
        return
        
    # Hitung total dan diskon
    total_harga, diskon = hitung_total_dan_diskon(items)
    
    # Input pembayaran
    while True:
        try:
            uang_bayar = float(input(f"\nTotal yang harus dibayar: Rp {total_harga - diskon:,.0f}\nMasukkan jumlah uang: Rp "))
            if uang_bayar >= (total_harga - diskon):
                break
            print("Uang tidak cukup")
        except ValueError:
            print("Masukkan angka")
    
    # Cetak struk
    print("\n" * 2)
    header()
    tabel_item(items)
    tabel_hasil(total_harga, diskon, uang_bayar)
    footer()
    

if __name__ == "__main__":
    main()