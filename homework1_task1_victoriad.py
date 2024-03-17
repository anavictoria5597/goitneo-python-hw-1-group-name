#Homework 1 - Task 1
from datetime import datetime
from collections import defaultdict
def get_birthdays_per_week(users):
    birthday_per_week = defaultdict(list) 
    current_date = datetime.today().date()
    #print("Current Date:", current_date)
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        # Converting by the type date to the current year
        birthday_this_year = birthday.replace(year=current_date.year)
        #print("Birthday This Year:", birthday_this_year)
        if birthday_this_year < current_date:
            birthday_this_year = birthday.replace(year=current_date.year + 1)
        delta_days = (birthday_this_year - current_date).days
        #print("Birthday This Year:", birthday_this_year)
        #print("Delta Days:", delta_days)
        if 0 <= delta_days < 7:
            bday = birthday_this_year.strftime('%A')
            if bday == "Saturday" or bday == "Sunday":
                bday = "Monday"
            birthday_per_week[bday].append(name)
            # else:
            #     birthday_per_week[bday].append(name) #diferit
    for bday, names in birthday_per_week.items():
        names_str = ', '.join(names)
        print (bday + ':' + names_str)
    return birthday_per_week

get_birthdays_per_week(users=[
    {"name": "Maria", "birthday": datetime(1955, 3, 18)},
    {"name": "George", "birthday": datetime(1976, 3, 23)},
    {"name": "Victoria", "birthday": datetime(1980, 10, 21)},
    {"name": "Alex", "birthday": datetime(1974, 11, 30)},
    {"name": "Diana", "birthday": datetime(1990, 3, 20)} ])
           

