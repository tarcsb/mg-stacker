def sort_tech_stacks(stack_options, criteria="overall"):
    if criteria == "team_skills":
        sorted_stacks = sorted(stack_options, key=lambda x: x[2], reverse=True)
    elif criteria == "performance":
        sorted_stacks = sorted(stack_options, key=lambda x: x[2], reverse=True)
    else:
        sorted_stacks = sorted(stack_options, key=lambda x: x[2], reverse=True)
    return sorted_stacks
