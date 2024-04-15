# Caterva2 demo data

This repository contains the data files (roots and datasets) used to deploy a Caterva2 demo site, but they may be used independently.

## How data was generated

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

### Caterva2 directory root (root-example)

```sh
venv/bin/python -m caterva2.services.dirroot root-example \
&& (. venv/bin/activate && python lung_b2nd.py 10 root-example/lung-jpeg2000_10x.b2nd)
```

### HDF5 root (hdf5root-example)

```sh
venv/bin/python -m caterva2.services.hdf5root hdf5root-example.h5
```

### JPEG 2000 numbers HDF5 root (numbers-jpeg2000)

```sh
(. venv/bin/activate && cd caterva2/test-images && python encode-grok-numbers.py) \
 && mv caterva2/test-images/numbers-jpeg2000.h5 numbers-jpeg2000.h5
```

### JPEG 2000 lung tomography HDF5 root (lung-jpeg2000)

```sh
(. venv/bin/activate && python lung_hdf5.py lung-jpeg2000.h5)
```

TODO
