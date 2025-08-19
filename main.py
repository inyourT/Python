from abc import ABC,abstractmethod

class Product(ABC):
    def __init__(self, title, author, price, stock=0):
        self._title = title
        self.author = author
        self._price = price
        self.stock = stock

    @abstractmethod
    def info (self):
        pass

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, new_title):
        if not new_title.strip():
            raise ValueError("Juduk tidak boleh kosong")
        self._title = new_title

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            raise ValueError("Harga harus lebih dari 0")
        self._price = new_price
    
    def __str__(self):
        return f"{self.__class__.__name__} | {self.title}, harga Rp. {self.price}, stock {self.stock}"
    

class Book(Product):
   def info(self):
       return str(self)

class Ebook(Product):
    def __init__(self, title, author, price, file_size):
        super().__init__(title, author, price, stock=0)
        self.file_size = file_size
    
    def __str__(self):
         return f"{self.__class__.__name__} | {self.title}, harga Rp. {self.price}"
    
    def info(self):
        return str(self) + f", Ukuran File : {self.file_size}MB"

class Magazine(Product):
    def __init__(self, title, author, price, stock, edition):
        super().__init__(title, author, price, stock)
        self.edition = edition
    
    def info(self):
        return str(self) + f", Edisi: {self.edition}"


store = [
    Book("Laskar Pelangi", "Andrea Hirata", 50000, 10),
    Ebook("Python OOP", "GPT", 30000, 5),
    Magazine("Majalah Ilmiah", "Kimito", 15000, 30, 2025)
]

print("==dafrat Produk di toko==")
for item in store:
    print(item.info())


print("\n=== Update Harga & Stock ===")
store[0].price = 60000 
store[0].stock -= 2    
print(store[0].info())