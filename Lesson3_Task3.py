#печать уникальных значений словарей
input = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
{"VI": "S005"}, {"VII": "S005"}, {" V ":"S009"}, {" VIII":"S007"}]
values = []

for dictionary in input:
    for key in dictionary:
        values.append(dictionary[key])
print(set(values))