class Solution:
    def karatsuba(self, x, y):
        if len(x) == 1 or len(y) == 1:
            return int(x) * int(y)


        n = max(len(x), len(y))
        m=n//2


        x = x.zfill(n)
        y = y.zfill(n)

        x_high = x[:-m]
        x_low = x[-m:]
        y_high = y[:-m]
        y_low = y[-m:]


        a = self.karatsuba(x_low, y_low)            
        b = self.karatsuba(x_high, y_high)          
        c = self.karatsuba(str(int(x_low) + int(x_high)), str(int(y_low) + int(y_high))) - a - b

        return (b * 10**(2*m)) + (c * 10**(m)) + a
    
    def multiply(self, num1: str, num2: str) -> str:
        return str(self.karatsuba(num1,num2))

