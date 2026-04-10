# Core Number

Small Python CLI tool that calculates a **core number** from either:

- a **4-letter word** (`A=1`, `B=2`, ..., `Z=26`), or
- a **number with at least 4 digits**.

The script tries valid operator orders using:

- `+` for the first number
- one each of `-`, `x`, and `:` for the remaining three numbers

It then returns the **smallest positive whole number** that can be produced.

If the input is a number with more than 4 digits, the script also tries all possible ways to split it into **4 parts** and chooses the split that produces the smallest positive whole number.

It also prints the expression that was used, for example:

```text
+ 8 - 6 x 45 : 5
```

## What the script does

### Word input

If you enter a 4-letter word, the script:

1. converts each letter to its alphabet position
2. creates a list of 4 numbers
3. tries all valid operator orders
4. returns the smallest positive whole-number result
5. prints the corresponding letter if the core number is between `1` and `26`

Example:

```text
BABA -> [2, 1, 2, 1]
```

### Number input

If you enter a number:

- with exactly **4 digits**, each digit is used as one number
- with **more than 4 digits**, the script tries every possible split into 4 numbers

It then selects the split and operator combination that produces the **smallest positive whole number**.

## Requirements

- Python `>= 3.14`
- [`uv`](https://docs.astral.sh/uv/)

## Setup with `uv`

Clone the repository and install/sync the project environment:

```bash
git clone <your-repo-url>
cd core-number
uv sync
```

## Run the script

Start the CLI with:

```bash
uv run python main.py
```

You will then be prompted for either a word or a number.

## Example usage

### Example 1: Number with more than 4 digits

Input:

```text
86455
```

Output:

```text
Word or number (at least 4 characters): Numbers: [8, 6, 45, 5]
Expression: + 8 - 6 x 45 : 5
Core number: 18
```

### Example 2: 4-digit number

Input:

```text
8645
```

Output:

```text
Word or number (at least 4 characters): Numbers: [8, 6, 4, 5]
Expression: + 8 x 6 : 4 - 5
Core number: 7
```

### Example 3: 4-letter word

Input:

```text
BABA
```

Output:

```text
Word or number (at least 4 characters): Numbers: [2, 1, 2, 1]
Expression: + 2 - 1 x 2 : 1
Core number: 2
Letter: B
```

## Input rules

- Words must contain **exactly 4 letters** (`A-Z` only)
- Numbers must contain **at least 4 digits**
- Only **positive whole-number core numbers** are accepted as valid results
- If no valid positive whole-number result can be found, the script prints an error

## Project file

The main logic is in:

- `main.py`

## Quick start

```bash
uv sync
uv run python main.py
```

