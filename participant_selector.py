#!/usr/bin/env python3

import json
import os
import random
import sys
import time

import pyfiglet
from colorama import Fore
from tabulate import tabulate

DEFAULT_COLOR = Fore.BLUE
HIGHLIGHT_COLOR = Fore.GREEN


def clear_console():
    # For Windows
    if os.name == "nt":
        _ = os.system("cls")
    # For Mac and Linux
    else:
        _ = os.system("clear")


def print_new_line():
    print("")


def typewriter_effect(sentence):
    for char in sentence:
        sys.stdout.write(char)
        sys.stdout.flush()
        type_delay = random.randint(0, 20) / 100
        time.sleep(type_delay)
    print_new_line()
    time.sleep(1)


def type_default(msg: str) -> None:
    typewriter_effect(DEFAULT_COLOR + msg)


def type_highlight(msg: str) -> None:
    typewriter_effect(HIGHLIGHT_COLOR + msg)


def print_default(msg: str) -> None:
    print(DEFAULT_COLOR + msg)


def print_highlight(msg: str) -> None:
    print(HIGHLIGHT_COLOR + msg)


def read_participants_file(file_path: str) -> dict:
    with open(file_path) as user_file:
        file_content = user_file.read()
        parsed_json = json.loads(file_content)
        return parsed_json


def present_participants(participants: dict) -> None:
    table = [(key, value) for key, value in participants.items()]
    print_default(
        tabulate(table, headers=["Nome", "Participações"], tablefmt="outline")
    )
    print_new_line()


def get_random_participant_key(participants: dict) -> str:
    keys = list(participants.keys())
    random_idx = random.randint(0, len(keys) - 1)
    return keys[random_idx]


def present_selected_participant(selected_participant_key: str) -> None:
    type_default("Parabéns!")
    styled_text = pyfiglet.figlet_format(selected_participant_key, font="doom")
    print_highlight(styled_text)
    type_default("É a sua vez :)")


def update_result_file(file_path: str, data: dict) -> None:
    type_default("Atualizando arquivo com resultados")
    with open(file_path, "w") as json_file:
        json.dump(data, json_file, indent=2)


def increase_participation_counter(participants, selected_participant_key) -> None:
    participants[selected_participant_key] += 1


def start_participant_selection():
    input("Aperte qualquer tecla para sortear participante...")


def should_select_another_participant() -> bool:
    repeat = input(
        "Aperte 'o' para escolher outro participante, ou 'enter' para salvar escolha: "
    )
    return repeat == "o"


def main(file_path: str = "participants.json") -> None:
    clear_console()
    all_participants = read_participants_file(file_path)

    max_participation = max(all_participants.values())
    participating = all_participants

    not_participating = {
        key: value
        for key, value in all_participants.items()
        if value == max_participation
    }
    if len(not_participating) != len(all_participants):
        type_default("Estes NÃO serão selecionados:")
        present_participants(not_participating)

        participating = {
            key: value
            for key, value in all_participants.items()
            if value != max_participation
        }

    type_default("Estes são os participantes:")
    present_participants(participating)

    start_participant_selection()

    selected_participant_key = None
    while selected_participant_key is None:
        clear_console()
        selected_participant_key = get_random_participant_key(participating)
        present_selected_participant(selected_participant_key)

        if should_select_another_participant():
            selected_participant_key = None

    increase_participation_counter(all_participants, selected_participant_key)
    update_result_file(file_path, all_participants)


if __name__ == "__main__":
    main()
