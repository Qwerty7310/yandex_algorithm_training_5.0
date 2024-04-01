days_of_week = {
    "Monday":       0,
    "Tuesday":      1,
    "Wednesday":    2,
    "Thursday":     3,
    "Friday":       4,
    "Saturday":     5,
    "Sunday":       6
}

month_of_year = {
    "January":      0,
    "February":     1,
    "March":        2,
    "April":        3,
    "May":          4,
    "June":         5,
    "July":         6,
    "August":       7,
    "September":    8,
    "October":      9,
    "November":     10,
    "December":     11
}


def get_day_of_week(cur_year, first_day_of_week, cur_month, cur_day):
    # print(cur_year, first_day_of_week, cur_month, cur_day)
    days_arr = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (cur_year % 400 == 0) or ((cur_year % 4 == 0) and (cur_year % 100 != 0)):
        days_arr[1] = 29
    num = cur_day
    for i in range(cur_month):
        num += days_arr[i]
    # print(((num - 1) % 7 + first_day_of_week) % 7)
    return ((num - 1) % 7 + first_day_of_week) % 7


def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k


# print()
# print(get_day_of_week(1900, 0, 2, 1))
# print()

n = int(input())
year = int(input())
holidays = [[0]*2 for i in range(n)]
for i in range(n):
    a, b = map(str, input().split())
    # print("a =", a, "b =", b)
    holidays[i][0] = int(a)
    holidays[i][1] = month_of_year[b]
first_day = days_of_week[str(input())]

number_of_holiday = [0] * 7
for i in range(n):
    number_of_holiday[get_day_of_week(year, first_day, holidays[i][1], holidays[i][0])] += 1

days = [52]*7
days[first_day] += 1
if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    days[(first_day+1) % 7] += 1

res = [0]*7
for i in range(7):
    res[i] = days[i] + sum(number_of_holiday) - number_of_holiday[i]
# print(days)
# print(number_of_holiday)
# print(res)

min_i = 500
max_i = 0
for i in range(7):
    if res[i] == min(res):
        min_i = i
    if res[i] == max(res):
        max_i = i

print(get_key(days_of_week, max_i), get_key(days_of_week, min_i))
