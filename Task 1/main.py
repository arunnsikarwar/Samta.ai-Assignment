def calculate_area(length, width):   #function to calculate area and check if is square or not
    if length == width:
        return "This is a square!"
    else:
        return length * width

def main():
    length = float(input("Enter the length: "))    #Taking input from user for length of rectangle
    width = float(input("Enter the width: "))      #Taking input from user for breadth of rectangle
    
    result = calculate_area(length, width)   #calling the function calculate_area for getting the result
    
    if isinstance(result, str):              #Checking the function is returning string or area
        print(result)
    else:
        print(f"The area of the rectangle is: {result}")

if __name__ == "__main__":
    main()
