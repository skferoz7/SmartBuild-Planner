def generate_plan(length, width, floors, bedrooms):
    total_area = length * width * floors

    rooms = []

    rooms.append({"name": "Hall", "size": "15x12"})

    for i in range(bedrooms):
        rooms.append({"name": f"Bedroom {i+1}", "size": "12x10"})

    rooms.append({"name": "Kitchen", "size": "10x8"})
    rooms.append({"name": "Bathroom", "size": "8x6"})

    return total_area, rooms
