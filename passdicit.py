#!/usr/bin/python3
from pyfiglet import Figlet
from rich import print as rprint
from rich.prompt import Prompt
import argparse
import random
import threading

def generate_passwords(first_name, last_name, age, keywords, colors, pets, hobbies, min_length, max_length, num_passwords, result):
    passwords = set()
    base_components = [first_name, last_name, str(age)] + keywords + colors + pets + hobbies
    
    while len(passwords) < num_passwords:
        password_length = random.randint(min_length, max_length)
        password = ''.join(random.choices(base_components, k=password_length))
        
        if min_length <= len(password) <= max_length:
            passwords.add(password)

    result.extend(passwords)

def main():
    parser = argparse.ArgumentParser(
        prog='PassDict',
        description='A password generator tool based on user information.',
        epilog='For more info, visit: github.com/dincertekin/passdicit'
    )

    parser.add_argument('-x', '--min', type=int, default=6, help='Minimum password length')
    parser.add_argument('-z', '--max', type=int, default=12, help='Maximum password length')
    parser.add_argument('-l', '--limit', type=int, default=1000, help='Number of passwords to generate')
    args = parser.parse_args()

    f = Figlet(font='slant')
    print(f.renderText('PassDict'))

    first_name = Prompt.ask("First Name")
    last_name = Prompt.ask("Last Name")
    
    while True:
        age_input = Prompt.ask("Age (0+)", default="0")
        if age_input.isdigit() and int(age_input) >= 0:
            age = age_input
            break
        else:
            rprint("[red]Please enter a valid age (0 or positive number).[/red]")
    
    keywords = Prompt.ask("Important Keywords (comma separated)").split(',')
    colors = Prompt.ask("Favorite Colors (comma separated)").split(',')
    pets = Prompt.ask("Pet Names (comma separated)").split(',')
    hobbies = Prompt.ask("Hobbies/Interests (comma separated)").split(',')

    rprint("[bold green]Generating passwords...[/bold green]")

    result = []
    password_thread = threading.Thread(target=generate_passwords,
        args=(first_name, last_name, age, keywords, colors, pets, hobbies,
        args.min, args.max, args.limit, result)
    )
    password_thread.start()
    password_thread.join()

    with open("passwords.lst", "w") as f:
        for password in result:
            f.write(f"{password}\n")

    rprint(f"[bold green]Generated {len(result)} passwords and saved to passwords.lst.[/bold green]")

if __name__ == "__main__":
    main()