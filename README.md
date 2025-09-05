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

> !NOTE: If you are running the publisher & subscriber scripts in separate shells, you will need to activate the `venv` in each of those shells. There's probably a way to do this automagically for a `tmux` session or when within a specific directory. I should refresh that fuzzy recollection.

### store and query example

Install[^i] the Zenoh router (`zenohd`):
```

```
and start it with the configuration file from [the instructions][first-app]:
```
zenohd -c zenoh-myhome.json5
```

## build with `meson`
```
meson setup /tmp/build
meson compile -C /tmp/build
```
_____________
[zenoh]: https://zenoh.io
[first-app]: https://zenoh.io/docs/getting-started/first-app/
[install]: https://zenoh.io/docs/getting-started/installation/
_____________
[^i]: To install `zenohd`, adapt [the official instructions][install],
  summarized & scripted in `install-zenoh.debian.sh`.

