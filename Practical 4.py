try:
    V = float(input("Enter voltage (V): "))
    R = float(input("Enter resistance (Ohms): "))
    if R <= 0:
        print("Invalid resistance!")
    else:
        I = V / R
        print(f"Current: {I:.2f} A")
        if I > 10:
            print("High current! Circuit may get damaged.")
        elif I > 5:
            print("Moderate current.")
        else:
            print("Low current, safe circuit.")
except ValueError:
    print("Invalid input. Please enter numeric values.")
    