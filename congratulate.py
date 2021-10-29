import ast
import datetime
import sys


def format_income_string(users):
    users = users.replace("[", "").replace("]", "")
    return ast.literal_eval(users)


def users_list(users):
    users_list = []
    for i in users:
        users_list.append((i['birthday'][5:10], i['name']))
    return users_list


def week_days_list():
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    base = datetime.datetime.today()
    date_list = [base + datetime.timedelta(days=x) for x in range(7)]
    full_name_date_list = []
    for i in date_list:
        full_name_date_list.append((str(i.month) + '-' + str(i.day), days[i.weekday()]))
    return full_name_date_list


def congratulate(users_list, week_list):
    final_list = {}
    for user in users_list:
        for day in week_list:
            if user[0] == day[0]:
                if day[1] == 'Saturday' or day[1] == 'Sunday':
                    final_list.setdefault('Monday', []).append(user[1])
                else:
                    final_list.setdefault(day[1], []).append(user[1])
    return final_list


if __name__ == "__main__":
    try:
        users = format_income_string(sys.argv[1])
        users_list = users_list(users)
        week_list = week_days_list()
        log = congratulate(users_list, week_list)
        for k, v in log.items():
            print(k + ':', ', '.join(v))
    except SyntaxError:
        print('Проверьте правильность написания списка!')

#"[{'name': 'Bill', 'birthday': '1983-10-23'}, {'name': 'Kim', 'birthday': '1983-10-25'}, {'name': 'Bob', 'birthday': '1987-10-24'}]"
