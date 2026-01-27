import matplotlib.pyplot as plt

SCALE = 20   # 1 ft = 20 pixels
WALL_THICKNESS = 2

def draw_floor_plan(rooms, image_path, plot_length=40, plot_width=30):
    fig, ax = plt.subplots(figsize=(8, 6))

    # 🔹 Draw outer boundary (plot)
    ax.add_patch(
        plt.Rectangle(
            (0, 0),
            plot_length * SCALE,
            plot_width * SCALE,
            fill=False,
            linewidth=3
        )
    )

    x_offset = 0
    y_offset = 0
    max_row_height = 0

    for room in rooms:
        w_ft, h_ft = map(int, room["size"].split("x"))
        w = w_ft * SCALE
        h = h_ft * SCALE

        # Move to next row if exceeds width
        if x_offset + w > plot_length * SCALE:
            x_offset = 0
            y_offset += max_row_height
            max_row_height = 0

        # Draw room
        ax.add_patch(
            plt.Rectangle(
                (x_offset, y_offset),
                w,
                h,
                fill=False,
                linewidth=WALL_THICKNESS
            )
        )

        # Label
        ax.text(
            x_offset + w / 2,
            y_offset + h / 2,
            room["name"],
            ha="center",
            va="center",
            fontsize=8
        )

        x_offset += w
        max_row_height = max(max_row_height, h)

    ax.set_aspect("equal")
    ax.axis("off")
    plt.tight_layout()
    plt.savefig(image_path, dpi=300)
    plt.close()
