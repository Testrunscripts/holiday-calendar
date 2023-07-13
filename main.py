
import calendar
import webbrowser

import datetime as dt
import tkinter as tk

import holidays as h
import holiday_dicts as dict
import julian as jul


options = [
"January",
"February",
"March",
"April",
"May",
"June",
"July",
"August",
"September",
"October",
"November",
"December"
]

options1 = [
"1",
"2",
"3",
"4",
"5",
"6",
"7",
"8",
"9",
"10",
"11",
"12",
"13",
"14",
"15",
"16",
"17",
"18",
"19",
"20",
"21",
"22",
"23",
"24",
"25",
"26",
"27",
"28",
"29",
"30",
"31"
]

options2 = [
"2020",
"2021",
"2022",
"2023",
"2024",
"2025",
"2026",
"2027",
"2028",
"2029",
"2030",
"2031",
"2032",
"2033",
"2034",
"2035",
"2036",
"2037",
"2038",
"2039",
"2040",
"2041",
"2042",
"2043",
"2044",
"2045",
"2046",
"2047",
"2048",
"2049",
"2050"
]

dt_months = {
1 : "January",
2 : "February",
3 : "March",
4 : "April",
5 : "May",
6 : "June",
7 : "July",
8 : "August",
9 : "September",
10 : "October",
11 : "November",
12 : "December"
}

weekdays = {
0 : "Monday",
1 : "Tuesday",
2 : "Wednesday",
3 : "Thursday",
4 : "Friday",
5 : "Saturday",
6 : "Sunday",
}


menu = False
page = 1


def page_switch(can, x = 0):
	global page
	print("test1", page)
	can.delete("all")
	scroller = tk.Scrollbar(menu_frm, orient = "vertical", command = can.yview)
	scroller.pack(side = "right", fill = "y")
	can.pack(side = "left", fill = "y")
	nfrm = tk.Frame(can, bg = "light grey")
	nfrm.bind(lambda e: can.configure(scrollregion = can.bbox("all")))
	can.create_window((0, 0), window = nfrm, anchor = "nw")
	can.config(yscrollcommand = scroller.set)
	can.yview_moveto(0.0)
	if x == 0:
		pg_lbl = tk.Label(nfrm, text = page + 1, bg = "light grey")
		pg_lbl.pack(padx= 5, pady = 5)
	else:
		if page != 1:
			pg_lbl = tk.Label(nfrm, text = page - 1, bg = "light grey")
			pg_lbl.pack(padx= 5, pady = 5)
		else:
			pg_lbl = tk.Label(nfrm, text = page, bg = "light grey")
			pg_lbl.pack(padx= 5, pady = 5)
	bbtn = tk.Button(nfrm, text = "<- Previous Page", command = lambda c = can: page_switch(c, x = 1), bg = "light grey", relief = "flat", borderwidth = 0)
	bbtn.pack( padx = 5, pady = 5)
	fbtn = tk.Button(nfrm, text = "Next Page ->", command = lambda c = can: page_switch(c), bg = "light grey", relief = "flat", borderwidth = 0)
	fbtn.pack(padx = 5, pady = 5)
	if x == 0:
		page += 1
		try:
			for i in range(100):
				i = i + (100 * (page - 1))
				btn = tk.Button(nfrm, text = list(dict.holiday_dict)[i], wraplength = 900, command = lambda x = list(dict.holiday_dict)[i]: test_command(x), bg = "light grey", relief = "flat", borderwidth = 0)
				btn.pack(padx = 5, pady =5)
		except:
			pass
		bbtn = tk.Button(nfrm, text = "<- Previous Page", command = lambda c = can: page_switch(c, x = 1), bg = "light grey", relief = "flat", borderwidth = 0)
		bbtn.pack(side = "left", padx = 5, pady = 5)
		fbtn = tk.Button(nfrm, text = "Next Page ->", command = lambda c = can: page_switch(c), bg = "light grey", relief = "flat", borderwidth = 0)
		fbtn.pack(side = "right", padx = 5, pady = 5)
	else:
		if page == 1:
			try:
				for i in range(100):
					i = i
					btn = tk.Button(nfrm, text = list(dict.holiday_dict)[i], wraplength = 900, command = lambda x = list(dict.holiday_dict)[i]: test_command(x), bg = "light grey", relief = "flat", borderwidth = 0)
					btn.pack(padx = 5, pady =5)
			except:
				pass
			bbtn = tk.Button(nfrm, text = "<- Previous Page", command = lambda c = can: page_switch(c, x = 1), bg = "light grey", relief = "flat", borderwidth = 0)
			bbtn.pack(side = "left", padx = 5, pady = 5)
			fbtn = tk.Button(nfrm, text = "Next Page ->", command = lambda c = can: page_switch(c), bg = "light grey", relief = "flat", borderwidth = 0)
			fbtn.pack(side = "right", padx = 5, pady = 5)
		else:
			page -= 1
			try:
				for i in range(100):
					i = i + (100 * (page - 1)) 
					btn = tk.Button(nfrm, text = list(dict.holiday_dict)[i], wraplength = 900, command = lambda x = list(dict.holiday_dict)[i]: test_command(x), bg = "light grey", relief = "flat", borderwidth = 0)
					btn.pack(padx = 5, pady =5)
			except:
				pass
			bbtn = tk.Button(nfrm, text = "<- Previous Page", command = lambda c = can: page_switch(c, x = 1), bg = "light grey", relief = "flat", borderwidth = 0)
			bbtn.pack(side = "left", padx = 5, pady = 5)
			fbtn = tk.Button(nfrm, text = "Next Page ->", command = lambda c = can: page_switch(c), bg = "light grey", relief = "flat", borderwidth = 0)
			fbtn.pack(side = "right", padx = 5, pady = 5)

def search(url):
	try:
		webbrowser.open_new_tab(url)
	except:
		pass
		
def back_cal():
	pass

def back(m):
	global menu
	global menu_frm
	can1.yview_moveto(0.0)
	for w in info_frm.winfo_children():
		w.destroy()
	if m is True:
		try:
			menu_frm.destroy()
		except:
			pass
		menu = False
		btm_frm.lift()
		top_frm.lift()
	else:
		menu_frm = tk.Frame(root, bg = "light grey")
		menu_frm.grid(row = 1, column = 0, sticky = "news")
		can = tk.Canvas(menu_frm)
		scroller = tk.Scrollbar(menu_frm, orient = "vertical", command = can.yview)
		scroller.pack(side = "right", fill = "y")
		can.pack(side = "left", fill = "y")
		nfrm = tk.Frame(can, bg = "light grey")
		nfrm.bind(lambda e: can.configure(scrollregion = can.bbox("all")))
		can.create_window((0, 0), window = nfrm, anchor = "nw")
		can.config(yscrollcommand = scroller.set)
		pg_lbl = tk.Label(nfrm, text = page, bg = "light grey")
		pg_lbl.pack(padx= 5, pady = 5)
		bbtn = tk.Button(nfrm, text = "<- Previous Page", command = lambda c = can: page_switch(c, x = 1), bg = "light grey", relief = "flat", borderwidth = 0)
		bbtn.pack(padx = 1, pady = 1)
		fbtn = tk.Button(nfrm, text = "Next Page ->", command = lambda c = can: page_switch(c), bg = "light grey", relief = "flat", borderwidth = 0)
		fbtn.pack(padx = 5, pady = 5)
		menu = True
		menu_frm.lift()
		mtop_frm.lift()
		for i in range(100):
			btn = tk.Button(nfrm, text = list(dict.holiday_dict)[i], wraplength = 900, command = lambda x = list(dict.holiday_dict)[i]: test_command(x), bg = "light grey", relief = "flat", borderwidth = 0)
			btn.pack(padx = 5, pady =5)
		bbtn = tk.Button(nfrm, text = "<- Previous Page", command = lambda c = can: page_switch(c, x = 1), bg = "light grey", relief = "flat", borderwidth = 0)
		bbtn.pack(side = "left", padx = 5, pady = 5)
		fbtn = tk.Button(nfrm, text = "Next Page ->", command = lambda c = can: page_switch(c), bg = "light grey", relief = "flat", borderwidth = 0)
		fbtn.pack(padx = 5, pady = 5)
		menu = True
		menu_frm.lift()
		mtop_frm.lift()

def test_command(item):
	print("This is", item)
	global menu
	if menu is True:
		menu = False
	else:
		menu = True
	d = dt.date(int(year.get()), jul.m_dict[month.get()] , int(day.get())).weekday()
	print("TestA", d)
	prelbl = tk.Label(info_frm, text = weekdays[d] + ", " + month.get() + " " + day.get() + ", " + year.get(), wraplength = 1050, bg = "light grey")
	prelbl.pack(padx = 5, pady = 20)
	prelbl1 = tk.Label(info_frm, text = "______________________________________________\n", bg = "light grey")
	prelbl1.pack(padx = 5, pady = 5)
	lbl1 = tk.Label(info_frm, text = item, wraplength = 1050, bg = "light grey")
	lbl1.pack(padx = 5, pady = 20)
	lbl2 = tk.Label(info_frm, text = "___\n", bg = "light grey")
	lbl2.pack(padx = 5, pady = 5)
	lbl3 = tk.Label(info_frm, text = dict.holiday_dict[item][0], wraplength = 1050, bg = "light grey")
	lbl3.pack(padx = 5, pady = 5)
	lbl4 = tk.Label(info_frm, text = "___\n", bg = "light grey")
	lbl4.pack(padx = 5, pady = 5)
	lbl5 = tk.Label(info_frm, text = dict.holiday_dict[item][1], wraplength = 1050, bg = "light grey")
	lbl5.pack(padx = 5, pady = 5)
	lbl6 = tk.Label(info_frm, text = "___\n", bg = "light grey")
	lbl6.pack(padx = 5, pady = 5)
	lbl7 = tk.Label(info_frm, text = dict.holiday_dict[item][2], wraplength = 1050, bg = "light grey")
	lbl7.pack(padx = 5, pady = 5)
	lbl8 = tk.Label(info_frm, text = "___\n", bg = "light grey")
	lbl8.pack(padx = 5, pady = 5)
	lbl9 = tk.Label(info_frm, text = "To Wikipedia ->", wraplength = 1050, bg = "light grey", fg = "blue")
	lbl9.pack(padx = 5, pady = 5)
	lbl9.bind("<Button-1>", lambda e: search("https://en.m.wikipedia.org/wiki/" + dict.holiday_dict[item][3]))
	info_frm.lift()
	
def wipe():
	for w in info_frm.winfo_children():
		w.destroy()
	for w in nfrm1.winfo_children():
		w.destroy()
	btm_frm.lift()
	if month.get() in ("February", "April", "June", "September", "November"):
		if len(options1) > 30:
			options1.remove("31")
			pass
		if len(options1) < 30:
			if len(options1) < 29:
				options1.append("29")
			else:
				options1.append("30")
		if month.get() == "February":
			if len(options1) > 30:
				options1.remove("31")
			if len(options1) > 29:
				options1.remove("30")
			if int(year.get()) % 4 != 0:
				if len(options1) > 28:
					options1.remove("29")
			else:
				if int(year.get()) % 100 == 0:
					if len(options1) > 28:
						options1.remove("29")
	else:
		if len(options1) < 29:
			options1.append("29")
		if len(options1) < 30:
			options1.append("30")
		if len(options1) < 31:
			options1.append("31")
	d = day.get()
	day.set("")
	day_btn["menu"].delete(0, tk.END)
	for o in options1:
		day_btn["menu"].add_command(label = o, command = tk._setit(day, o))
	if d not in options1:
		day.set(options1[-1])
	else:
		day.set(d)

def holiday_check(m, d, y):
	wipe()
	z = h.check_holidays(m, d, y)
	z.sort()
	d = dt.date(int(year.get()), jul.m_dict[month.get()] , int(day.get())).weekday()
	prelblb = tk.Label(nfrm1, text = weekdays[d] + ", " + month.get() + " " + day.get() + ", " + year.get(), wraplength = 950, bg = "light grey")
	prelblb.pack(padx = 5, pady = 20)
	prelblb1 = tk.Label(nfrm1, text = "______________________________________________\n", bg = "light grey")
	prelblb1.pack(padx = 5, pady = 5)
	for item in z:
		btn = tk.Button(nfrm1, text = item, wraplength = 950, command = lambda item = item: test_command(item), bg = "light grey", relief = "flat", borderwidth = 0)
		btn.pack(padx = 5, pady = 5, side = "top")

def change_month(x = 0):
	can1.yview_moveto(0.0)
	m = month.get()
	index = options.index(m)
	if x == 0:
		pass
	elif x == 1:
		if index == 0:
			change_year(x = 1)
			month.set(options[-1])
		else:
			month.set(options[index - 1])
	elif x == 2:
		if index == len(options) - 1:
			change_year(x = 2)
			month.set(options[0])
		else:
			month.set(options[index + 1])
	holiday_check(month.get(), day.get(), year.get())
			
def change_day(x = 0):
	can1.yview_moveto(0.0)
	d = day.get()
	index = options1.index(d)
	if x == 0:
		pass
	elif x == 1:
		if index == 0:
			change_month(x = 1)
			day.set(options1[-1])
		else:
			day.set(options1[index - 1])
	elif x == 2:
		if index == len(options1) - 1:
			change_month(x = 2)
			day.set(options1[0])
		else:
			day.set(options1[index + 1])
	holiday_check(month.get(), day.get(), year.get())
			
def change_year(x = 0):
	can1.yview_moveto(0.0)
	y = year.get()
	index = options2.index(y)
	if x == 0:
		pass
	elif x == 1:
		if index == 0:
			year.set(options2[-1])
		else:
			year.set(options2[index - 1])
	elif x == 2:
		if index == len(options2) - 1:
			year.set(options2[0])
		else:
			year.set(options2[index + 1])
	holiday_check(month.get(), day.get(), year.get())


root = tk.Tk()


month = tk.StringVar()
month.set(dt_months[dt.datetime.now().month])

day = tk.StringVar()
day.set(dt.datetime.now().day)

year = tk.StringVar()
year.set(dt.datetime.now().year)

root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight = 1)
root.rowconfigure(1, weight = 100)

mtop_frm = tk.Frame(root, bg = "dark grey")
mtop_frm.grid(row= 0, column = 0, sticky = "news")

top_frm = tk.Frame(root, bg = "dark grey")
top_frm.grid(row= 0, column = 0, sticky = "news")

top_frm.columnconfigure(0, weight = 1)
top_frm.columnconfigure(1, weight = 2)
top_frm.columnconfigure(2, weight = 1)

stblzr = tk.Label(top_frm, text = "QQQQQQQQQQQQQQQ")
stblzr.grid(row = 0, column = 1)

monthb_btn = tk.Button(top_frm, text = "<-", command = lambda: change_month(x = 1))
monthb_btn.grid(row = 0, column = 0, sticky = "news", padx = 5, pady = 5)

month_btn = tk.OptionMenu(top_frm, month, *options, command = lambda x: change_month())
month_btn.grid(row = 0, column = 1, sticky = "news", padx = 5, pady = 5)

monthf_btn = tk.Button(top_frm, text = "->", command = lambda: change_month(x = 2))
monthf_btn.grid(row = 0, column = 2, sticky = "news", padx = 5, pady = 5)

dayb_btn = tk.Button(top_frm, text = "<-", command = lambda: change_day(x = 1))
dayb_btn.grid(row = 1, column = 0, sticky = "news", padx = 5, pady = 5)

day_btn = tk.OptionMenu(top_frm, day, *options1, command = lambda x: change_day())
day_btn.grid(row = 1, column = 1, sticky = "news",  padx = 5, pady = 5)

dayf_btn = tk.Button(top_frm, text = "->", command = lambda: change_day(x = 2))
dayf_btn.grid(row = 1, column = 2, sticky = "news", padx = 5, pady = 5)

yearb_btn = tk.Button(top_frm, text = "<-", command = lambda: change_year(x = 1))
yearb_btn.grid(row = 2, column = 0, sticky = "news", padx = 5, pady = 5)

year_btn = tk.OptionMenu(top_frm, year, *options2, command = lambda x: change_year())
year_btn.grid(row = 2, column = 1, sticky = "news",  padx = 5, pady = 5)

yearf_btn = tk.Button(top_frm, text = "->", command = lambda: change_year(x = 2))
yearf_btn.grid(row = 2, column = 2, sticky = "news", padx = 5, pady = 5)

back_btn = tk.Button(top_frm, text = "<--", command = lambda x = menu: back(menu))
back_btn.grid(row = 3, column = 0, columnspan = 3, sticky = "news", padx = 5, pady = 5)

mback_btn = tk.Button(mtop_frm, text = "<--", command = lambda x = menu: back(menu))
mback_btn.pack(fill = "both")

info_frm = tk.Frame(root, bg = "light grey")
info_frm.grid(row = 1, column = 0, sticky = "news")

btm_frm = tk.Frame(root, bg = "light grey")
btm_frm.grid(row = 1, column = 0, sticky = "news")

can1 = tk.Canvas(btm_frm, bg = "light grey")
scroller1 = tk.Scrollbar(btm_frm, orient = "vertical", command = can1.yview)
scroller1.pack(side = "right", fill = "y")
can1.pack(side = "left", fill = "y")
nfrm1 = tk.Frame(can1, bg = "light grey")
nfrm1.bind(lambda e: can1.configure(scrollregion = can1.bbox("all")))
nfrm1.pack()
can1.create_window((0, 0), window = nfrm1, anchor = "nw")
can1.config(yscrollcommand = scroller1.set)


holiday_check(month.get(), day.get(), year.get())


if __name__ == "__main__":
	root.mainloop()
