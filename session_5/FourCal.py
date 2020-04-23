class FourCal:
    def __init__(self, name, age, university):
        self.name = name
        self.age = age
        self.university = university
        self.add_num = 0
        self.subtract_num = 0
        self.divide_num = 0
        self.multiply_num = 0

    def add(self, n1, n2):
        self.add_num += 1
        return n1 + n2


    def subtract(self, n1, n2):
        self.subtract_num += 1
        return n1 - n2

    def divide(self, n1, n2):
        self.divide_num += 1
        return n1 / n2

    def multiply(self, n1, n2):
        if n2 == 0:
            print("0으로 나눌 수 없습니다.")
            return None
        self.multiply_num += 1
        return n1 * n2

    def ShowCount(self):
        print("덧셈: %d" % self.add_num)
        print("뺄셈: %d" % self.subtract_num)
        print("곱셈: %d" % self.divide_num)
        print("나눗셈: %d" % self.multiply_num)


calculator1 = FourCal("류지현", 23, "고려대학교")
print(calculator1.name, calculator1.age, calculator1.university)
print(calculator1.add(15,5))
print(calculator1.subtract(15,5))
print(calculator1.multiply(15,5))
print(calculator1.divide(15,5))

print(calculator1.ShowCount())