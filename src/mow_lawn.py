from .mower import Mower


def mow_lawn(procedure: str):
    lines = [line for line in procedure.split('\n') if line]
    plateau_max_x, plateau_max_y = _parse_plateau(lines)
    initial_position_x, initial_position_y, initial_facing = _parse_deploy_situation(lines)
    commands = _parse_commands(lines)

    mower = Mower.deploy(
        initial_position_x, initial_position_y,
        initial_facing,
        plateau_max_x, plateau_max_y
    )

    return mower.execute(commands).report()


def _parse_plateau(lines: list) -> tuple:
    plateau_max_x, plateau_max_y = lines[0].split(' ')

    return int(plateau_max_x), int(plateau_max_y)


def _parse_deploy_situation(lines: list) -> tuple:
    initial_position_x, initial_position_y, initial_facing = lines[1].split(' ')

    return int(initial_position_x), int(initial_position_y), initial_facing


def _parse_commands(lines: list) -> tuple:
    return [command for command in lines[2]]
