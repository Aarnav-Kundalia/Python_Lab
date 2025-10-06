a = input("Enter base number")
b = input("Enter power number: ")
def convert(a, b):    
    try:
        return int(a), int(b)
    except:
        try:
            return float(a), float(b)
        except:
            try:
                return complex(a.replace(' ', '')), complex(b.replace(' ', ''))
            except:
                raise ValueError("Input is a string, not a number")
            
a, b = convert(a, b)

while b > 0:
    a *= a
    b -= 1

print(f"The power of the number is {a}")