def draw_road(orientation = "horizontal", length = 5):

    if orientation == "horizontal":
        print("----" * length)
        print("--  "* length)
        print("----" * length)

    if orientation == "vertical":
        for _ in range(length):
            print("|  |  |")
            print("|     |")

    else:

        print("Road not found!")
