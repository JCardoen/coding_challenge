def get_total_achievable_load(plants):
    total_achievable_load = 0
    for plant in plants:
        total_achievable_load += plant.get_pmax()

    return total_achievable_load


def key_function(plant):
    return plant.calculate_cost_per_mwh()


def powerplant_uc_solver(plants, max_load):
    """
        Greedy algorithm implementation
        for the calculation of activated power plants
        Constraint: load required, with 2 subconstraints: pmin and pmax
        Ranking factor: cost per mwh
    """
    copy_plants = sorted(plants, key=key_function)
    total_load = 0

    for i in range(len(copy_plants)):
        current_plant = copy_plants[i]

        if(total_load + current_plant.get_pmin()) <= max_load:
            if(total_load + current_plant.get_pmax()) <= max_load:
                if i < len(copy_plants) - 1:
                    next_plant = copy_plants[i + 1]
                    if (total_load + current_plant.get_pmax() + next_plant.get_pmin()) <= max_load:
                        current_plant.set_p(current_plant.get_pmax())
                        total_load += current_plant.get_pmax()
                    else:
                        effective_load = current_plant.get_pmax() - next_plant.get_pmin()
                        total_load += effective_load
                        current_plant.set_p(effective_load)

                        effective_load = max_load - total_load
                        total_load += effective_load
                        next_plant.set_p(effective_load)
                else:
                    if (total_load + current_plant.get_pmax()) <= max_load:
                        current_plant.set_p(current_plant.get_pmax())
                        total_load += current_plant.get_pmax()
                    else:
                        effective_load = max_load - total_load
                        current_plant.set_p(effective_load)
                        total_load += effective_load
            else:
                effective_load = max_load - total_load
                current_plant.set_p(effective_load)
                total_load += effective_load
        else:
            current_plant.set_p(0)

    return copy_plants
