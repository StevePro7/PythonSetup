from fractions import Fraction


def mixed_numeral1(vulgar: int) -> tuple[int, Fraction]:
    if not (hasattr(vulgar, 'numerator') and hasattr(vulgar, 'denominator')):
        raise TypeError(f"Input {vulgar} is not a rational number")

    integer: int = vulgar.numerator // vulgar.denominator
    fraction: Fraction = Fraction(vulgar.numerator - integer * vulgar.denominator, vulgar.denominator)
    return integer, fraction


def mixed_numeral2(vulgar: int) -> tuple[int, Fraction]:
    integer: int = vulgar.numerator // vulgar.denominator
    fraction: Fraction = Fraction(vulgar.numerator - integer * vulgar.denominator, vulgar.denominator)
    return integer, fraction


def mixed_numeral3(vulgar: int) -> tuple[int, Fraction]:
    try:
        integer: int = vulgar.numerator // vulgar.denominator
        fraction: Fraction = Fraction(vulgar.numerator - integer * vulgar.denominator, vulgar.denominator)
        return integer, fraction
    except AttributeError as e:
        raise TypeError(f"Input {vulgar} is not a rational number")


if __name__ == '__main__':
    # test = mixed_numeral1(3 / 2)
    test = mixed_numeral2(3 / 2)
    # test = mixed_numeral3(3 / 2)
    print(test)