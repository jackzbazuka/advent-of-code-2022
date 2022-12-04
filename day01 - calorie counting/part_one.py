def main() -> None:
    """
    Returns:
        elf_index: number
        elf_calories: number
    """

    with open("calories.in", "r") as f:
        calories_per_elf = []
        calories_accumulator = 0

        for line in f:
            if line != "\n":
                calories_accumulator += int(line)
            else:
                calories_per_elf.append(calories_accumulator)
                calories_accumulator = 0

        calories_per_elf.sort(reverse=True)

        return calories_per_elf[0]


if __name__ == "__main__":
    max_calories = main()
    print(max_calories)
