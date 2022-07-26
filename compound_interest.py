if __name__=="__main__":
    P = int (input("Enter Principle:"))
    T = int (input("Enter Time:"))
    R = float(input("Enter Rate:"))

    CIF = P * pow((1 + R / 100),T)

    print ("Compound Interest =", float(CIF))
    
    
