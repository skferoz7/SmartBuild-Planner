import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Arc

# CONFIG
SCALE = 20          # 1 ft = 20 drawing units
OUTER_WALL = 3
INNER_WALL = 1.5


# HELPERS
def draw_room(ax, x, y, w, h, label):
    ax.add_patch(
        Rectangle((x, y), w, h, fill=False, linewidth=INNER_WALL)
    )
    ax.text(
        x + w / 2,
        y + h / 2,
        label,
        ha="center",
        va="center",
        fontsize=8
    )


def select_layout(bedrooms, area):
    """
    Decide layout type based on bedrooms + plot area
    """
    if bedrooms == 1:
        return "1bhk"

    if bedrooms == 2:
        if area < 500:
            return "2bhk_compact"
        else:
            return "2bhk_standard"

    if bedrooms >= 3:
        if area < 900:
            return "3bhk_compact"
        else:
            return "3bhk_standard"

# MAIN DRAW FUNCTION
def draw_floor_plan(rooms, image_path, plot_length, plot_width, bedrooms):
    """
    Draw dynamic floor plan based on inputs
    """

    # Convert plot size to drawing units
    W = plot_width * SCALE
    H = plot_length * SCALE
    area = plot_length * plot_width

    layout = select_layout(bedrooms, area)

    fig, ax = plt.subplots(figsize=(7, 7))

    # OUTER WALL
    ax.add_patch(
        Rectangle((0, 0), W, H, fill=False, linewidth=OUTER_WALL)
    )

    top_h = H * 0.55
    bottom_h = H * 0.45

    # 1 BHK
    if layout == "1bhk":
        draw_room(ax, 0, top_h, W, H - top_h, "HALL")
        draw_room(ax, 0, 0, W * 0.6, bottom_h, "BEDROOM")
        draw_room(ax, W * 0.6, 0, W * 0.4, bottom_h, "KITCHEN")

    # 2 BHK COMPACT
    elif layout == "2bhk_compact":
        draw_room(ax, 0, top_h, W * 0.5, H - top_h, "BEDROOM")
        draw_room(ax, W * 0.5, top_h, W * 0.5, H - top_h, "HALL")
        draw_room(ax, 0, 0, W * 0.4, bottom_h, "KITCHEN")
        draw_room(ax, W * 0.4, 0, W * 0.6, bottom_h, "DINING")

    # 2 BHK STANDARD
    elif layout == "2bhk_standard":
        left = W * 0.33
        center = W * 0.34
        right = W * 0.33

        draw_room(ax, 0, top_h, left, H - top_h, "BEDROOM")
        draw_room(ax, left, top_h, center, H - top_h, "HALL")
        draw_room(ax, left + center, top_h, right, H - top_h, "BEDROOM")

        draw_room(ax, 0, 0, left, bottom_h, "KITCHEN")
        draw_room(ax, left, 0, center * 0.5, bottom_h, "BATH")
        draw_room(ax, left + center * 0.5, 0,
                  center * 0.5 + right, bottom_h, "DINING")

    # 3 BHK COMPACT
    elif layout == "3bhk_compact":
        room_w = W / 3

        draw_room(ax, 0, top_h, room_w, H - top_h, "BEDROOM")
        draw_room(ax, room_w, top_h, room_w, H - top_h, "BEDROOM")
        draw_room(ax, room_w * 2, top_h, room_w, H - top_h, "HALL")

        draw_room(ax, 0, 0, room_w, bottom_h, "KITCHEN")
        draw_room(ax, room_w, 0, room_w, bottom_h, "BATH")
        draw_room(ax, room_w * 2, 0, room_w, bottom_h, "DINING")

    # 3 BHK STANDARD
    else:
        room_w = W / 3

        draw_room(ax, 0, top_h, room_w, H - top_h, "BEDROOM")
        draw_room(ax, room_w, top_h, room_w, H - top_h, "HALL")
        draw_room(ax, room_w * 2, top_h, room_w, H - top_h, "BEDROOM")

        draw_room(ax, 0, 0, room_w, bottom_h, "KITCHEN")
        draw_room(ax, room_w, 0, room_w * 0.5, bottom_h, "BATH")
        draw_room(ax, room_w * 1.5, 0, room_w * 1.5, bottom_h, "DINING")

    # MAIN DOOR (DECORATIVE)
    ax.add_patch(
        Arc((W / 2, 0), 40, 40, theta1=0, theta2=90, linewidth=1.5)
    )

    ax.set_xlim(0, W)
    ax.set_ylim(0, H)
    ax.invert_yaxis()
    ax.set_aspect("equal")
    ax.axis("off")

    plt.tight_layout()
    plt.savefig(image_path, dpi=300)
    plt.close()
