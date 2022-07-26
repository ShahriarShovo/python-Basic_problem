if __name__=="__main__":
    days=int (input ("Enter days:"))


    year=days/365
    weeks=(days - (year*365)) / 7
    days= days-((year*365) + (weeks*7))

    print("373 days=", int(year),"year/s,",  int (weeks),"week/s  and", int (days),"day/s.")
    
