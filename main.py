import argparse
from typing import List


def sort(width: float, height: float, length: float, mass: float) -> List[str]:
    """
    Sorts a package based on its dimensions and mass.

    Parameters:
    width (float): The width of the package in cm.
    height (float): The height of the package in cm.
    length (float): The length of the package in cm.
    mass (float): The mass of the package in kg.

    Returns:
    str: The sorting decision for the package.
    """

    TOTAL_BULKY_THRESHOLD = 1_000_000  # 1,000,000 cm^3
    HEAVY_THRESHOLD = 20  # 20 kg
    INDIVIDUAL_BULK_THRESHOLD = 150  # 150 cm

    volume = width * height * length
    bulky = (
        volume >= TOTAL_BULKY_THRESHOLD
        or width >= INDIVIDUAL_BULK_THRESHOLD
        or height >= INDIVIDUAL_BULK_THRESHOLD
        or length >= INDIVIDUAL_BULK_THRESHOLD
    )
    heavy = mass >= HEAVY_THRESHOLD
    if bulky and heavy:
        return "REJECTED"
    if bulky or heavy:
        return "SPECIAL"
    return "STANDARD"


def main():
    parser = argparse.ArgumentParser(
        description="Sort a package based on its dimensions and mass."
    )
    parser.add_argument(
        "-w", "--width", type=float, help="The width of the package in cm."
    )
    # -h conflicts with help menu argument
    parser.add_argument(
        "-he", "--height", type=float, help="The height of the package in cm."
    )
    parser.add_argument(
        "-l", "--length", type=float, help="The length of the package in cm."
    )
    parser.add_argument(
        "-m", "--mass", type=float, help="The mass of the package in kg."
    )

    args = parser.parse_args()
    sorting_decision = sort(args.width, args.height, args.length, args.mass)
    print(f"The sorting decision for the package is: {sorting_decision}")


if __name__ == "__main__":
    main()
