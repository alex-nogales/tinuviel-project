'''
Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.
'''

s = '12:00:00AM'
def time_conversion(s):
    s_splitted = s.split(':')

    if 'PM' in s_splitted[-1]:
        if s_splitted[0] == '12':
            return s_splitted[0] + ':' + s_splitted[1] + ':' + s_splitted[2][:2]
        else:
            return str(int(s_splitted[0]) + 12) + ':' + s_splitted[1] + ':' + s_splitted[2][:2]
    else:
        if s_splitted[0] == '12':
            return '00:' + s_splitted[1] + ':' + s_splitted[2][:2]
        else:
            return s_splitted[0] + ':' + s_splitted[1] + ':' + s_splitted[2][:2]


if __name__ == '__main__':
    print(time_conversion(s))