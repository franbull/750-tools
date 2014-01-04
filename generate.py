import os
import calendar
from datetime import datetime
from datetime import timedelta
import re

def change_day_for_x(cal_table, day):
    pat = '(<td class="\S+">)(%s)(</td>)' % day
    def repl(m):
        return m.group(1) + 'x' + m.group(3)
    print re.findall(pat, cal_table)
    cal_table = re.sub(pat, repl, cal_table)
    return cal_table

def make_calendar(dates):
    cal = calendar.HTMLCalendar(6)
    tables = []
    cur_month = None
    cal_table = None
    for date in dates:
        if date.month != cur_month:
            if cal_table is not None:
                tables.append(cal_table)
            cal_table = cal.formatmonth(date.year, date.month)
            cur_month = date.month
        cal_table = change_day_for_x(cal_table, date.day)
    tables.append(cal_table)
    return tables

def get_data():
    dates = []
    for root, dirs, files in os.walk('..'):
        for fp in files:
            dates.append(datetime.fromtimestamp(os.stat(os.path.join('..', fp)).st_mtime))
        # don't actually want to walk into directories
        break
    # the server is 8 hours ahead, hack around
    td = timedelta(hours=8)
    new_dates = sorted([d - td for d in dates])
    return new_dates

def write_content(content):
    html = open('html.template', 'r').read()
    html = html % {'content': content}
    open('index.html', 'w').write(html)

if __name__ == '__main__':
    write_content('\n'.join(make_calendar(get_data())))
