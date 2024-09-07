from abc import ABC, abstractmethod

# Kelas dasar untuk semua burung
class Bird(ABC):
    @abstractmethod
    def move(self):
        pass

# Kelas khusus untuk burung yang bisa terbang
class FlyingBird(Bird):
    @abstractmethod
    def fly(self):
        pass

# Kelas khusus untuk burung yang tidak bisa terbang
class NonFlyingBird(Bird):
    @abstractmethod
    def walk(self):
        pass

# Implementasi subkelas burung yang bisa terbang
class Sparrow(FlyingBird):
    def fly(self):
        print("Sparrow is flying!")
    
    def move(self):
        self.fly()

class Eagle(FlyingBird):
    def fly(self):
        print("Eagle is soaring high!")
    
    def move(self):
        self.fly()

# Implementasi subkelas burung yang tidak bisa terbang
class Penguin(NonFlyingBird):
    def walk(self):
        print("Penguin is walking!")
    
    def move(self):
        self.walk()

# Fungsi yang sekarang menggunakan metode 'move' sesuai dengan jenis burung
def let_bird_move(bird: Bird):
    bird.move()

# Contoh penggunaan
sparrow = Sparrow()
eagle = Eagle()
penguin = Penguin()

let_bird_move(sparrow)  # Output: Sparrow is flying!
let_bird_move(eagle)    # Output: Eagle is soaring high!
let_bird_move(penguin)  # Output: Penguin is walking!
