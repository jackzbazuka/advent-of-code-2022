def main() -> int:
    with open("assignments.in", "r") as f:
        overlap_count = 0  # check for complete overlaps

        for assignment_pair in f:
            first_elf, second_elf = assignment_pair.split(",")

            first_elf_start, first_elf_end = first_elf.split("-")
            second_elf_start, second_elf_end = second_elf.split("-")

            first_elf_start = int(first_elf_start)
            first_elf_end = int(first_elf_end)
            second_elf_start = int(second_elf_start)
            second_elf_end = int(second_elf_end)

            if (
                second_elf_start >= first_elf_start
                and second_elf_start <= first_elf_end
            ):
                overlap_count += 1
            elif first_elf_end >= second_elf_start and first_elf_end <= second_elf_end:
                overlap_count += 1
            elif (
                first_elf_start >= second_elf_start
                and first_elf_start <= second_elf_end
            ):
                overlap_count += 1
            elif second_elf_end >= first_elf_start and second_elf_end <= first_elf_end:
                overlap_count += 1

        return overlap_count


if __name__ == "__main__":
    complete_overlaps = main()
    print(f"Complete overlaps - {complete_overlaps}")

# Complete overlaps - 907
# Thanks for watching !!!
