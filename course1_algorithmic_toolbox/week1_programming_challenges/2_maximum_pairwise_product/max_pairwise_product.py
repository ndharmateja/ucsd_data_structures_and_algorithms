def max_pairwise_product(numbers):
    first, second = -float('inf'), -float('inf')
    for number in numbers:
        if number > first:
            second = first
            first = number
        elif number > second:
            second = number

    return first * second


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
