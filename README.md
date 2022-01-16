## Overview

[![CI](https://github.com/dgoel/export_music/actions/workflows/ci.yml/badge.svg)](https://github.com/dgoel/export_music/actions/workflows/ci.yml)

Python3 script `export.py` to export music from an [XSPF](https://www.xspf.org/) compatible playlist to a directory.

## Usage
```shell
$ ./export.py --playlist /path/to/playlist.xspf --dest_dir /path/to/dest/dir [--dry-run]
```

## Unit Test
```shell
$ python -m pytest export.py
```
