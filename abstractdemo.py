class MyClass:
    pass
class Calculator:
    def addition(self,var1,var2):
        pass
    def subtraction(self, var1,var2):
        pass
class Add(Calculator):
    def addition(self,var1,var2):
        print("Addition of two numbers is ",(var1+var2))
a=Add()
a.addition(10,20)