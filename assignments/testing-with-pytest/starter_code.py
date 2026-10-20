def is_even(number: int) -> bool:
    return number % 2 == 0


def celsius_to_fahrenheit(celsius: float) -> float:
    return celsius * 9 / 5 + 32


def classify_score(score: int) -> str:
    if not 0 <= score <= 100:
        raise ValueError("Score must be between 0 and 100")
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"
