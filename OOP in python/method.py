
class calculator:
    Brand = 'Casio ms990'
    
    def subtraction(self,num1,num2):
        result = num1 - num2
        return result
    def multiplication(self,num1,num2):
        result = num1 * num2
        return result
    def division(self,num1,num2):
        result = num1 / num2
        return result
    
    
my_calculator = calculator()
print(my_calculator.Brand)
print(my_calculator.subtraction(5,3))
print(my_calculator.multiplication(2,3))
print(my_calculator.division(6,3))