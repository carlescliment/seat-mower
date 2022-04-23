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
            mower = Mower.deploy(0, 0, NORTH)

            expect(mower.report()).to(equal(f'0 0 {NORTH}'))

        with it('can be faced east'):
            mower = Mower.deploy(0, 0, EAST)

            expect(mower.report()).to(equal(f'0 0 {EAST}'))

        with it('can be faced west'):
            mower = Mower.deploy(0, 0, WEST)

            expect(mower.report()).to(equal(f'0 0 {WEST}'))

        with it('can be faced south'):
            mower = Mower.deploy(0, 0, SOUTH)

            expect(mower.report()).to(equal(f'0 0 {SOUTH}'))

        with it('can be placed on a given X coordinate'):
            mower = Mower.deploy(1, 0, SOUTH)

            expect(mower.report()).to(equal(f'1 0 {SOUTH}'))

        with it('can be placed on a given Y coordinate'):
            mower = Mower.deploy(1, 2, SOUTH)

            expect(mower.report()).to(equal(f'1 2 {SOUTH}'))

    with context('when spinning the mower right or left'):

        with context('when facing north'):

            with it('will face west when spinning left'):
                mower = Mower.deploy(0, 0, NORTH)

                mower.execute('L')

                expect(mower.report()).to(equal(f'0 0 {WEST}'))

            with it('will face east when spinning right'):
                mower = Mower.deploy(0, 0, NORTH)

                mower.execute('R')

                expect(mower.report()).to(equal(f'0 0 {EAST}'))
