### Python Dates
* A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.
* Example:
```bash
import datetime

x = datetime.datetime.now()
print(x) 

"""
When we execute the code from the example above the result will be: 2022-10-01 01:29:13.620299
The date contains year, month, day, hour, minute, second, and microsecond.
"""

print(x.year)
print(x.strftime("%A"))
```

### Creating Date Objects
* To create a date, we can use the datetime() class (constructor) of the datetime module.
* The datetime() class requires three parameters to create a date: year, month, day.
```bash
import datetime

x = datetime.datetime(2020, 5, 17)

print(x) 
```
* The datetime() class also takes parameters for time and timezone (hour, minute, second, microsecond, tzone), but they are optional, and has a default value of 0, (None for timezone).
* The method is called strftime(), and takes one parameter, format, to specify the format of the returned string:
```bash
import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B")) 
```
### A reference of all the legal format codes:
<table class="ws-table-all notranslate">

<tbody>

<tr>

<th style="width:25%">Directive</th>

<th style="width:35%">Description</th>

<th style="width:30%">Example</th>

</tr>

<tr>

<td>%a</td>

<td>Weekday, short version</td>

<td>Wed</td>

</tr>

<tr>

<td>%A</td>

<td>Weekday, full version</td>

<td>Wednesday</td>

</tr>

<tr>

<td>%w</td>

<td>Weekday as a number 0-6, 0 is Sunday</td>

<td>3</td>

</tr>

<tr>

<td>%d</td>

<td>Day of month 01-31</td>

<td>31</td>

</tr>

<tr>

<td>%b</td>

<td>Month name, short version</td>

<td>Dec</td>

</tr>

<tr>

<td>%B</td>

<td>Month name, full version</td>

<td>December</td>

</tr>

<tr>

<td>%m</td>

<td>Month as a number 01-12</td>

<td>12</td>

</tr>

<tr>

<td>%y</td>

<td>Year, short version, without century</td>

<td>18</td>

</tr>

<tr>

<td>%Y</td>

<td>Year, full version</td>

<td>2018</td>

</tr>

<tr>

<td>%H</td>

<td>Hour 00-23</td>

<td>17</td>

</tr>

<tr>

<td>%I</td>

<td>Hour 00-12</td>

<td>05</td>

</tr>

<tr>

<td>%p</td>

<td>AM/PM</td>

<td>PM</td>

</tr>

<tr>

<td>%M</td>

<td>Minute 00-59</td>

<td>41</td>

</tr>

<tr>

<td>%S</td>

<td>Second 00-59</td>

<td>08</td>

</tr>

<tr>

<td>%f</td>

<td>Microsecond 000000-999999</td>

<td>548513</td>

</tr>

<tr>

<td>%z</td>

<td>UTC offset</td>

<td>+0100</td>

</tr>

<tr>

<td>%Z</td>

<td>Timezone</td>

<td>CST</td>

</tr>

<tr>

<td>%j</td>

<td>Day number of year 001-366</td>

<td>365</td>

</tr>

<tr>

<td>%U</td>

<td>Week number of year, Sunday as the first day of week, 00-53</td>

<td>52</td>

</tr>

<tr>

<td>%W</td>

<td>Week number of year, Monday as the first day of week, 00-53</td>

<td>52</td>

</tr>

<tr>

<td>%c</td>

<td>Local version of date and time</td>

<td>Mon Dec 31 17:41:00 2018</td>

</tr>

<tr>

<td>%C</td>

<td>Century</td>

<td>20</td>

</tr>

<tr>

<td>%x</td>

<td>Local version of date</td>

<td>12/31/18</td>

</tr>

<tr>

<td>%X</td>

<td>Local version of time</td>

<td>17:41:00</td>

</tr>

<tr>

<td>%%</td>

<td>A % character</td>

<td>%</td>

</tr>

<tr>

<td>%G</td>

<td>ISO 8601 year</td>

<td>2018</td>

</tr>

<tr>

<td>%u</td>

<td>ISO 8601 weekday (1-7)</td>

<td>1</td>

</tr>

<tr>

<td>%V</td>

<td>ISO 8601 weeknumber (01-53)</td>

<td>01</td>

</tr>

</tbody>

</table>

### Important resources
* [Python date-time](https://www.w3schools.com/python/python_datetime.asp)