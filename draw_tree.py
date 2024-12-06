def draw_tree(height):
    """
    Prints an ASCII tree of the given height.
    :param height: The height of the tree (number of levels).
    """
    if height < 1:
        print("Height must be greater than 0!")
        return

    for i in range(height):
        spaces = " " * (height - i - 1)
        stars = "*" * (2 * i + 1)
        print(spaces + stars)

    trunk_width = height // 3 if height > 3 else 1
    trunk_height = (
        height // 3 if height > 3 else 1
    )
    trunk_space = " " * (
        height - trunk_width // 2 - 1
    )

    for _ in range(trunk_height):
        print(trunk_space + "|" * trunk_width)


if __name__ == "__main__":
    try:
        user_height = int(
            input(
                "Enter the height of the tree: "
            )
        )
        draw_tree(user_height)
    except ValueError:
        print("Please enter a valid integer!")
