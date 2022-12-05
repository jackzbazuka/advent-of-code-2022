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

            first_diff = abs(first_elf_start - first_elf_end)
            second_diff = abs(second_elf_start - second_elf_end)

            print(first_diff, second_diff)

            if first_diff > second_diff:
                # Range of assignments of first elf covers the range of assignments of second elf
                print("first diff is greater")
                if (
                    first_elf_start <= second_elf_start
                    and first_elf_end >= second_elf_end
                ):
                    print("complete overlap")
                    overlap_count += 1
            elif first_diff < second_diff:
                # Range of assignments of second elf covers the range of assignments of first elf
                print("second diff is greater")
                if (
                    second_elf_start <= first_elf_start
                    and second_elf_end >= first_elf_end
                ):
                    print("complete overlap")
                    overlap_count += 1

            elif first_diff == second_diff:
                print("both diff are same")
                if (
                    second_elf_start == first_elf_start
                    and second_elf_end == first_elf_end
                ):
                    print("complete overlap")
                    overlap_count += 1

        return overlap_count


if __name__ == "__main__":
    complete_overlaps = main()
    print(f"Complete overlaps - {complete_overlaps}")

# Complete overlaps - 567
# We are done with part-1 of day-4!
