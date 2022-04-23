from mamba import (
    description,
    it
)

from expects import (
    expect,
    equal
)
from src.mow_lawn import mow_lawn


with description('Mow lawn service'):
    with it('runs a single lawn mower'):
        output = mow_lawn("""
5 5
1 2 N
LMLMLMLMM
""")
        expect(output).to(equal('1 3 N'))
