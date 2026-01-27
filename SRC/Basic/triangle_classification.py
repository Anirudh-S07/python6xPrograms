def triangle_classifier():
    a = float(input(" Enter first side length "))
    b = float(input(" Enter second side length "))
    c = float(input(" Enter third side length "))

    if a+b > c and b+c > a and c+a > b:
        if a == b == c:
            print("This is an equilateral triangle")
        elif a == b or b == c or a == c:
            print("This a isoceles Triangle")
        else:
            print("This a scalene")
    else:
        print("This is not a triangle")


triangle_classifier()


