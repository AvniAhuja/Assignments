def print_lower_triangle(n):
    for i in range(1, n + 1):
        print('* ' * i)

def print_upper_triangle(n):
    for i in range(n, 0, -1):
        print('* ' * i)

def print_pyramid(n):  
    for i in range(1, n + 1):     
        print(' ' * (n - i), end='')
        print('* ' * i)

def main():
    while True:
        try:
            n = int(input("Enter the size of the patterns (a positive integer): "))
            if n <= 0:
                print("Please enter a positive integer!")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a number.")
    
    print("\nLower Triangular Pattern:")
    print_lower_triangle(n)
    
    print("\nUpper Triangular Pattern:")
    print_upper_triangle(n)
    
    print("\nPyramid Pattern:")
    print_pyramid(n)

if __name__ == "__main__":
    main() 