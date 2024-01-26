def tampilkan_menu():
    print("========== Menu ==========")
    print("1. Input Angka")
    print("2. Sorting")
    print("3. Searching")
    print("4. Selesai")
    print("==========================")

# Contoh pemanggilan
tampilkan_menu()
def layar_input():
    input_user = input("Masukkan pilihan:[1/2/3/4] ")
    return input_user



# Contoh pemanggilan
while True:

    pilihan = input("Masukkan pilihan : [1/2/3/4]: ")

    if pilihan == '1':
        angka = input("Masukkan angka:")
        print(angka)
    
    elif pilihan == '2':
        a = int(input("Angka 1: "))
        b = int(input("Angka 2: "))
        c = int(input("Angka 3: "))

        if a > b:
            a,b = b,a
        if a > c:
            a,c = c,a
        if b > c:
            b,c = c,b
    
        print (a, "<", b, "<", c)
        
    elif pilihan == '3':
        from random import choice
        number = [1,2,3,4,5,6,7,8,9,10]
        for i in range (5):
            bil = choice (number)
        print(bil)
        
    elif pilihan == '4':
        print ("Perintah selesai terima kasih")
        
    else :
        print ("Angka tidak ditemukan")

    