from rich import print
from rich.console import Console

console = Console()

email = input("Enter your Email: ")  # Example: g@g.in , anishcse815@gmail.com
k, j, d = 0, 0, 0

if len(email) >= 6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@") == 1):
            if (email[-4] == ".") ^ (email[-3] == "."):
                for i in email:
                    if i.isspace():
                        k = 1
                    elif i.isalpha():
                        if i == i.upper():  # upper case letter
                            j = 1
                    elif i.isdigit():
                        continue
                    elif i in ["_", ".", "@"]:
                        continue
                    else:
                        d = 1

                if k == 1 or j == 1 or d == 1:
                    console.print("[bold red]❌ Wrong Email Format [Code 5][/bold red]")
                else:
                    console.print("[bold green]✅ Right Email[/bold green]")
            else:
                console.print("[bold red]❌ Wrong Email Format [Code 4][/bold red]")
        else:
            console.print("[bold red]❌ Wrong Email Format [Code 3][/bold red]")
    else:
        console.print("[bold red]❌ Wrong Email Format [Code 2][/bold red]")
else:
    console.print("[bold red]❌ Wrong Email Format [Code 1][/bold red]")
