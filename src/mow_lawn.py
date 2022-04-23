from .mower import Mower


def mow_lawn(procedure: str):
    lines = [line for line in procedure.split('\n') if line]
    plateau_max_x, plateau_max_y = lines[0].split(' ')
    initial_position_x, initial_position_y, initial_facing = lines[1].split(' ')
    commands = [command for command in lines[2]]
    mower = Mower.deploy(
        int(initial_position_x), int(initial_position_y),
        initial_facing,
        int(plateau_max_x), int(plateau_max_y)
    )

    return mower.execute(commands).report()