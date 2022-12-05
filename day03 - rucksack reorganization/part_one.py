def main() -> int:
    priority_accumulator = 0

    with open("rucksack.in", "r") as f:
        for rucksack in f:
            half_idx = int(len(rucksack.strip()) / 2)
            left_compartment = rucksack.strip()[:half_idx]
            right_compartment = rucksack.strip()[half_idx:]

            repeat_char_set = set(left_compartment).intersection(right_compartment)
            repeat_char = "".join(repeat_char_set).strip()

            priority = (
                ord(repeat_char) - 96
                if repeat_char.islower()
                else ord(repeat_char) - 38
            )

            priority_accumulator += priority

    return priority_accumulator


if __name__ == "__main__":
    total_priority = main()
    print(total_priority)
