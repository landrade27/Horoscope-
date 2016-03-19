
print "What is your birthday? EX: 01/09/1989"
birthday= raw_input()  
birthday= birthday.split("/")
print birthday 
signs_dictionary = { 
				1: {"split_day" :19, "less_sign": "Capricorn", "greater_sign": "Aquarius"},
				2: {"split_day":18, "less_sign": "Aquarius", "greater_sign": "Pisces"},
				3: {"split_day":20, "less_sign": "Pisces", "greater_sign": "Aries"},
				4: {"split_day":19, "less_sign": "Aries", "greater_sign": "Taurus"},
				5: {"split_day":20, "less_sign": "Taurus", "greater_sign": "Gemini"},
				6: {"split_day":20, "less_sign": "Gemini", "greater_sign": "Cancer"},
				7: {"split_day":22, "less_sign": "Cancer", "greater_sign": "Leo"},
				8: {"split_day":23, "less_sign": "Leo", "greater_sign": "Virgo"},
				9: {"split_day":22, "less_sign": "Virgo", "greater_sign": "Libra"},
				10: {"split_day":22, "less_sign": "Libra", "greater_sign": "Scorpio"},
				11: {"split_day":21, "less_sign": "Scorpio", "greater_sign": "Sagitarious"},
				12: {"split_day":21, "less_sign": "Sagitarious", "greater_sign": "Capricorn"}
				}
				# split_Day: 20 (is <=)
def birthday_sign (month, day):
	potential_sign= signs_dictionary[month]
	if day <= potential_sign ["split_day"]:
		return potential_sign["less_sign"]
	else:
		return potential_sign["greater_sign"]
print birthday_sign (int(birthday[1]), int(birthday[0]))

print "What type of reading would you like?"
print raw_input ("A: Yearly Horoscope reading")		
print raw_input ("B: Monthly Horoscope Reading")
print raw_input ("C: Weekly Horoscope reading")
reading = raw_input()

# def type_of_reading ():
# 	if raw_input= "A":
# 		print yearly_reading #need API for yearly horsicope reading 
# 	if raw_input= "B":
# 		print monthly_reading #need API for monthly horiscope reading 
# 	if raw_input = "C":
# 		print weekly_reading #need API for weekly horiscope reading 
# 	else:
# 		print "Please enter A, B or C, in upper case to get to your reading" 

# def birthday_reading ( )
# # reading = raw_input ("What type of reading would you like? A) Weekly Horiscope Reading B) Monthly Horiscope Reading C) Yearly Horiscope Reading")



