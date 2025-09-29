names_f = open("student_marks/student_names.txt", 'r')
statistics_f = open("student_marks/statistics.txt", 'r')
math_f = open("student_marks/math.txt", 'r')
physics_f = open("student_marks/physics.txt", 'r')

marks_dict = {}

phys_dict = {}
math_dict = {}
stat_dict = {}

for name, stat_m, math_m, phys_m in zip(names_f.read().splitlines(), statistics_f.read().splitlines(), math_f.read().splitlines(), physics_f.read().splitlines()):
	marks_dict[name] = {"math":int(math_m), "statistics":int(stat_m), "physics":int(phys_m)}
	math_dict[name] = int(math_m)
	phys_dict[name] = int(phys_m)
	stat_dict[name] = int(stat_m)


avarge_dict = {}
for name in marks_dict.keys():
	avarge_dict[name] = sum(marks_dict[name].values())/3
	print(f'Студент {name}, середня оцінка {avarge_dict[name]}')


print("\n\n3 студенти з найвищим рейтингом")
best_3 = sorted(avarge_dict.items(), key=lambda item: item[1])[:-4:-1]
for student in best_3:
	print(student[0])


print(f'\n\nКількість студентів: {len(avarge_dict)}, Максимальна середня оцінка: {max(avarge_dict.values())}, Мінімальна оцінка: {min(avarge_dict.values())}')


best_math = sorted(math_dict.items(), key=lambda item: item[1])[-1]
best_phys = sorted(phys_dict.items(), key=lambda item: item[1])[-1]
best_stat = sorted(stat_dict.items(), key=lambda item: item[1])[-1]
print(f'\n\nМатематика: студент {best_math[0]}, оцінка {best_math[1]}')
print(f'Статистика: студент {best_stat[0]}, оцінка {best_stat[1]}')
print(f'Фізика: студент {best_phys[0]}, оцінка {best_phys[1]}')


l50_names = ""
l50_cnt = 0
for name in avarge_dict.keys():
	if avarge_dict[name] < 50:
		l50_cnt += 1
		l50_names += name + '\n'
print(f'\n\nКількість студентів з оцінкою нижче 50: {l50_cnt}\n{l50_names}')
