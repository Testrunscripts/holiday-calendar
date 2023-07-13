
import datetime as dt

import julian as jul


def check_holidays(month, day, year):
	work = []
	for holiday in holidays:
		if month == holidays[holiday][0]:
			if day == holidays[holiday][1]:
				work.append(holiday)
	if month == "January":
		try:
			for item in check_january(day, year):
				work.append(item)
		except:
			pass
	if month == "February":
		try:
			for item in check_february(day, year):
				work.append(item)
		except:
			pass
	if month == "March":
		try:
			for item in check_march(day, year):
				work.append(item)
		except:
			pass
	if month == "April":
		try:
			for item in check_april(day, year):
				work.append(item)
		except:
			pass
	if month == "May":
		try:
			for item in check_may(day, year):
				work.append(item)
		except:
			pass
	if month == "June":
		try:
			for item in check_june(day, year):
				work.append(item)
		except:
			pass
	if month == "July":
		try:
			for item in check_july(day, year):
				work.append(item)
		except:
			pass
	if month == "August":
		try:
			for item in check_august(day, year):
				work.append(item)
		except:
			pass
	if month == "September":
		try:
			for item in check_september(day, year):
				work.append(item)
		except:
			pass
	if month == "October":
		try:
			for item in check_october(day, year):
				work.append(item)
		except:
			pass
	if month == "November":
		try:
			for item in check_november(day, year):
				work.append(item)
		except:
			pass
	if month == "December":
		try:
			for item in check_december(day, year):
				work.append(item)
		except:
			pass
	try:
		x = jul.julian_check(year, month, day)
		for item in x:
			work.append(item)
	except Exception as e:
		print(e)
	for i in work:
		pass
	return work
	
def check_january(day, year):
	work = []
	d = dt.date(int(year), 1, 1).weekday()
	if d == 0:
		first_monday = d
	else:
		first_monday = 8 - d
	if int(day) == first_monday:
		work.append("Handsel Monday")
	if d == 0:
		third_monday = 15
	else:
		third_monday = 22 - d
	if int(day) == third_monday:
		work.append("Martin Luther King Jr. Day")
	return work
	
def check_february(day, year):
	work = []
	d = dt.date(int(year), 2, 1).weekday()
	if d == 0:
		third_monday = 15
	else:
		third_monday = 22 - d
	if int(day) == third_monday:
		work.append("Presidents' Day (United States)")
	return work
	
def check_march(day, year):
	work = []
	d = dt.date(int(year), 3, 1).weekday()
	if d == 0:
		second_monday = 8
	else:
		second_monday = 15 - d
	if int(day) == second_monday:
		work.append("Commonwealth Day")
	if d <= 2:
		second_wednesday = 10 - d
	else:
		second_wednesday = 17 - d
	if int(day) == second_wednesday:
		work.append("Decoration Day (Liberia)")
	return work
	
def check_april(day, year):
	work = []
	d = dt.date(int(year), 4, 1).weekday()
	if d <= 4:
		second_friday = 12 - d
	else:
		second_friday = 19 - d
	if int(day) == second_friday:
		work.append("Fast and Prayer Day")
	return work
	
def check_may(day, year):
	work = []
	d = dt.date(int(year), 5, 1).weekday()
	if d == 0:
		first_monday = d
	else:
		first_monday = 8 - d
	if int(day) == first_monday:
		pass
	if d == 0:
		second_monday = 8
	else:
		second_monday = 15 - d
	if int(day) == second_monday:
		work.append("Gospel Day (Tuvalu)")
	if d >= 6:
		last_monday = 37 - d
	else:
		last_monday = 29 - d
	if int(day) == last_monday:
		work.append("Memorial Day")
	return work
	
def check_june(day, year):
	work = []
	d = dt.date(int(year), 6, 1).weekday()
	if d >= 4:
		last_saturday = 34 - d
	else:
		last_saturday = 27 - d
	if int(day) == last_saturday:
		pass
	return work
	
def check_july(day, year):
	work = []
	d = dt.date(int(year), 7, 1).weekday()
	if d == 0:
		first_monday = d
	else:
		first_monday = 8 - d
	if int(day) == first_monday:
		work.append("Heroes' Day (Zambia)")
	if d <= 4:
		first_friday = 5 - d
	else:
		first_friday = 12 - d
	if int(day) == first_friday:
		work.append("Fishermen's Day")
	if d < 1:
		following_tuesday = d
	elif d == 1:
		following_tuesday = 8
	else:
		folkowing_tuesday = 9 - d
	if int(day) == following_tuesday:
		work.append("Unity Day (Zambia)")
	if d == 6:
		fourth_sunday = 22
	else:
		fourth_sunday = 28 - d
	if int(day) == fourth_sunday:
		work.append("Parents' Day (United States)")
	return work
	
def check_august(day, year):
	work = []
	d = dt.date(int(year), 8, 1).weekday()
	if d == 0:
		first_monday = d
	else:
		first_monday = 8 - d
	if int(day) == first_monday:
		work.append("August Monday")
		work.append("Emancipation Day (The Bahamas)")
		work.append("Emancipation Day (Dominica)")
		work.append("Farmers' Day (Zambia)")
		work.append("Kadooment Day")
		work.append("National Children's Day (Tuvalu)")
	if d < 1:
		august_tuesday = d
	elif d == 1:
		august_tuesday = 8
	else:
		august_tuesday = 9 - d
	if int(day) == august_tuesday:
		work.append("August Tuesday")
	if d <= 4:
		first_friday = 5 - d
	else:
		first_friday = 12 - d
	if int(day) == first_friday:
		work.append("Umuganura Day")
	if d == 0:
		second_monday = 8
	else:
		second_monday = 15 - d
	if int(day) == second_monday:
		work.append("Heroes' Day (Zimbabwe)")
	if d < 1:
		following2_tuesday = d
	elif d == 0:
		following2_tuesday = 9
	else:
		following2_tuesday = 16 - d
	if int(day) == following2_tuesday:
		work.append("Defence Forces Day (Zimbabwe)")
	return work
	
def check_september(day, year):
	work = []
	d = dt.date(int(year), 9, 1).weekday()
	if d == 0:
		first_monday = d
	else:
		first_monday = 8 - d
	if int(day) == first_monday:
		work.append("Labor Day (United States)")
	if d <= 4:
		first_friday = 5 - d
	else:
		first_friday = 12 - d
	if int(day) == first_friday:
		work.append("Labor Day (Marshall Islands)")
	if d <= 2:
		last_friday = 26 - d
	else:
		last_friday = 33 - d
	if int(day) == last_friday:
		work.append("Manit Day")
	return work
	
def check_october(day, year):
	work = []
	d = dt.date(int(year), 10, 1).weekday()
	if d == 0:
		first_monday = d
	else:
		first_monday = 8 - d
	if int(day) == first_monday:
		work.append("Thanksgiving (Saint Lucia)")
	if d == 0:
		second_monday = 8
	else:
		second_monday = 15 - d
	if int(day) == second_monday:
		work.append("Columbus Day (United States)")
		work.append("National Heroes' Day (The Bahamas)")
	return work

def check_november(day, year):
	work = []
	d = dt.date(int(year), 11, 1).weekday()
	if d == 0:
		first_monday = d
	else:
		first_monday = 8 - d
	if int(day) == first_monday:
		work.append("Columbus Day (Italy)")
	if d <= 3:
		first_thursday = 4 - d
	else:
		first_thursday = 11 - d
	if int(day) == first_thursday:
		work.append("Thanksgiving (Liberia)")
	if d <= 3:
		fourth_thursday = 25 - d
	else:
		fourth_thursday = 22 - (d - 3)
	if int(day) == fourth_thursday:
		work.append("Thanksgiving (United States)")
	if d < 4:
		black_friday = 26 - d
	elif d == 4:
		black_friday = 30
	else:
		black_friday = 23 - (d - 4)
	if d <= 4:
		fourth_friday = 26 - d
	else:
		fourth_friday = 33 - d
	if int(day) == fourth_friday:
		work.append("Family Day (Palau)")
	if int(day) == black_friday:
		work.append("Black Friday")
	return work
	
def check_december(day, year):
	work = []
	d = dt.date(int(year), 7, 1).weekday()
	if d <= 4:
		first_friday = 5 - d
	else:
		first_friday = 12 - d
	if int(day) == first_friday:
		work.append("Gospel Day")
	return work
	
	
holidays = {
"1994 Genocide Against the Tutsi Commemoration Day" : ["April", "7"],
"Adwa Victory Day" : ["March", "2"],
"Afghan Independence Day" : ["August", "19"],
"Africa Day" : ["May", "25"],
"Afro-Colombian Day" : ["May", "21"],
"Agrarian Reform Day" : ["August", "2"],
"Air Force Day" : ["February", "1"],
"All Saints' Day (Western Christianity)" : ["November", "1"],
"All Souls' Day" : ["November", "2"],
"Americas Day" : ["April", "14"],
"Angam Day" : ["October", "26"],
"Anzac Day" : ["April", "25"],
"Argentina Independence Day" : ["July", "9"],
"Armed Forces Day (Benin)" : ["October", "26"],
"Armed Forces Day (Liberia)" : ["February", "11"],
"Armed Forces Day (Mali)" : ["January", "20"],
"Armed Forces Day (Mozambique)" : ["September", "25"],
"Armed Forces Day (Sierra Leone)" : ["February", "18"],
"Army Abolition Day" : ["December", "1"],
"Army Day (Democratic Republic of the Congo)" : ["November", "17"],
"Army Day (Guatemala)" : ["June", "30"],
"Army Day (Honduras)" : ["October", "21"],
"Army Day (Nicaragua)" : ["May", "27"],
"Assumption of Mary" : ["August", "15"],
"Baba Marta Day" : ["March", "1"],
"Barthelemy Boganda Day" : ["March", "29"],
"Battle of Boyaca" : ["August", "7"],
"Battle of Las Piedras Day" : ["May", "18"],
"Belgian National Day" : ["July", "21"],
"Birthday of Jose Gervasio Artigas" : ["June", "19"],
"Birthday of Kenneth Kaunda" : ["April", "28"],
"Boxing Day" : ["December", "26"],
"Bulgarian Armed Forces Day" : ["May", "6"],
"Canada Day" : ["July", "1"],
"Cassinga Day" : ["May", "4"],
"Celebration of the Greek Revolution" : ["March", "25"],
"Cheikh Al Maarouf Day" : ["March", "18"],
"Children's Day (Uruguay)" : ["January", "6"],
"Children's Day (Vanuatu)" : ["July", "24"],
"Christmas" : ["December", "25"],
"Christmas Eve" : ["December", "24"],
"Commemoration of the Victory over Kadhafi" : ["March", "19"],
"Community Service Day" : ["November", "4"],
"Constitution Day (Marshall Islands)" : ["May", "1"],
"Constitution Day (Nauru)" : ["May", "17"],
"Constitution Day (Norway)" : ["May", "17"],
"Constitution Day (Palau)" : ["July", "9"],
"Constitution Day (Seychelles)" : ["June", "18"],
"Constitution Day (Uruguay)" : ["July", "18"],
"Constitution Day (Vanuatu)" : ["October", "5"],
"Culturama Day" : ["August", "2"],
"Crab Soup Day" : ["August", "27"],
"Cry of Dolores" : ["September 16"],
"Custom Chief's Day" : ["March", "5"],
"Cyprien Ntaryamira Day" : ["April", "6"],
"Day of Peace and Reconciliation" : ["October", "4"],
"Day of Restoration of Independence (Azerbaijan)" : ["October", "18"],
"Day of Restoration of Independence (Estonia)" : ["August", "20"],
"Day of Restoration of Independence of Lithuania" : ["March", "11"],
"Day of Restoration of the State of Lithuania" : ["February", "16"],
"Day of Svetitskhoveli Cathedral" : ["October", "14"],
"Day of the Constitution of the Slovak Republic" : ["September", "1"],
"Day of the Establishment of the Slovak Republic" : ["January", "1"],
"Day of the Family (Uruguay)" : ["December", "25"],
"Day of the Glories of the Army" : ["September", "19"],
"Day of the Holy Brothers Cyril and and Methodius, of the Bulgarian Alphabet, Education and Culture and of the Slavonic Literature" : ["May", "24"],
"Day of the Restoration of Latvian Independence" : ["May", "4"],
"Day of Unity of Ukraine" : ["January", "21"],
"Declaration of Independence (Colombia)" : ["July", "20"],
"Democracy Day (Cape Verde)" : ["January", "13"],
"Dia del Nino (Costa Rica)" : ["September", "9"],
"Dormition of the Mother of God" : ["August", "15"],
"Emancipation Day (Barbados)" : ["August", "1"],
"Emancipation Day (Tonga)" : ["June", "4"],
"Epiphany" : ["January", "6"],
"Errol Barrow Day" : ["January", "21"],
"Ethiopian Christmas" : ["January", "7"],
"Evacuation Day (Syria)" : ["April", "17"],
"Evacuation Day (Tunisia)" : ["October", "15"],
"Family Day (Mozambique)" : ["December", "25"],
"Family Day (Vanuatu)" : ["December", "26"],
"Father Lini Day" : ["February", "21"],
"Feast of Our Lady of the Angels" : ["August", "2"],
"February 17 Revolution Day" : ["February", "17"],
"Fete du Vodoun" : ["January", "10"],
"Freedom and Democracy Day" : ["December", "1"],
"Fiji Day" : ["October", "10"],
"Flag Day (Liberia)" : ["August", "24"],
"Francisco Morazan's Day" : ["October", "3"],
"Freedom Day" : ["April", "25"],
"General Prayer Day" : ["June", "30"],
"German Unity Day" : ["October", "3"],
"Global Day of Parents" : ["June", "1"],
"Green March" : ["November", "6"],
"Guanacaste Day" : ["July", "25"],
"Halloween" : ["October", "31"],
"Heroes Day (Cape Verde)" : ["January", "20"],
"Heroes Day (Guinea-Bissau)" : ["January", "20"],
"Heroes' Day (Mozambique)" : ["February", "3"],
"Heroes' Day (Namibia)" : ["August", "26"],
"Heroes' Day (Paraguay)" : ["March", "1"],
"Human Rights Day" : ["December", "10"],
"Independence and Unity Day" : ["December", "26"],
"Independence Day (Albania)" : ["November", "28"],
"Independence Day (Algeria)" : ["July", "5"],
"Independence Day (Angola)" : ["November", "11"],
"Independence Day (Antigua and Barbuda)" : ["November", "1"],
"Independence Day (Armenia)" : ["September", "21"],
"Independence Day (Azerbaijan)" : ["May", "28"],
"Independence Day (Bahrain)" : ["August", "15"],
"Independence Day (Bangladesh)" : ["March", "26"],
"Independence Day (Barbados)" : ["November", "30"],
"Independence Day (Belarus)" : ["July", "3"],
"Independence Day (Belize)" : ["September", "21"],
"Independence Day (Benin)" : ["August", "1"],
"Independence Day (Bolivia)" : ["August", "6"],
"Independence Day (Bosnia and Herzegovina)" : ["March", "1"],
"Independence Day (Botswana)" : ["September", "30"],
"Independence Day (Brazil)" : ["September", "7"],
"Independence Day (Bulgaria)" : ["September", "22"],
"Independence Day (Burkina Faso)" : ["August", "5"],
"Independence Day (Burundi)" : ["July", "1"],
"Independence Day (Cambodia)" : ["November", "9"],
"Independence Day (Cape Verde)" : ["July", "5"],
"Independence Day (Central African Republic)" : ["August", "13"],
"Independence Day (Chad)" : ["August", "11"],
"Independence Day (Chile)" : ["September", "18"],
"Independence Day (Costa Rica)" : ["September", "15"],
"Independence Day (Cuba)" : ["October", "10"],
"Independence Day (Cyprus)" : ["October", "1"],
"Independence Day (Czech Republic)" : ["October",  "28"],
"Independence Day (Democratic Republic of the Congo)" : ["June", "30"],
"Independence Day (Djibouti)" : ["June", "27"],
"Independence Day (Dominica)" : ["November", "3"],
"Independence Day (Dominican Republic)" : ["February", "27"],
"Independence Day (Ecuador)" : ["May", "24"],
"Independence Day (El Salvador)" : ["September", "15"],
"Independence Day (Equatorial Guinea)" : ["October", "12"],
"Independence Day (Eritrea)" : ["May", "24"],
"Independence Day (Estonia)" : ["February", "24"],
"Independence Day (Finland)" : ["December", "6"],
"Independence Day (Gabon)" : ["August", "17"],
"Independence Day (Georgia)" : ["May", "26"],
"Independence Day (Ghana)" : ["March", "6"],
"Independence Day (Grenada)" : ["February", "7"],
"Independence Day (Guatemala)" : ["September", "15"],
"Independence Day (Guinea)" : ["October", "2"],
"Independence Day (Guyana)" : ["May", "26"],
"Independence Day (Haiti)" : ["January", "1"],
"Independence Day (Honduras)" : ["September", "15"],
"Independence Day (India)" : ["August", "15"],
"Independence Day (Indonesia)" : ["August", "17"],
"Independence Day (Iraq)" : ["October", "3"],
"Independence Day (Ivory Coast)" : ["August", "7",],
"Independence Day (Jamaica)" : ["August", "6"],
"Independence Day (Jordan)" : ["May", "25"],
"Independence Day (Kazakhstan)" : (
"December", "16"),
"Independence Day (Kiribati)" : ["July", "12"],
"Independence Day (Kyrgyzstan)" : ["August", "31"],
"Independence Day (Lesotho)" : ["October", "4"],
"Independence Day (Liberia)" : ["July", "26"],
"Independence Day (Libya)" : ["December", "24"],
"Idependence Day (Madagascar)" : ["June", "26"],
"Independence Day (Malawi)" : ["July", "6"],
"Independence Day (Malaysia)" : ["August", "31"],
"Independence Day (Maldives)" : ["July", "26"],
"Independence Day (Mali)" : ["September", "22"],
"Independence Day (Malta)" : ["September", "21"],
"Independence Day (Mauritania)" : ["November", "28"],
"Independence Day (Mauritius)" : ["March 12"],
"Independence Day (Moldova)" : ["August", "27"],
"Independence Day (Mongolia)" : ["December", "29"],
"Independence Day (Montenegro)" : ["May", "21"],
"Independence Day (Mozambique)" : ["June", "25"],
"Independence Day (Myanmar)" : ["January", "4"],
"Independence Day (Namibia)" : ["March", "21"],
"Independence Day (Nauru)" : ["January", "31"],
"Independence Day (Niger)" : ["August", "3"],
"Independence Day (Nigeria)" : ["October", "1"],
"Independence Day (North Macedonia)" : ["September", "8"],
"Independence Day (Pakistan)" : ["August", "14"],
"Independence Day (Palau)" : ["October", "1"],
"Independence Day (Panama)" : ["November", "28"],
"Independence Day (Papua New Guinea)" : ["September", "16"],
"Independence Day (Peru)" : ["July", "28"],
"Independence Day (Philippines)" : ["June", "12"],
"Independence Day (Rwanda)" : ["July", "1"],
"Independence Day (Saint Kitts and Nevis)" : ["September", "19"],
"Independence Day (Saint Lucia)" : ["February", "22"],
"Independence Day (Saint Vincent and the Grenadines)" : ["October", "27"],
"Independence Day (Samoa)" : ["June", "1"],
"Independence Day (Sao Tome and Principe)" : ["July", "12"],
"Independence Day (Senegal)" : ["April", "4"],
"Independence Day (Sierra Leone)" : ["April", "27"],
"Independence Day (Solomon Islands)" : ["June", "7"],
"Independence Day (Somalia)" : ["July", "1"],
"Independence Day (Somaliland)" : ["May", "18"],
"Independence Day (South Sudan)" : ["July", "9"],
"Independence Day (Sri Lanka)" : ["February", "4"],
"Independence Day (Sudan)" : ["January", "1"],
"Independence Day (Suriname)" : ["November", "25"],
"Independence Day (Tajikistan)" : ["September", "9"],
"Independence Day (Tanzania)" : ["December", "9"],
"Independence Day (Togo)" : ["April", "27"],
"Independence Day (The Bahamas)" : ["July", "10"],
"Independence Day (The Gambia)" : ["February", "18"],
"Independence Day (Trinidad and Tobago)" : ["August", "31"],
"Independence Day (Tunisia)" : ["March", "20"],
"Independence Day (Turkmenistan)" : ["September", "27"],
"Independence Day (Uganda)" : ["October", "9"],
"Independence Day (United States)" : ["July", "4"],
"Independence Day (Uruguay)" : ["August", "25"],
"Independence Day (Uzbekistan)" : ["September", "1"],
"Independence Day (Vanuatu)" : ["July", "30"],
"Independence Day (Vatican City)" : ["February", "11"],
"Independence Day (Venezuela)" : ["July", "5"],
"Independence Day (Yemen)" : ["November", "30"],
"Independence Day (Zambia)" : ["October", "24"],
"Independence Dau (Zimbabwe)" : ["April", "18"],
"Independence Day of Ukraine" : ["August", "24"],
"Indian Arrival Day (Trinidad and Tobago)" : ["May", "30"],
"Indigenous Resistance Day" : ["October", "12"],
"International Women's Day" : ["March", "8"],
"International Workers' Day" : ["May", "1"],
"International Youth Day" : ["August", "12"],
"Jamhuri Day" : ["December", "12"],
"J. J. Roberts' Birthday" : ["March", "15"],
"John Chilembe Day" : ["January", "15"],
"Juan Santamaria Day" : ["April", "11"],
"Juneteenth" : ["June", "19"],
"Karume Day" : ["April", "7"],
"Landing of the 33 Patriots Day" : ["April", "19"],
"Laurent-Desire Kabila Assassination" : ["January", "16"],
"Lebanese Independence Day" : ["November", "22"],
"Liberation Day (Albania)" : ["November", "29"],
"Liberation Day (Bulgaria)" : ["March", "3"],
"Liberation Day (Cuba)" : ["January", "1"],
"Liberation Day (Democratic Republic of the Congo)" : ["May", "17"],
"Liberation Day (Kuwait)" : ["February", "26"],
"Liberation Day (Libya)" : ["October", "23"],
"Liberation Day (Nicaragua)" : ["July", "19"],
"Liberation Day (Rwanda)" : ["July", "4"],
"Liberation Day (Togo)" : ["January", "13"],
"Liberation Day (Yemen)" : ["October", "14"],
"Madeira Day" : ["July", "1"],
"Majority Rule Day" : ["January", "10"],
"Malaysia Day" : ["September", "16"],
"Maore Day" : ["November", "12"],
"March 1 Movement" : ["March", "1"],
"Martyrs' Day (Burkina Faso)" : ["October", "31"],
"Martyrs Day (Democratic Republic of the Congo)" : ["January", "4"],
"Martyrs' Day (Libya)" : ["September", "16"],
"Martyrs' Day (Madagascar)" : ["March", "29"],
"Martyrs' Day (Malawi)" : ["March", "3"],
"Martyrs' Day (Mali)" : ["March", "26"],
"Martyrs' Day (Panama)" : ["January", "9"],
"Martyrs' Day (South Sudan)" : ["July", "30"],
"Martyrs' Day (Togo)" : ["June", "21"],
"Martyrs' Day (Tunisia)" : ["April", "9"],
"May Day" : ["May", "1"],
"May Eve" : ["April", "30"],
"Moshoeshoe's Day" : ["March", "11"],
"Nane Nane Day" : ["August", "8"],
"National Awakening Day (Bulgaria)" : ["November", "1"],
"National Day (Benin)" : ["November", "30"],
"National Day (Bhutan)" : ["December", "17"],
"National Day (Brunei)" : ["February", "23"],
"National Day (Cameroon)" : ["May", "20"],
"National Day (Central African Republic)" : ["December", "1"],
"National Day (Comoros)" : ["July", "6"],
"National Day (Guinea-Bissau)" : ["September", "24"],
"National Day (Iceland)" : ["June", "17"],
"National Day (Kuwait)" : ["February", "25"],
"National Day (Liechtenstein)" : ["August", "15"],
"National Day (Palestine)" : ["November", "15"],
"National Day (Qatar)" : ["December", "18"],
"National Day (Republic of the Congo)" : ["August", "15"],
"National Day (Saint Lucia)" : ["December", "13"],
"National Day (Seychelles)" : ["June", "29"],
"National Day (Singapore)" : ["August", "9"],
"National Day (United Arab Emirates)" : ["December", "2"],
"National Day (Vietnam)" : ["September", "2"],
"National Day of Oman" : ["November", "18"],
"National Day of Sweden" : ["June", "6"],
"National Foundation Day" : ["February", "11"],
"National Heroes Day (Antigua and Barbuda)" : ["December", "9"],
"National Heroes' Day (Barbados)" : ["April", "28"],
"National Heroes Day (Rwanda)" : ["February", "1"],
"National Heroes Day (Saint Kitts and Nevis)" : ["September", "16"],
"National Heroes' Day (Saint Vincent and the Grenadines)" : ["March", "14"],
"National Independence Day (Poland)" : ["November", "11"],
"National Liberation Day of Korea" : ["August", "15"],
"National Parks Day (Costa Rica)" : ["August", "24"],
"National Unification Day" : ["May", "14"],
"National Unity Day (Georgia)" : ["April", "9"],
"National Unity Day (Vanuatu)" : ["November", "29"],
"National Unity Day (Zimbabwe)" : ["December", "22"],
"National Women's Day (Tunisia)" : ["August", "13"],
"National Youth Day (Nauru)" : ["September", "25"],
"National Youth Day. (Zimbabwe)" : ["February", "21"],
"Nativity of John the Baptist" : ["June", "24"],
"Ndadaye Day" : ["October", "21"],
"New Year's Day" : ["January", "1"],
"New Year's Eve" : ["December", "31"],
"Nyerere Day" : ["October", "14"],
"Oak Apple Day" : ["May", "29"],
"Oued Ed-Dahab Day" : ["August", "14"],
"Parents' Day (Democratic Republic of the Congo)" : ["August", "1"],
"Parents' Day (South Korea)" : ["May", "8"],
"Patrice Lumumba Assassination" : ["January", "17"],
"Pidjiguiti Day" : ["August", "3"],
"Plurinational State of Bolivia Anniversary" : ["January", "22"],
"Portugal Day" : ["June", "10"],
"President Kamuzu Banda's Birthday" : ["May", "14"],
"Presidents' Day (Marshall Islands)" : ["November", "17"],
"President's Day (Palau)" : ["June", "1"],
"Proclamation Day of the Republic of Latvia" : ["November", "18"],
"Proclamation of Independence Day (Burkina Faso)" : ["December", "11"],
"Proclamation of Independence Day (East Timor)" : ["November", "28"],
"Proclamation of Independence Day (Morocco)" : ["January", "11"],
"Readjustment Movement Day" : ["November", "14"],
"Reconciliation Day (Republic of the Congo)" : ["June", "10"],
"Remembrance Day (Marshall Islands)" : ["March", "1"],
"Repentance Day" : ["August", "26"],
"Republic Day (Armenia)" : ["May", "28"],
"Republic Day (Chad)" : ["November", "28"],
"Republic Day (Maldives)" : ["November", "11"],
"Republic Day (Philippines)" : ["July", "4"],
"Republic Day (Portugal)" : ["October", "5"],
"Republic Day (Republic of the Congo)" : ["November", "28"],
"Republic Day (Trinidad and Tobago)" : ["September", "24"],
"Republic Day (Tunisia)" : ["July", "25"],
"Restoration Day" : ["January", "1"],
"Restoration of Independence Day" : ["December", "1"],
"Retrocession Day" : ["October", "25"],
"Revolution Day (Burkina Faso)" : ["January", "3"],
"Revolution Day (Egypt)" : ["July", "23"],
"Revolution Day (Guatemala)" : ["October", "20"],
"Revolution Day (Morocco)" : ["August", "20"],
"Revolution Day (Yemen)" : ["September", "26"],
"Revolution Day (The Gambia)" : ["July", "22"],
"Revolution Day (Tunisia)" : ["December", "17"],
"Revolution of the King and the People Day" : ["August", "20"],
"Rwagasore Day" : ["October", "13"],
"Saba Saba Day" : ["July", "7"],
"Senior Citizens Day" : ["May", "5"],
"Separation Day" : ["November", "3"],
"Slovak National Uprising Anniversary" : ["August", "29"],
"Spiritual Baptist/Shouter Liberation Day" : ["March", "30"],
"SPLA Day" : ["May", "16"],
"Statehood Day (Croatia)" : ["May", "30"],
"Statehood Day (Lithuania)" : ["July", "6"],
"Statehood Day (Serbia)" : ["February", "15"],
"Statehood Day (Slovenia)" : ["June", "25"],
"State Independence Day of Romania" : ["May", "9"],
"St. George's Caye Day" : ["September", "10"],
"Struggle for Freedom and Democracy Day" : ["November", "17"],
"Swiss National Day" : ["August", "1"],
"Tuvalu Day" : ["October", "1"],
"Unification Day (Bulgaria)" : ["September", "6"],
"Union Day" : ["April", "26"],
"Union Dissolution Day" : ["June", "7"],
"United Nations Day" : ["October", "24"],
"Unity Day (Burundi)" : ["February", "5"],
"Unity Day (Yemen)" : ["May", "22"],
"Valentine's Day (Western Christian)" : ["February", "14"],
"Veterans Day (United States)" : ["November", "11"],
"Victory Day (9 May)" : ["May", "9"],
"Victory Day (Bangladesh)" : ["December 16"],
"Victory Day (Cuba)" : ["January", "2"],
"Victory Day (Maldives)" : ["November", "3"],
"Victory Day (Mozambique)" : ["September", "7"],
"Victory in Europe Day" : ["May", "8"],
"William V. S. Tubman's Birthday" : ["November", "29"],
"Women's Day (Gabon)" : ["April", "17"],
"Women's Day (Mozambique)" : ["April", "7"],
"Youth Day (Cape Verde)" : ["June", "1"],
"Youth Day (Palau)" : ["March", "15"],
"Youth Day (Zambia)" : ["March", "12"],
"Zanzibar Revolution Day" : ["January", "12"],
}
		