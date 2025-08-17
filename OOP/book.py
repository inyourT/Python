class Book:
    def __init__(self, title, author, price, stock):
        self._title = title
        self.author = author
        self._price = price
        self.stock = stock

    @property
    def title (self):
        return self._title
    
    @title.setter
    def title(self, new_title):
        if not isinstance(new_title, str) or not new_title.strip():
            raise ValueError("Title tidak boleh kosong")
        self._title = new_title.strip()

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, new_price):
        if not isinstance(new_price, (int, float)) or new_price <= 0:
            raise ValueError("Harga tidak boleh kosong !!")
        self._price = new_price

    def __str__(self):
       return(f"judul buku {self.title}, penulis {self.author} dengan harga Rp. {self.price}")
    
    def info(self):
        print(str(self))

book1 = Book("Laskar pelangi", "andrea", 50000, 12)
book1.info()

book1.title = "pelangi"
book1.info()

book1.price = 1
book1.info()