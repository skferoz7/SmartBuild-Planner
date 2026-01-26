import matplotlib.pyplot as plt

def draw_floor_plan(rooms, file_path):
    fig, ax = plt.subplots(figsize=(8, 6))

    x, y = 0, 0

    for room in rooms:
        width, height = map(int, room["size"].replace("ft", "").split("x"))

        ax.add_patch(
            plt.Rectangle((x, y), width, height, fill=False)
        )
        ax.text(
            x + width/4, y + height/2, room["name"], fontsize=9
        )

        x += width  # next room side by side

    ax.set_aspect("equal")
    ax.axis("off")

    plt.savefig(file_path)
    plt.close()
