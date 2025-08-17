class Book:
    def __init__(self, title, author, price, stock):
        self.__title = title
        self.__author = author
        self.__price = price
        self.__stock = stock

    
    def get_title(self):
        return self.__title
    
    def set_title(self, new_title):
        if new_title == "":
            print(f"title tidak boleh kosong")
        else:
            self.__title = new_title
            print(f"title buku diperbarui menjadi {new_title}")

    def get_author(self):
        return self.__author
    
    def set_author(self, new_author):
        if new_author == "":
            print(f"author tidak boleh kosong")
        else:
            self.__author = new_author
            print(f"author diperbarui menjadi {new_author}")

    # getter
    def get_price(self):
        return self.__price
    
    # setter
    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
            print(f"buku '{self.__title}' di perbarui menjadi Rp. {new_price}")

    # getter untuk stock
    def get_stock(self):
        return self.__stock
    
    # setter untuk stock
    def set_stock(self, new_stock):
        if new_stock > 0:
            self.__stock = new_stock
            print(f"stock buku ")

    def info(self):
        print(f"judul buku {self.__title}, penulis {self.__author} dengan harga Rp. {self.__price}")

book1 = Book("Laskar pelangi", "andrea", 50000, 12)
book2 = Book("naruto", "masashi moto", 50000, 10)
book3 = Book("filosofi teras", "henry M", 45000, 11)
book4 = Book("learning python", "-", 65000, 15)

book1.set_title("laskar")

book1.info()