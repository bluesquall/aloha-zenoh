# aloha-zenoh

A learning repository for [Zenoh][zenoh].

## python examples

### virtual environment
First, activate a virtual environment and install the Zenoh library for Python:
```
pushd py # Let's keep the python examples in a separate directory.
python3 -m venv .venv # N.B. The path .venv is excluded by .gitignore
source .venv/bin/activate
pip install eclipse-zenoh
```

### publish & subscribe example
Follow along with [the official `first-app` instructions][first-app].


## build with `meson`
```
meson setup /tmp/build
meson compile -C /tmp/build
```
_____________
[zenoh]: https://zenoh.io
[first-app]: https://zenoh.io/docs/getting-started/first-app/

_____________
