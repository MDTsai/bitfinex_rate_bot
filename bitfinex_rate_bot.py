import datetime
import json
import requests
import time

CURRENCY = "USD"
BFX_URL = "https://api-pub.bitfinex.com/v2/trades/f{}/hist".format(CURRENCY)
BFX_SLEEP_INTERVAL = 60
BFX_HISTORY_INTERVAL = 5

TG_BOT_API = "BOT API KEY"
TG_CHAT_ID = "CHAT ID"
TG_URL = "https://api.telegram.org/bot{}/sendMessage".format(TGBOT_API)

APY_THRESHOLD = 10

def parseTrades(trades):
	if len(trades) > 0:

		rate = []
		for trade in trades:
			rate.append(trade[3])

		# Convert lending rate to APY
		apy = (sum(rate)/len(rate))*100*365

		if apy > APY_THRESHOLD:
			param = {
				"chat_id": TG_CHAT_ID,
				"text": "USD Funding Rate: {:.2f}%".format(apy)
			}

			response = requests.request("GET", TG_URL, params = param)
	

while True:
	# Track last 5 minutes fUSD trades only
	start = datetime.datetime.now() - datetime.timedelta(minutes=BFX_HISTORY_INTERVAL)
	param = { "start": start.timestamp()*1000 }

	response = requests.request("GET", BFX_URL, params = param)
	parseTrades(json.loads(response.text))
	time.sleep(BFX_SLEEP_INTERVAL)
