from mamba import (
    context,
    description,
    it
)
from expects import (
    expect,
    equal
)

from src.mower import Mower

NORTH = 'N'
EAST = 'E'
WEST = 'W'
SOUTH = 'S'

with description('Seat Mower'):
    with context('when deploying the mower'):
        with it('can be faced north'):
            mower = Mower.deploy(NORTH)

            expect(mower.report()).to(equal(NORTH))

        with it('can be faced east'):
            mower = Mower.deploy(EAST)

            expect(mower.report()).to(equal(EAST))

        with it('can be faced west'):
            mower = Mower.deploy(WEST)

            expect(mower.report()).to(equal(WEST))

        with it('can be faced south'):
            mower = Mower.deploy(SOUTH)

            expect(mower.report()).to(equal(SOUTH))
