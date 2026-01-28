import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Arc

SCALE = 20
OUTER_WALL = 4
INNER_WALL = 2

def draw_room(ax, x, y, w, h, label):
    ax.add_patch(Rectangle((x, y), w, h, fill=False, linewidth=INNER_WALL))
    ax.text(x + w/2, y + h/2, label, ha="center", va="center", fontsize=8)

def draw_floor_plan(rooms, image_path, plot_length, plot_width):
    W = plot_width * SCALE
    H = plot_length * SCALE

    fig, ax = plt.subplots(figsize=(10, 8))

    # Outer wall
    ax.add_patch(Rectangle((0, 0), W, H, fill=False, linewidth=OUTER_WALL))

    # Layout
    left_w = W * 0.3
    center_w = W * 0.4
    right_w = W * 0.3

    top_h = H * 0.55
    bottom_h = H * 0.45

    draw_room(ax, 0, top_h, left_w, H - top_h, "BEDROOM")
    draw_room(ax, left_w, top_h, center_w, H - top_h, "HALL")
    draw_room(ax, left_w + center_w, top_h, right_w, H - top_h, "BEDROOM")

    draw_room(ax, 0, 0, left_w, bottom_h, "KITCHEN")
    draw_room(ax, left_w, 0, center_w * 0.5, bottom_h, "BATH")
    draw_room(ax, left_w + center_w * 0.5, 0, center_w * 0.5 + right_w, bottom_h, "DINING")

    # Door
    ax.add_patch(Arc((left_w + center_w/2, 0), 40, 40, theta1=0, theta2=90))

    # 🔥 THIS FIXES YOUR ISSUE
    ax.set_xlim(0, W)
    ax.set_ylim(0, H)
    ax.set_aspect("equal")
    ax.axis("off")

    plt.tight_layout()
    plt.savefig(image_path, dpi=300)
    plt.close()
