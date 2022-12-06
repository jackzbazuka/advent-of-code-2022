def scan_matrix():
    matrix = [[], [], [], [], [], [], [], [], []]

    with open("supplies.in", "r") as f:

        # parse the crates first
        # let's maintain a vertical vector as shown in the readme, it'll be easier to move the crates that way

        for line_num, line in enumerate(f):
            if line_num == 8:
                break

            loop_counter = 1  # start with 1, increment 4 at each loop
            vector_counter = 0

            while loop_counter <= 36:
                if line[loop_counter] != " ":
                    matrix[vector_counter].append(line[loop_counter])
                loop_counter += 4
                vector_counter += 1

    return matrix


def main() -> str:
    matrix = scan_matrix()

    with open("supplies.in", "r") as f:
        for lc, instruction in enumerate(f):
            if lc > 9:
                _, move_quantity, _, from_crate, _, to_crate = instruction.split(" ")
                move_quantity = int(move_quantity.strip())
                from_crate = int(from_crate.strip()) - 1
                to_crate = int(to_crate.strip()) - 1

                matrix[to_crate] = matrix[from_crate][:move_quantity] + matrix[to_crate]
                matrix[from_crate] = matrix[from_crate][move_quantity:]

    sol_elements = [stack[0] for stack in matrix]

    return "".join(sol_elements)


if __name__ == "__main__":
    solution = main()
    print(solution)

"""
After the rearrangement procedure completes, what crate ends up on top of each stack?

Solution -> QNDWLMGNS

Thanks for watching, if you are!!

"""
