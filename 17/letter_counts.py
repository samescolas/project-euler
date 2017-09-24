#!/usr/bin/python

def num2word(n):
	words = { 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen', 20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety', 100:'hundred'}
	if n <= 0:
		return ''
	word = {'ones' : '', 'tens' : '', 'hundreds': ''}
	if n <= 20:
		word['ones'] = words[n]
		#return words[n]
	elif n < 100:
		word['ones'] = (' ' + words[n%10]) if n%10 != 0 else ''
		word['tens'] = words[10 * (n/10)]
	elif n < 1000:
		word['hundreds'] = words[n/100]
		return "{} hundred{}".format(word['hundreds'], (' and ' + num2word(n%100) if num2word(n%100) != '' else ''))
	return "{}{}".format(word['tens'], word['ones'])

length = 0
for i in xrange(1, 1000):
	word = num2word(i)
	length += (len(word) - word.count(' '))

print("Total length: {}".format(length + len("onethousand")))
