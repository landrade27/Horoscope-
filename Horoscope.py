
import requests



print "What is your birthday (month and day)? Ex: 01/09"
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
chosen_sign = birthday_sign (int(birthday[0]), int(birthday[1]))

print """What type of reading would you like?
A: Daily Horoscope reading
B: Weekly Horoscope Reading
C: Monthly Horoscope reading"""

user_input = raw_input()

readings_requests= requests.get("http://www.api.littleastro.com/restserver/index.php/api/horoscope/readings/format/json")
readings = readings_requests.json()
sign_reading = None

for sign in readings: 
	if sign ["Sign"]== chosen_sign: 
		reading=sign 

if user_input == "A":
	print sign ["Daily_Horoscope"]
elif user_input == "B":
	print sign ["Weekly_Horoscope"]
elif user_input == "C":
	print sign ["Monthly_Horoscope"]

