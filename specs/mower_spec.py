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

with description('Seat Mower'):
    with context('when deploying the mower'):
        with it('can be faced north'):
            mower = Mower.deploy(NORTH)

            expect(mower.report()).to(equal(NORTH))
