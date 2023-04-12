ticket_count = int(input("Введите количество билетов: "))
age_list = []
for i in range(ticket_count):
    age = int(input("Введите возраст посетителя: "))
    age_list.append(age)

total_cost = 0
for age in age_list:
    if age < 18:
        cost = 0
    elif age < 25:
        cost = 990
    else:
        cost = 1390
    total_cost += cost

if ticket_count > 3:
    total_cost *= 0.9

print("Сумма к оплате:", total_cost, "руб.")