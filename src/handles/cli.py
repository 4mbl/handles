# flake8: noqa: T201
from __future__ import annotations

import argparse
import os
from pathlib import Path

from handles.platforms.enum import Platforms

DEFAULT_INPUT_DIR = Path(Path(__file__).parent, 'secret')


def process_input(input_dir: Path = DEFAULT_INPUT_DIR) -> list[str]:
    usernames = []
    for file_name in os.listdir(input_dir):
        with Path(input_dir, file_name).open() as f:
            for line in f:
                if line == '\n':
                    continue
                if file_name.endswith('.txt'):
                    usernames.append(line.strip())
                elif file_name.endswith('.csv'):
                    usernames.append(line.split(';')[0].rstrip())
    return usernames


def cli(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description='Check username availability across platforms.')
    parser.add_argument('username', type=str, help='The username to check')
    parser.add_argument('--github', action='store_true', help='Check on GitHub')
    parser.add_argument('--instagram', action='store_true', help='Check on Instagram')
    parser.add_argument('--medium', action='store_true', help='Check on Medium')
    parser.add_argument('--npm', action='store_true', help='Check on npm')
    parser.add_argument('--file', type=str, help='File containing usernames to check')

    args = parser.parse_args(argv)
    usernames = [args.username]

    if args.file:
        usernames.extend(process_input(Path(args.file)))

    selected_platforms = []
    if args.github:
        selected_platforms.append(Platforms.GITHUB)
    if args.instagram:
        selected_platforms.append(Platforms.INSTAGRAM)
    if args.medium:
        selected_platforms.append(Platforms.MEDIUM)
    if args.npm:
        selected_platforms.append(Platforms.NPM)

    for platform in selected_platforms:
        print(f'{platform.name.lower()} : {platform.value().are_available(usernames)}')

    raise SystemExit(0)
