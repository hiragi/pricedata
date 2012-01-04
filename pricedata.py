# -*- coding: utf-8 -*-
from BeautifulSoup import BeautifulSoup
import sys
from optparse import OptionParser
import urllib2

URL = "http://www.monex.com/liveprices"

html = urllib2.urlopen(URL).read()
soup = BeautifulSoup(html)

def scrape_price():
	"""
	scraping bullion prices

	Rerurns: all bullion prices as array
	"""
	_prices = []
	_values = (soup("td", {"class": "numeric"}))
	for i, value in enumerate(_values):
		if i > 15: break
		if i % 5 == 0:
			_prices.append(value.renderContents())
	
	return _prices

def parse_options():
	"""
	-g 		- display gold price data
	-s 		- display silver price data
	-p 		- display platinum price data
	-a 		- display palladium price data
	Default - display all price data
	"""
	usage = "%prog [options]"
	parser = OptionParser()
	parser.add_option("-g", "--gold", dest="gold", action="store_true", help="display gold data")
	parser.add_option("-s", "--silver", dest="silver", action="store_true", help="display silver data")
	parser.add_option("-p", "--platinum", dest="platinum", action="store_true", help="display platinum data")
	parser.add_option("-a", "--palladium", dest="palladium", action="store_true", help="display palladium data")

	(options, args) = parser.parse_args(sys.argv[1:])

	return options, args

def main():

	options, args = parse_options()
	price = scrape_price()

	if options.gold:
		print("Gold\t%s" % price[0])
	elif options.silver:
		print("Silver\t%s" % price[1])
	elif options.platinum:
		print("Platinum\t%s" % price[2])
	elif options.palladium:
		print("Palladium\t%s" % price[3])
	else:
		print("Gold\t\t%s\nSilver\t\t%s\nPlatinum\t%s\nPalladium\t%s" % (price[0], price[1], price[2], price[3]))

if __name__ == "__main__":
	main()
