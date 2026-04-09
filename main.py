from itertools import permutations


def letter_to_number(letter: str) -> int:
    return ord(letter) - ord("A") + 1


def number_to_letter(number: int) -> str:
    if not isinstance(number, int) or isinstance(number, bool):
        raise ValueError("Die Zahl muss eine ganze Zahl zwischen 1 und 26 sein.")

    if number < 1 or number > 26:
        raise ValueError("Die Zahl muss zwischen 1 und 26 liegen.")

    return chr(ord("A") + number - 1)


def calculate_core_number(numbers):
    if len(numbers) != 4:
        raise ValueError("Es werden genau vier Zahlen benötigt.")

    valid_results = []

    for ops in permutations(("-", "*", "/")):
        result = float(numbers[0])

        for operator, value in zip(ops, numbers[1:]):
            if operator == "-":
                result -= value
            elif operator == "*":
                result *= value
            else:
                if value == 0:
                    result = None
                    break
                result /= value

        if result is None:
            continue

        rounded = round(result)
        if abs(result - rounded) < 1e-9:
            valid_results.append((rounded, ops))

    if not valid_results:
        raise ValueError("Es konnte keine Core Number mit der Eingabe gefunden werden.")

    positive = [r for r in valid_results if r[0] > 0]
    if positive:
        best = min(positive, key=lambda x: x[0])
        return best[0], best[1]

    raise ValueError("Es konnte keine Core Number mit der Eingabe gefunden werden.")


def format_expression(numbers, operators):
    """Format the expression in the style: + 8 - 6 x 45 : 5"""
    op_symbols = {"-": "-", "*": "x", "/": ":"}

    expression = f"+ {numbers[0]}"
    for op, num in zip(operators, numbers[1:]):
        symbol = op_symbols[op]
        expression += f" {symbol} {num}"

    return expression


def generate_partitions(digit_string):
    """Generate all possible ways to split a digit string into 4 parts."""
    n = len(digit_string)
    if n < 4:
        return []

    partitions = []
    # i, j, k are split points: [0:i], [i:j], [j:k], [k:]
    for i in range(1, n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                part1 = int(digit_string[:i])
                part2 = int(digit_string[i:j])
                part3 = int(digit_string[j:k])
                part4 = int(digit_string[k:])
                partitions.append([part1, part2, part3, part4])

    return partitions


def process_number(digit_string):
    """Process a number string with at least 4 digits."""
    if len(digit_string) == 4:
        numbers = [int(d) for d in digit_string]
        core, ops = calculate_core_number(numbers)
        return core, [int(d) for d in digit_string], ops

    partitions = generate_partitions(digit_string)
    if not partitions:
        raise ValueError("Ungültige Eingabe: Es werden mindestens 4 Ziffern benötigt.")

    best_core = None
    best_partition = None
    best_ops = None

    for partition in partitions:
        try:
            core, ops = calculate_core_number(partition)
            if best_core is None or core < best_core:
                best_core = core
                best_partition = partition
                best_ops = ops
        except ValueError:
            continue

    if best_core is None:
        raise ValueError("Es konnte keine Core Number mit der Eingabe gefunden werden.")

    return best_core, best_partition, best_ops


def process_word(word):
    """Process a word input."""
    word = word.upper()

    if len(word) != 4:
        raise ValueError("Bitte exakt 4 Buchstaben eingeben.")

    if not word.isalpha() or not word.isascii():
        raise ValueError("Bitte nur Buchstaben A-Z ohne Sonderzeichen eingeben.")

    numbers = [letter_to_number(letter) for letter in word[:4]]
    core_number, ops = calculate_core_number(numbers)
    return core_number, numbers, ops


def main():
    user_input = input("Wort oder Zahl (mind. 4 Zeichen): ").strip()

    if not user_input:
        print("Bitte geben Sie etwas ein.")
        return

    try:
        if user_input.isdigit():
            # Input is a number
            if len(user_input) < 4:
                print("Bitte mindestens 4 Ziffern eingeben.")
                return

            core_number, numbers, ops = process_number(user_input)
            print(f"Zahlen: {numbers}")
            expression = format_expression(numbers, ops)
            print(f"Ausdruck: {expression}")
            print(f"Core number: {core_number}")
        else:
            # Input is a word
            core_number, numbers, ops = process_word(user_input)
            print(f"Zahlen: {numbers}")
            expression = format_expression(numbers, ops)
            print(f"Ausdruck: {expression}")
            print(f"Core number: {core_number}")
            if core_number > 0 and core_number < 27:
                letter = number_to_letter(core_number)
                print(f"Letter: {letter}")
    except ValueError as e:
        print(f"Fehler: {e}")


if __name__ == "__main__":
    main()
