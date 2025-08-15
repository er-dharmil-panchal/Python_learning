import time
time1=time.strftime("7(%a)--8(%A)--9(%b)--10(%B)--11(%c)--12(%d)--14(%H)--15(%I)--16(%j)--17(%m)\n18(%M)--19(%p)--20(%S)--21(%U)--22(%w)--23(%W)--24(%x)--25(%X)--26(%y)--27(%Y)--28(%z)\n29(%Z)--30(%%)")
print(time1)


'''
%a      Locale's abbreviated weekday name.
%A      Locale's full weekday name.
%b      Locale's abbreviated month name.
%B      Locale's full month name.
%c      Locale's appropriate date and time representation.
%d      Day of the month as a decimal number [01,31].
%f      Microseconds as a decimal number        [000000,999999].
%H      Hour (24-hour clock) as a decimal number [00,23].
%I      Hour (12-hour clock) as a decimal number [01,12].
%j      Day of the year as a decimal number [001,366].
%m      Month as a decimal number [01,12].
%M      Minute as a decimal number [00,59].
%p      Locale's equivalent of either AM or PM.
%S      Second as a decimal number [00,61].
%U      Week number of the year (Sunday as the first day of the week) as a decimal number [00,53]. All days in a new year preceding the first Sunday are considered to be in week 0.
%w      Weekday as a decimal number [0(Sunday),6(saturday)].
%W      Week number of the year (Monday as the first day of the week) as a decimal number [00,53]. All days in a new year preceding the first Monday are considered to be in week 0.
%x      Locale's appropriate date representation.
%X      Locale's appropriate time representation.
%y      Year without century as a decimal number [00,99].
%Y      Year with century as a decimal number.
%z      Time zone offset indicating a positive or negative time difference from UTC/GMT of the form +HHMM or -HHMM, where H represents decimal hour digits and M represents decimal minute digits [-23:59, +23:59]. [1]
%Z      Time zone name (no characters if no time zone exists). Deprecated. [1]
%%      A literal '%' character.

'''



#NOTE  https://docs.python.org/3/library/time.html#time.strftime
