def filter_programs(programs, criteria):
    filtered_programs = []
    for program in programs:
        if all(program.get(key) in value for key, value in criteria.items()):
            filtered_programs.append(program)
    return filtered_programs
