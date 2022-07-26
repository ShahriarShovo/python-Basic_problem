if __name__=="__main__":

    eng= int (input("Enter the number of eng="))
    Phy= int (input("Enter the number of Phy="))
    chem= int (input("Enter the number of chem="))
    math= int (input("Enter the number of math="))
    comp= int (input("Enter the number of comp="))

    Sum=eng + Phy + chem + math + comp
    average=Sum / 5
    percentage=(Sum / 500) * 100

    print("Total=", float(Sum))
    print("Average=", float(average))            
    print("Percentage=", float(percentage))            

                
