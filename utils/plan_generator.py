def generate_plan(length, width, floors, bedrooms):
    total_area = length * width * floors

    rooms = []

    # Hall
    rooms.append({
        "name": "Hall",
        "size": "15 x 12 ft"
    })

    # Bedrooms
    for i in range(1, bedrooms + 1):
        rooms.append({
            "name": f"Bedroom {i}",
            "size": "12 x 10 ft"
        })

    # Kitchen & Bathroom
    rooms.append({"name": "Kitchen", "size": "10 x 8 ft"})
    rooms.append({"name": "Bathroom", "size": "8 x 6 ft"})

    return total_area, rooms
