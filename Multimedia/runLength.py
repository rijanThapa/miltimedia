def run_length_encoding(input_string):
    """Run-length encoding implementation that takes an input string and returns its RLE representation"""

    count = 1
    prev_char = input_string[0]
    output = ""

    for char in input_string[1:]:
        if char == prev_char:
            count += 1
        else:
            output += str(count) + prev_char
            count = 1
            prev_char = char

    output += str(count) + prev_char

    return output

input_string = input("Enter a string for run-length encoding: ")

encoded_string = run_length_encoding(input_string)

print("Encoded output:", encoded_string)
