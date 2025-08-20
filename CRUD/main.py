book_list = []

def add_book(title,author):
    new_id = len(book_list) + 1

    book = {
            "id" : new_id,
            "title" : title,
            "author" : author
            }
    
    book_list.append(book)
    print(f"book '{title}', author '{author}' successfully added!")

def show_book():
    if len(book_list) == 0:
        print("Belum ada buku yang tersimpan.")
    else:
        print("\nDaftar buku: ")
        for book in book_list:
            print(f"ID: {book['id']} | Judul: {book['title']} | penulis: {book['author']}")

def update_book(book_id):
    for book in book_list:
        if book['id'] == book_id:
            print(f"Buku ditemukan: {book['title']} - {book['author']}")

            new_title = input("Masukkan judul baru (kosongkan jika tidak diubah): ")
            new_author = input("Masukkan author baru (kosongkan jika tidak diubah): ")
        
            if new_title != "":
                book['title'] = new_title
            if new_author != "":
                book['author'] = new_author
        
            print("Buku berhasil diperbarui")
            return
    
    print("Buku dengan ID tersebut tidak ditemukan")

def delete_book(book_id):
   for book in book_list:
       if book['id'] == book_id:
           book_list.remove(book)
           print(f"buku dengan ID {book_id} berhasil di hapus")
           return
       print("Buku dengan ID tersebut tidak ditemukan")



judul = input("Masukan judul buku: ")
penulis = input("Masukan Nama Penulis: ")
add_book(judul,penulis)

judul = input("Masukan judul buku: ")
penulis = input("Masukan Nama Penulis: ")
add_book(judul,penulis)

# update_book(1)

delete_book(1)

show_book()