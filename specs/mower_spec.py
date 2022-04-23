from mamba import (
    before,
    context,
    description,
    it
)
from expects import (
    expect,
    equal,
    raise_error
)

from src.mower import (
    CannotGoOutOfThePlateauError,
    Mower
)

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

            with before.each:
                self.mower = Mower.deploy(0, 0, NORTH)

            with it('will face west when spinning left'):
                self.mower.execute(['L'])

                expect(self.mower.report()).to(equal(f'0 0 {WEST}'))

            with it('will face east when spinning right'):
                self.mower.execute(['R'])

                expect(self.mower.report()).to(equal(f'0 0 {EAST}'))

        with context('when facing west'):

            with before.each:
                self.mower = Mower.deploy(0, 0, WEST)

            with it('will face south when spinning left'):
                self.mower.execute(['L'])

                expect(self.mower.report()).to(equal(f'0 0 {SOUTH}'))

            with it('will face north when spinning right'):
                self.mower.execute(['R'])

                expect(self.mower.report()).to(equal(f'0 0 {NORTH}'))

        with context('when facing south'):

            with before.each:
                self.mower = Mower.deploy(0, 0, SOUTH)

            with it('will face east when spinning left'):
                self.mower.execute(['L'])

                expect(self.mower.report()).to(equal(f'0 0 {EAST}'))

            with it('will face west when spinning right'):
                self.mower.execute(['R'])

                expect(self.mower.report()).to(equal(f'0 0 {WEST}'))

        with context('when facing east'):

            with before.each:
                self.mower = Mower.deploy(0, 0, EAST)

            with it('will face north when spinning left'):
                self.mower.execute(['L'])

                expect(self.mower.report()).to(equal(f'0 0 {NORTH}'))

            with it('will face south when spinning right'):
                self.mower.execute(['R'])

                expect(self.mower.report()).to(equal(f'0 0 {SOUTH}'))

    with context('when moving forward'):
        with it('can move north'):
            mower = Mower.deploy(0, 0, NORTH)

            mower.execute(['M'])

            expect(mower.report()).to(equal(f'0 1 {NORTH}'))

        with it('can move east'):
            mower = Mower.deploy(0, 0, EAST)

            mower.execute(['M'])

            expect(mower.report()).to(equal(f'1 0 {EAST}'))

        with it('can move south'):
            mower = Mower.deploy(0, 1, SOUTH)

            mower.execute(['M'])

            expect(mower.report()).to(equal(f'0 0 {SOUTH}'))

        with it('can move west'):
            mower = Mower.deploy(1, 0, WEST)

            mower.execute(['M'])

            expect(mower.report()).to(equal(f'0 0 {WEST}'))

    with it('can execute multiple instructions'):
        mower = Mower.deploy(0, 0, NORTH)

        mower.execute(['M', 'M', 'R', 'M', 'M', 'L', 'M', 'L'])

        expect(mower.report()).to(equal(f'2 3 {WEST}'))

    with description('when going outside of the plateau'):
        with it('raises an error when asked to go beyond the limits to the north'):
            mower = Mower.deploy(0, 4, NORTH, 5, 5)

            expect(lambda: mower.execute(['M', 'M'])).to(raise_error(CannotGoOutOfThePlateauError))

        with it('raises an error when asked to go beyond the limits to the east'):
            mower = Mower.deploy(4, 0, EAST, 5, 5)

            expect(lambda: mower.execute(['M', 'M'])).to(raise_error(CannotGoOutOfThePlateauError))

        with it('raises an error when asked to go beyond the limits to the south'):
            mower = Mower.deploy(0, 1, SOUTH, 5, 5)

            expect(lambda: mower.execute(['M', 'M'])).to(raise_error(CannotGoOutOfThePlateauError))

        with it('raises an error when asked to go beyond the limits to the west'):
            mower = Mower.deploy(1, 0, WEST, 5, 5)

            expect(lambda: mower.execute(['M', 'M'])).to(raise_error(CannotGoOutOfThePlateauError))

        with it('stays in the last valid position'):
            mower = Mower.deploy(0, 4, NORTH, 5, 5)

            try:
                mower.execute(['M', 'M'])
            except CannotGoOutOfThePlateauError:
                pass

            expect(mower.report()).to(equal(f'0 5 {NORTH}'))
