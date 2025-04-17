import random


def create_group(participant_list, group_size, additional_participant):
    random.shuffle(participant_list)
    group_list = []
    group = []
    for participant in participant_list:
        if len(group) < group_size:
            group.append(participant)
        else:
            group_list.append(group)
            group = [participant]
    if len(group) > 0:
        if len(group) < group_size:
            group.append(additional_participant)
        group_list.append(group)
    return group_list


if "__main__" == __name__:
    participant_list = ["Name", "of", "each", "participant"]
    group_list = create_group(participant_list, 3, "Matheus")
    print("Result:")
    for group in group_list:
        print(group)
