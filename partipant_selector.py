import json
import random

import pyfiglet
from colorama import Fore
from pyfiglet import Figlet
from tabulate import tabulate


def print_default(msg: str) -> None:
    print(Fore.BLUE + msg)


def print_highlight(msg: str) -> None:
    print(Fore.GREEN + msg)


def read_participants_file(file_path: str) -> dict:
    with open(file_path) as user_file:
        file_content = user_file.read()
        parsed_json = json.loads(file_content)
        return parsed_json


def present_participants(participants: dict) -> None:
    print_default('Estes são os participantes:')
    table = [(key, value) for key, value in participants.items()]
    print_default(tabulate(table, headers=['Nome', 'Participações'], tablefmt="outline"))


def get_random_participant_key(participants: dict) -> str:
    keys = list(participants.keys())
    random_idx = random.randint(0, len(keys) - 1)
    return keys[random_idx]


def present_selected_participant(selected_participant_key: str) -> None:
    print_default("Parabéns!")
    styled_text = pyfiglet.figlet_format(selected_participant_key, font='doom')
    print_highlight(styled_text)
    print_default("É a sua vez :)")


def update_result_file(file_path: str, data: dict) -> None:
    with open(file_path, "w") as json_file:
        json.dump(data, json_file, indent=4)


def increase_participation_counter(participants, selected_participant_key) -> None:
    participants[selected_participant_key] += 1


def main(file_path: str = 'participants.json') -> None:
    participants = read_participants_file(file_path)
    present_participants(participants)
    selected_participant_key = get_random_participant_key(participants)
    present_selected_participant(selected_participant_key)
    increase_participation_counter(participants, selected_participant_key)
    update_result_file(file_path, participants)


if __name__ == '__main__':
    main()
