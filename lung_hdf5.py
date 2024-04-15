from subprocess import call
import sys, tempfile
from caterva2.tools.cat2_to_hdf5 import export

out = sys.argv[1]

with tempfile.TemporaryDirectory() as tmp:
    for cr in [2, 5, 10, 20, 30]:
        call([sys.executable, 'lung_b2nd.py', str(cr), f'{tmp}/lung_{cr}x.b2nd'])
    export(tmp, out)
