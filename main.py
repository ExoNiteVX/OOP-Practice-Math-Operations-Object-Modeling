import time


class Math:
    def init(self, a, b):
        self.a = a
        self.b = b

class Adder(Math):
    def add(self):
        return self.a + self.b

class Subtractor(Math):
    def subtract(self):
        return self.a - self.b

class Mult(Math):
    def multiply(self):
        return self.a * self.b

class Divi(Math):
    def divide(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Bor aylanib ke!!!!"


a = int(input("Birinchi sonni kiriting: "))
b = int(input("Ikkinchi sonni kiriting: "))


add = Adder(a, b)
sub = Subtractor(a, b)
mul = Mult(a, b)
div = Divi(a, b)


print("Qo‘shish:", add.add())
print("Ayirish:", sub.subtract())
print("Ko‘paytirish:", mul.multiply())
print("Bo‘lish:", div.divide())


time.sleep(6)
print("-------------------------------")
print("-------------------------------")
print("-------------------------------")
print("Standart task 1")


class komputer:
    def init(self, egasi, protsessor, operatsion, xotira, RAM, monitor):
        self.egasi = egasi
        self.protsessor = protsessor
        self.operation = operatsion
        self.xotira = xotira
        self.RAM = RAM
        self.monitor = monitor

komp = komputer("Asilbek","Ryzen 9 9800","Linux",2,128,"ASUS ROG Swift OLED PG27AQDM")
print(f"egasi : {komp.egasi}\n"
      f"protsessor : {komp.protsessor}\n"
      f"operation : {komp.operation}\n"
      f"xotira : {komp.xotira}T\n"
      f"RAM : {komp.RAM}GB\n"
      f"monitor : {komp.monitor}")

print("-------------------------------------------------")

class komputer2:
    def init(self, egasi, protsessor, operatsion, xotira, RAM, monitor):
        self.egasi = egasi
        self.protsessor = protsessor
        self.operation = operatsion
        self.xotira = xotira
        self.RAM = RAM
        self.monitor = monitor

kopm = komputer2("Toshmat","Core i9","Windows 11",1,64,"HP OLED")
print(f"egasi : {kopm.egasi}\n"
      f"protsessor : {kopm.protsessor}\n"
      f"operation : {kopm.operation}\n"
      f"xotira : {kopm.xotira}T\n"
      f"RAM : {kopm.RAM}GB\n"
      f"monitor : {kopm.monitor}")

print("---------------------------------------------------")

print("Solishtruv (xotira)")

print(komp.xotira > kopm.xotira)
print(komp.xotira >= kopm.xotira)
print(komp.xotira < kopm.xotira)
print(komp.xotira <= kopm.xotira)

print("Solishtruv (RAM)")
print(komp.RAM > kopm.RAM)
print(komp.RAM >= kopm.RAM)
print(komp.RAM < kopm.RAM)
print(komp.RAM <= kopm.RAM)

time.sleep(6)
print("-------------------------------")
print("-------------------------------")
print("-------------------------------")
print("Pro task 1")


class Student1:
    def init(self, name, age, group):
        self.name = name
        self.age = age
        self.group = group

    def get_name(self):
        return self.name
    def set_name(self, newname):
        self.name = newname

    def get_age(self):
        return self.age
    def set_age(self, newage):
        self.age = newage

    def get_group(self):
        return self.group
    def set_group(self, newgroup):
        self.group = newgroup

info  = Student1("Ivan",18,"10A")

print(info.name)
print(info.age)
print(info.group)

print("----------------------------------------------------------------")
info.set_name("John")
print(info.get_name())
info.set_age(25)
print(info.get_age())
info.set_group("12B")
print(info.get_group())

time.sleep(6)