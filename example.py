from pyluach import dates, hebrewcal, parshios

today = dates.HebrewDate.today()
lastweek_gregorian = (today - 7).to_greg()
lastweek_gregorian < today
True
today - lastweek_gregorian
7
greg = dates.GregorianDate(1986, 3, 21)
heb = dates.HebrewDate(5746, 13, 10)
greg == heb
True

purim = dates.HebrewDate(5781, 12, 14)
purim.hebrew_day()
'י״ד'
purim.hebrew_date_string()
'י״ד אדר תשפ״א'
purim.hebrew_date_string(True)
'י״ד אדר ה׳תשפ״א'

rosh_hashana = dates.HebrewDate(5782, 7, 1)
rosh_hashana.holiday()
'Rosh Hashana'
rosh_hashana.holiday(hebrew=True)
'ראש השנה'
(rosh_hashana + 3).holiday()
None

month = hebrewcal.Month(5781, 10)
month.month_name()
'Teves'
month.month_name(True)
'טבת'
month + 3
Month(5781, 1)
for month in hebrewcal.Year(5774).itermonths():
    print(month.month_name())
Tishrei, Cheshvan, Kislev, Teves, Shevat, Adar, Adar_I, Nisan, Iyar, Sivan, Tammuz, Av, Elul

date = dates.GregorianDate(2010, 10, 6)
parshios.getparsha(date)
[0]
parshios.getparsha_string(date, israel=True)
'Beraishis'
parshios.getparsha_string(date, hebrew=True)
'בראשית'
new_date = dates.GregorianDate(2021, 3, 10)
parshios.getparsha_string(new_date)
'Vayakhel, Pekudei'
parshios.getparsha_string(new_date, hebrew=True)
'ויקהל, פקודי'



from pyluach import dates, parshios
date = dates.HebrewDate(5781, 10, 5)
parshios.getparsha(date)
'Vayigash'
parshios.getparsha_string(date, hebrew=True)
'ויגש'
parshios.getparsha_string(dates.GregorianDate(2021, 3, 7), hebrew=True)
'ויקהל, פקודי'

