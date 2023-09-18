class Test:
    name = "Bharath Reddy"
    def method2(self, value):
        self.name=value
    def display(self):
        print(self.name)



t1 = Test()
t2 = Test()

t1.method2("Rahul Reddy")
t2.display()
t1.display()