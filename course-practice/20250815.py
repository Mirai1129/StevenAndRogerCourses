def countdown(start: int = 5) -> None:
    while start > 0:
        print(start)
        start -= 1

def print_higher_than_average_scores(scores: list[int]) -> None:
    total = 0
    
    for score in scores:
        total += score
    average = total / len(scores)
    
    for score in scores:
        if score > average:
            print(score)

def calculate_area(length: float, width: float) -> float:
    return length * width

def calculate_volume(length: float, width: float, height: float) -> float:
    return length * width * height

def is_narcissistic_number(num: int) -> bool:
    digits = [int(d) for d in str(num)]
    power = len(digits)
    return sum(d ** power for d in digits) == num

if __name__ == "__main__":
    # countdown
    # countdown()

    # print_higher_than_average_scores
    # scores = [85, 92, 78, 90, 88]
    # print_higher_than_average_scores(scores)

    # math
    # length = 5.0
    # width = 3.0
    # height = 2.0
    # area = calculate_area(length, width)
    # volume = calculate_volume(length, width, height)
    # print(f"Area: {area}, Volume: {volume}")

    # is_narcissistic_number
    test_numbers = [153, 370, 371, 9474, 123]
    for num in test_numbers:
        result = is_narcissistic_number(num)
        print(f"{num} is narcissistic: {result}")
