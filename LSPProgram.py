from abc import ABC, abstractmethod

# Kelas Dasar
class Bird(ABC):
    @abstractmethod
    def fly(self):
        pass

# Memperoleh Kelas - sesuai dengan LSP
class Sparrow(Bird):
    def fly(self):
        print("Sparrow is flying!")

# Memperoleh kelas - Pelanggaran LSP karena Penguin tidak bisa terbang
class Penguin(Bird):
    def fly(self):
        raise Exception("Penguins can't fly!")

# Memperoleh kelas - sesuai dengan LSP
class Eagle(Bird):
    def fly(self):
        print("Eagle is soaring high!")

# Function untuk demo LSP
def let_bird_fly(bird: Bird):
    bird.fly()

# Substitusi valid sesuai LSP
sparrow = Sparrow()
eagle = Eagle()

let_bird_fly(sparrow)  # Output: Sparrow is flying!
let_bird_fly(eagle)    # Output: Eagle is soaring high!

# Pelanggaran Penguin ke LSP
penguin = Penguin()
try:
    let_bird_fly(penguin)  
except Exception as e:
    print(e)  # Output: Penguins can't fly!
