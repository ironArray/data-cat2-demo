import sys
import blosc2 as b2
import blosc2_grok as b2g
import numpy

cratio, out = sys.argv[1:]; cratio = int(cratio)

bi = b2.open('source-data/lung_raw_slice.b2nd')
cs = (1, *bi.shape[1:])

b2g.set_params_defaults(
    cod_format=b2g.GrkFileFmt.GRK_FMT_JP2,
    quality_mode='rates', quality_layers=numpy.array([cratio], dtype='f8'))

cp = dict(codec=b2.Codec.GROK, filters=[], splitmode=b2.SplitMode.NEVER_SPLIT)
bo = bi.copy(urlpath=out, chunks=cs, blocks=cs, cparams=cp)
