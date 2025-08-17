class Mobil:
    def __init__(self, merk, warna): #construct
        self.merk = merk
        self.warna = warna
    
    def info(self): # method
        print(f"Mobil {self.merk} berwarna {self.warna}") 

mobil1 = Mobil("Toyota", "merah")
mobil1.info()