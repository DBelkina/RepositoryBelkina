# TODO Напишите функцию find_common_participants
def find_common_participants(str1_, str2_, r=', '):
    set_first_group = set(str1_.split(r))
    set_second_group = set(str2_.split(r))
    c_list = set_first_group.intersection(set_second_group)
    c_list = list(c_list)
    c_list.sort()
    return(c_list)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

print(find_common_participants(participants_first_group, participants_second_group, r='/'))