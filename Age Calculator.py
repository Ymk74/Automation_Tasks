Year = int(input('Enter Year='))
Month = int(input('Enter Month='))
Day = int(input('Enter Day='))
from datetime import date

def calculateAge(birthDate):
	days_in_year = 365.2425
	age = int((date.today() - birthDate).days / days_in_year)
	return age
		
# Driver code
print(calculateAge(date(Year, Month, Day)), "years")
