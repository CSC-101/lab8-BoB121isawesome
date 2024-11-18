
total=0.0
try:
    input = input("Enter a file name to open: ")
    with open(input, "r") as file:
        for line in file:
            values=line.split()
            if len(values)!=2:
                continue
            try:
                num1=float(values[0])
                num2=float(values[1])
                total+=num1+num2
                print(f"Current sum: {total}")
            except ValueError:
                print("Missing or Not a number")
except FileNotFoundError:
    print("Please enter a valid file name.")
    exit()

