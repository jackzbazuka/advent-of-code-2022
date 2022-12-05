def main() -> int:
    priority_accumulator = 0

    with open("rucksack.in", "r") as f:
        mem_count = 0
        priority_accumulator = 0
        mutual_intersection = ""

        three_count = 0

        for rucksack in f:
            if mem_count == 3:
                priority = (
                    ord(mutual_intersection.strip()) - 96
                    if mutual_intersection.strip().islower()
                    else ord(mutual_intersection.strip()) - 38
                )

                print(f"Cost of {mutual_intersection.strip()} - {priority}")

                priority_accumulator += priority
                three_count += 1
                mem_count = 0

            if mem_count == 0:
                mutual_intersection = rucksack.strip()
            elif mem_count > 0 and mem_count < 3:
                mutual_intersection = "".join(
                    set(mutual_intersection.strip()).intersection(rucksack.strip())
                )

            print(f"{mem_count} - {mutual_intersection}")

            mem_count += 1

        priority = (
            ord(mutual_intersection.strip()) - 96
            if mutual_intersection.strip().islower()
            else ord(mutual_intersection.strip()) - 38
        )

        print(f"Cost of {mutual_intersection.strip()} - {priority}")

        priority_accumulator += priority
        three_count += 1

        print(f"Resets - {three_count}")

    return priority_accumulator


if __name__ == "__main__":
    total_priority = main()
    print(total_priority)
