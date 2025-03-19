try:
    num = int(input("Enter the number to generate a multiplication table: "))
    start = int(input("Enter the starting multiplier: "))
    end = int(input("Enter the ending multiplier: "))

    if start > end:
        print("Invalid input! The starting number must be less than or equal to the ending number.")
    else:
        print(f"\nMultiplication Table for {num} from {start} to {end}:\n")
        for i in range(start, end + 1):
            print(f"{num} x {i} = {num * i}")
except ValueError:
    print("Please enter a valid integer.")
