def calculate_cost(total_area, budget):
    rate_per_sqft = 1500  # standard rate
    estimated_cost = total_area * rate_per_sqft

    status = "Within Budget" if estimated_cost <= budget else "Exceeds Budget"

    return estimated_cost, status
