#!/usr/bin/python3
from pyfiglet import Figlet
from rich import print as rprint
from rich.prompt import Prompt
import argparse
import random
import threading
import queue

# Password Generation Algorithm
def generate_passwords(first_name, last_name, age, keywords, colors, pets, hobbies, min_length, max_length, num_passwords, result_queue):
    passwords = set()
    base_components = [first_name, last_name, str(age)] + keywords + colors + pets + hobbies

    while len(passwords) < num_passwords:
        password_length = random.randint(min_length, max_length)
        password = ''.join(random.choices(base_components, k=password_length))

        if min_length <= len(password) <= max_length:
            passwords.add(password)

    for password in passwords:
        result_queue.put(password)

def main():
    parser = argparse.ArgumentParser(
        prog='passdicit',
        description='A password generator tool based on user information.',
        epilog='For more info, visit: github.com/dincertekin/passdicit'
    )

    parser.add_argument('-a', '--min', type=int, default=6, help='Minimum password length')
    parser.add_argument('-z', '--max', type=int, default=12, help='Maximum password length')
    parser.add_argument('-l', '--limit', type=int, default=100, help='Number of passwords to generate')
    args = parser.parse_args()

    f = Figlet(font='slant')
    print(f.renderText('passdicit'))

    first_name = Prompt.ask("First Name")
    last_name = Prompt.ask("Last Name")

    while True:
        age_input = Prompt.ask("Age", default="18")
        if age_input.isdigit() and int(age_input) >= 0:
            age = age_input
            break
        else:
            rprint("[red]Please enter a valid age (0 or positive number).[/red]")

    keywords = Prompt.ask("Important Keywords [blue](comma separated)").split(',')
    colors = Prompt.ask("Favorite Colors [blue](comma separated)").split(',')
    pets = Prompt.ask("Pet Names [blue](comma separated)").split(',')
    hobbies = Prompt.ask("Hobbies/Interests [blue](comma separated)").split(',')

    rprint("[bold green]Generating passwords...[/bold green] ")

    result_queue = queue.Queue()
    password_thread = threading.Thread(target=generate_passwords, args=(first_name, last_name, age, keywords, colors, pets, hobbies, args.min, args.max, args.limit, result_queue))
    password_thread.start()
    password_thread.join()

    result = []
    while not result_queue.empty():
        result.append(result_queue.get())

    with open("passwords.lst", "w") as f:
        for password in result:
            f.write(f"{password}\n")

    rprint(f"[bold green]Generated [white]{len(result)}[/white] passwords and saved to [white]passwords.lst[/white] file.[/bold green]")

if __name__ == "__main__":
    main()
