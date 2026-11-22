"""Console calculator used as a small Snyk test application."""


OPERATIONS = {
    "+": "dodawanie",
    "-": "odejmowanie",
    "*": "mnozenie",
    "/": "dzielenie",
}


def read_number(prompt: str) -> float:
    while True:
        raw_value = input(prompt).strip().replace(",", ".")
        try:
            return float(raw_value)
        except ValueError:
            print("Niepoprawna liczba, sprobuj ponownie.")


def read_operation() -> str:
    while True:
        operation = input("Wybierz operacje (+, -, *, /): ").strip()
        if operation in OPERATIONS:
            return operation
        print("Nieznana operacja, sprobuj ponownie.")


def calculate(left: float, right: float, operation: str) -> float:
    if operation == "+":
        return left + right
    if operation == "-":
        return left - right
    if operation == "*":
        return left * right
    if operation == "/":
        if right == 0:
            raise ZeroDivisionError("Nie mozna dzielic przez zero.")
        return left / right
    raise ValueError(f"Nieobslugiwana operacja: {operation}")


def main() -> None:
    print("Prosty kalkulator konsolowy")
    print("Dostepne operacje: " + ", ".join(OPERATIONS))

    while True:
        left = read_number("Podaj pierwsza liczbe: ")
        operation = read_operation()
        right = read_number("Podaj druga liczbe: ")

        try:
            result = calculate(left, right, operation)
        except ZeroDivisionError as error:
            print(error)
        else:
            print(f"Wynik: {result}")

        again = input("Kolejne obliczenie? (t/n): ").strip().lower()
        if again not in {"t", "tak", "y", "yes"}:
            print("Koniec.")
            break


if __name__ == "__main__":
    main()
