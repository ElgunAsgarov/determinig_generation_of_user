birth_year = int(input("What year you were born"))

if birth_year >= 1946 and birth_year <= 1964:
    print ("You are baby boomer")
elif birth_year >= 1965 and birth_year <= 1980:
    print ("you are member of generation X")
elif birth_year >= 1981 and birth_year <= 1996:
    print ("you are millennial")
elif birth_year >= 1997 and birth_year <= 2012:
    print ("you are member of generation Z")
elif birth_year >= 2013:
    print ("you are member of generation Alpha")    
else:
    print ("Error. Please enter a four-digit year, 1946 or later")