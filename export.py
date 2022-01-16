#!/usr/bin/env python3

import argparse
import os
from xml.etree import ElementTree as ET
import shutil


def paths_from_xml(xml_data: str):
    # https://en.wikipedia.org/wiki/XML_Shareable_Playlist_Format
    NS = {'xspf': "http://xspf.org/ns/0/"}
    ET.register_namespace('', NS['xspf'])

    # parse xml (playlist -> trackList -> track -> location
    root = ET.fromstring(xml_data)
    tracklist = root.find("xspf:trackList", NS)
    all_paths = [track.find('xspf:location', NS).text for track in tracklist]
    return all_paths


def _mkdir(dest_dir: str, dry_run: bool) -> None:
    if dry_run:
        return
    try:
        os.mkdir(dest_dir)
    except FileExistsError:
        pass


def _copy(file: str, dest_dir: str, dry_run: bool) -> None:
    if dry_run:
        print(f'[Dry Run] copy {file} to {dest_dir}')
    else:
        print(f'Copy {file} to {dest_dir}')
        shutil.copy2(file, dest_dir)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Export music from an xspf type playlist to a directory.')
    parser.add_argument('--playlist', help='path to xspf type playlist.',
                        dest='playlist', type=str, required=True)
    parser.add_argument('--dest_dir', help='directory to copy the music to.',
                        dest='dest_dir', type=str, required=True)
    parser.add_argument('--dry-run', help='do not perform an actual copy.',
                        dest='dry_run', action='store_true', default=False)
    args = parser.parse_args()

    # get list of paths to music files
    with open(args.playlist, 'r') as f:
        paths = paths_from_xml(f.read())

    # create dest directory
    _mkdir(args.dest_dir, args.dry_run)

    # copy to dest directory
    list(map(lambda x: _copy(x, args.dest_dir, args.dry_run), paths))
