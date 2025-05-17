# Assignment 1

class SmartPhone:
    def __init__(self, brand, model, storage, color):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.color = color

smartPhone1 = SmartPhone("Apple", "iPhone 14", "128GB", "Black")
smartPhone2 = SmartPhone("Samsung", "Galaxy S23", "256GB", "White")


class Tablet(SmartPhone):
    pass

tablet1 = Tablet("Apple", "iPad Pro", "512GB", "Silver")
tablet2 = Tablet("Samsung", "Galaxy Tab S8", "128GB", "Black")


class Apple(SmartPhone):
    def __init__(self, brand, model, storage, color):
        super().__init__(brand, model, storage, color)
        self.operating_system = "iOS"


class Samsung(SmartPhone):
    def __init__(self, brand, model, storage, color):
        super().__init__(brand, model, storage, color)
        self.operating_system = "Android"

for smartPhone in [smartPhone1, smartPhone2]:
    print(f"Brand: {smartPhone.brand}, Model: {smartPhone.model}, Storage: {smartPhone.storage}, Color: {smartPhone.color}")

apple_device = Apple("Apple", "iPhone 14 Pro", "256GB", "Gold")
samsung_device = Samsung("Samsung", "Galaxy S23 Ultra", "512GB", "Green")

for device in [apple_device, samsung_device]:
    print(f"Brand: {device.brand}, Model: {device.model}, OS: {device.operating_system}")

# Activity 2

class Falcon:
    def move(self):
        return "The falcon flies high in the sky."

class Shark:
    def move(self):
        return "The shark swims swiftly in the ocean."
    
for animals in [Falcon(), Shark()]:
    print(animals.move())