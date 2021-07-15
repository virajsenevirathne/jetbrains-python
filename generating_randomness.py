def get_input():
    return ''.join(
        [num for num in get_input_process('Print a random string containing 0 or 1:\n\n') if num == '1' or num == '0'])


def get_binary_value(decimal_value):
    if decimal_value <= 1:
        return str(decimal_value)
    return get_binary_value(int(decimal_value / 2)) + str((decimal_value % 2))


def get_binary(decimal_value):
    return get_binary_value(decimal_value).zfill(3)


def get_input_process(text):
    print(text)
    return ''.join([c for c in input() if c == '0' or c == '1'])


def process_input(text):
    return ''.join([c for c in text if c == '0' or c == '1'])


print("Please give AI some data to learn...\nThe current data length is 0, 100 symbols left")

s = get_input_process("Print a random string containing 0 or 1:\n\n")

while len(s) < 100:
    print(f"Current data length is {len(s)}, {100 - len(s)} symbols left")
    s = s + get_input()

print(f"\nFinal data string:\n{s}\n")

keys = [get_binary(i) for i in range(8)]
triad_count = {key: {'0': 0, '1': 0} for key in keys}

for i in range(len(s) - 3):
    ch = s[i + 3]
    key = s[i:i + 3]
    triad_count[key][ch] += 1

print(
    "You have $1000. Every time the system successfully predicts your next press, you lose $1.\n"
    "Otherwise, you earn $1. Print \"enough\" to leave the game. Let's go!")
capital = 1000
# input_string = get_input_process("Please enter a test string containing 0 or 1:\n\n")


while True:
    input_string = input("\nPrint a random string containing 0 or 1:\n")

    if input_string == "enough":
        print("Game over!")
        break
    else:
        input_string = process_input(input_string)

    if (len(input_string) > 3):
        test_string = [ch for ch in input_string]
        pred_string = [str(i) for i in range(len(input_string))]
        best_guess = {key: '0' if triad_count[key]['0'] >= triad_count[key]['1'] else '1' for key in triad_count.keys()}

        for i in range(len(test_string)):
            if i < 3:
                pred_string[i] = test_string[i]
            else:
                key = ''.join(test_string[i - 3:i])
                pred_string[i] = best_guess.get(key)

        correct_bits = 0

        for i in range(3, len(pred_string)):
            if pred_string[i] == test_string[i]:
                correct_bits += 1

        print(f"prediction:\n{(''.join(pred_string).strip())}\n")
        print(f"Computer guessed right {correct_bits} out of {(len(pred_string) - 3)} symbols "
              f"({correct_bits / (len(pred_string) - 3) * 100:.2f} %)")

        capital = capital - (correct_bits - (len(pred_string) - 3 - correct_bits))
        print(f"Your capital is now ${capital}")
