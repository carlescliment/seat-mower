from .mower import Mower


def mow_lawn(procedure: str):
    lines = [line for line in procedure.split('\n') if line]
    plateau_max_x, plateau_max_y = _parse_plateau(lines[0])

    current_line = 1
    reports = []
    while current_line < len(lines):
        reports.append(_run_mower_procedure(
            lines[current_line],
            lines[current_line + 1],
            plateau_max_x,
            plateau_max_y
        ))
        current_line += 2

    return '\n'.join(reports)


def _run_mower_procedure(
    deploy_line: str,
    commands_line: str,
    plateau_max_x: int,
    plateau_max_y: int
):
    initial_position_x, initial_position_y, initial_facing = _parse_deploy_situation(deploy_line)
    commands = _parse_commands(commands_line)
    mower = Mower.deploy(
        initial_position_x, initial_position_y,
        initial_facing,
        plateau_max_x,
        plateau_max_y
    )

    return mower.execute(commands).report()


def _parse_plateau(line: list) -> tuple:
    plateau_max_x, plateau_max_y = line.split(' ')

    return int(plateau_max_x), int(plateau_max_y)


def _parse_deploy_situation(line: str) -> tuple:
    initial_position_x, initial_position_y, initial_facing = line.split(' ')

    return int(initial_position_x), int(initial_position_y), initial_facing


def _parse_commands(line: str) -> tuple:
    return [command for command in line]
