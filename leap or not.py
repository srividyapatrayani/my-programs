def is_leap(year):
    leap = False
    if(year%4!=0):
        return leap
    else:
        print("True")

year = int(raw_input())
print is_leap(year)
