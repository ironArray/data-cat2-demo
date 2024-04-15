# Caterva2 demo data

This repository contains the data files (roots and datasets) used to deploy a Caterva2 demo site, but they may be used independently.

## How data was generated

**Note:** These instructions are not needed to use the data, only to re-generate it.

First, make sure that the `caterva2` submodule is cloned and up-to-date:

```sh
git submodule update --init --recursive caterva2
```

Then, install Caterva2 in a Python virtual environment:

```sh
test -d venv || python3 -m venv venv
(. venv/bin/activate && pip install -e ./caterva2[services,hdf5,blosc2-plugins] \
 && pip install pillow)
```

**Note:** If you want to update the version of Caterva2, update the `caterva2` submodule, update the virtual environment (see above), re-generate data files and commit the changes.

### Caterva2 directory root (`root-example`)

```sh
venv/bin/python -m caterva2.services.dirroot root-example.new \
&& (. venv/bin/activate && python scripts/lung_b2nd.py 10 root-example.new/lung-jpeg2000_10x.b2nd) \
&& mv root-example root-example.old && mv root-example.new root-example
```

### HDF5 root (`hdf5root-example.h5`)

```sh
venv/bin/python -m caterva2.services.hdf5root hdf5root-example.new.h5 \
&& mv hdf5root-example.new.h5 hdf5root-example.h5
```

### JPEG 2000 numbers HDF5 root (`numbers-jpeg2000.h5`)

```sh
(. venv/bin/activate && cd caterva2/test-images && python encode-grok-numbers.py) \
&& mv caterva2/test-images/numbers-jpeg2000.h5 numbers-jpeg2000.new.h5 \
&& mv numbers-jpeg2000.new.h5 numbers-jpeg2000.h5
```

### JPEG 2000 lung tomography HDF5 root (`lung-jpeg2000.h5`)

```sh
(. venv/bin/activate && python scripts/lung_hdf5.py lung-jpeg2000.new.h5) \
&& mv lung-jpeg2000.new.h5 lung-jpeg2000.h5
```
