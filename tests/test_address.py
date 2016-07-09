import sys,os
from nose.tools. import *
current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(current_dir, '../indiesquare'))
from indiesquare.address import Address

try:
    import settings



def test_get_balance():
    a1 = Address()
#    ok_(isinstance(a1.get_balance('1965areciqapsuL2hsia2yKkRLfAsH1smG').get('')))

