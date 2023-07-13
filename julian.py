
import datetime as dt


m_dict = {
"January" : 1,
"February" : 2,
"March" : 3,
"April" : 4,
"May" : 5,
"June" : 6,
"July" : 7,
"August" : 8,
"September" : 9,
"October" : 10,
"November" : 11,
"December" : 12
}


def julian_check(y, m, d):
	work = []
	if m == "January":
		if int(y) < 2100:
			a = dt.datetime(int(y), m_dict[m], int(d)) - dt.timedelta(days = 13)
		else:
			a = dt.datetime(int(y), m_dict[m], int(d)) - dt.timedelta(days = 14)
		if a.day == 1:
			work.append("New Year's Day (Julian Calendar)")
			work.append("Yennayer 1")
	return work
