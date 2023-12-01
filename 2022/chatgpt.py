def find_frequency_repeats(input_list):
    """
    This function takes a list of numbers and returns the first frequency
    that is seen twice.
    """
    seen_freqs = set()
    accumulator = 0
    while True:
        for num in input_list:
            accumulator += num
            if accumulator in seen_freqs:
                return accumulator
            seen_freqs.add(accumulator)

if __name__ == "__main__":
    input_list = [int(line) for line in open("./input_day1.txt")]
    answer = find_frequency_repeats(input_list)
    print(answer)