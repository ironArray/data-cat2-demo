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
(. venv/bin/activate && pip install -e ./caterva2[services,hdf5,blosc2-plugins])
```

TODO
