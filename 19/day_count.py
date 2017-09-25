#!/usr/bin/python

# returns 1..N for the n days in a month
def mdays(days):
	return range(1, days + 1)

# Uses a couple lookup lists to calculate dayOfWeek and dayOfMonth information per day of year
# to be summarized and filtered. Length is returned since it's all we need.
def summarize_year(year):
	months = []
	dom = []

	if year % 4 == 0:
		if year % 100 == 0 and year % 400 != 0:
			leap_year = 0
		else:
			leap_year = 1
	else:
		leap_year = 0

	month_lengths = [31, 28 + leap_year, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

	for mo in range(1, 13):
		months += [mo] * month_lengths[mo - 1]
		dom += mdays(month_lengths[mo - 1])

	data = dict([(x+1, {'month': y, 'dow': ((x + year - 2) % 7) + 1, 'dom': dom[x]}) for x,y in enumerate(months)])
	return len({k:v for k,v in data.iteritems() if v['dow'] == 1 and v['dom'] == 1})

# Loop through years and count total special days per year.
count = 0
for year in range(1901, 2001):
	count += summarize_year(year)

print("Special Sundays: {}".format(count))
