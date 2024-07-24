import datetime
def future_date(yy,mm,dd):
    date=datetime.datetime.now()
    current_year = date.year
    current_month = date.month
    current_day = date.day
    if yy > current_year:
        return True
    elif yy < current_year:
        return False
    elif yy ==current_year:
        if mm> current_month:
            return True
        elif mm < current_month:
            return False
        elif mm == current_month:
            if dd >current_day:
                return True
            if dd < current_day:
                return False
            if dd == current_day:
                return False

yy = int(input("Year> "))
mm = int(input("Month> "))
dd = int(input("day> "))
x = future_date(yy,mm,dd)
print(x)
    
