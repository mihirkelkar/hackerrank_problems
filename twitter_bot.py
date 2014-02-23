#-------------------------------------------------------------------------
#Trying to create a twitter bot which tweets out the temperature for Baltimore, MD. Every hour.
#--------------------------------------------------------------------------
from twitter import Twitter, OAuth, TwitterHTTPError
import tempscrapper
from random import choice
OAUTH_TOKEN = "2325991994-AUC6xhDw39APx9UBQmmPomFaQlte3OKJOkOwErq"
OAUTH_SECRET = "4W5uG8I7OVuSSadptlq9B0AwJRDsT7fb3ZmyG99l6vaot"
CONSUMER_KEY = "uZbtNV4143cTZEDzz60LkQ"
CONSUMER_SECRET = "wZN5LTC7qwUL0ElUCwxGA5dlZHE1yYcGl3y7Eo6M"

t = Twitter(auth = OAuth(OAUTH_TOKEN, OAUTH_SECRET, CONSUMER_KEY, CONSUMER_SECRET))

def get_temperature():
	tempscrapper.find()
	fp = open('temperature', r'U')
	temperature = fp.readlines()[-1].strip()
	temperature
	return temperature

def tweet_temperature():
	fucking_cold = ["Yo! Shits' Frozen here, its about ", "Much feezing , So cold, Wow! ", "Holy Shit poop its cold. ", "Do not try peeing outside. seriously don't. Its ", "My face hurts in the cold. Its bloody ", "Danny forgot to get his jacket. Danny died. Murderous temperature -> ", "Weather FUUUUUUU  ->  "]

	freezing = ["Damn, its cold ", "Well, atleast Canada is Colder. Charm City -> ", "Nope. Can't deal with the cold. Nope. Its ", "Winter? What are you doing? Winter STAAHP "]

	very_cold = ["Grab a jacket folks, Its ", "Holy! Shit Poops! We might actually see liquid water today? -> ", "Coooollllddddd "]

	cold = ["Russian Summer Temperatures. Its ", "Sweater weather is here.Its ", "Meh ! The temperature is ", "Not so cold, not so hot either. Gotta love Baltimore.Its "]
	
	ten_and_twenty = ["Ooh! Its nice outside ", "The temperature is ", "Dam.Good weather ", "Nice. Its "]
	
	twenty_and_thirty = ["Pretty warm ", "Quite warm ", "To the Beach. Its ", "Charm city at ", "Meh! its "]
	
	lower_thirty = ["Getting a bit too hot for my liking ", "Hot. Really Hot. its ", "Oh I miss the mid sixties. its ", "Damn! its "]
	
	hot = ["Holy! Fuc*! its f**king hot!", "Shits' on fire yo! ", "Goddamm heat ! ", "Summer what are you doing ? Summer STAHP. ", "Godamn Hot and Humid ", "This is Baaaaaaaaltimore...... "]
	temperature = int(get_temperature())
	#----Temperatures below 10 degrees-----------
	if temperature < 10:
		statust = choice(fucking_cold) + str(temperature) + "F"
	#------Temperatures above 10 and below 32---------
	elif((temperature >= 10) and (temperature < 25)):
		statust = choice(freezing) + str(temperature) + "F"
	#-------Temperatures above 25 and below 40---------
	elif((temperature >= 25) and (temperature < 40)):
		statust = choice(very_cold) + str(temperature) + "F"
	#-------Temperatures in the one digits celcius--------------
	elif((temperature >= 40) and (temperature < 50)):
		statust = choice(cold) + str(temperature) + "F"
	#------------Make a comfortable temperature quote-----------
	elif((temperature >= 50) and (temperature < 70)):
		statust = choice(ten_and_twenty) + str(temperature) + "F" 
	elif ((temperature >= 70) and (temperature < 85)):
		statust = choice(twenty_and_thirty) + str(temperature) + "F"
	elif ((temperature >= 85) and (temperature < 92)):
		statust = choice(lower_thirty) + str(temperature) + "F"
	elif (temperature >= 92):
		statust = choice(hot) + str(temperature) + "F"	
	try:
		print statust
		t.statuses.update(status = statust + " #baltimore " + "#weather")
		print "Status Updated"
	except:
		print "Something went wrong during the Status Update, deal with it"

def main():
	tweet_temperature()
if __name__ == "__main__":
	main()
