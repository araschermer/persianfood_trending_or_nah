import twitter

api = twitter.Api(consumer_key =        '*********************************',
                  consumer_secret =     '*********************************',
                  access_token_key =    '*********************************',
                  access_token_secret = '*********************************')

if api.VerifyCredentials():
    print('keys have worked\n')

trends = api.GetTrendsCurrent()

for trend in trends:
	if trend.name == ('#persianfood'):
    		print("#persianfood is finally trending\n")    
	else:
    		print("#persianfood isn't trending :(\n")
    		break
