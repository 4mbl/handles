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
    available_platforms = ', '.join([platform.name.lower() for platform in Platforms])

    parser = argparse.ArgumentParser(
        description='Check username availability across platforms.',
        formatter_class=lambda prog: argparse.HelpFormatter(prog, max_help_position=30),
    )
    parser.add_argument('username', type=str, help='The username to check')
    parser.add_argument(
        '--platforms',
        type=str,
        help=f'Comma-separated list of platforms to check (available: "*", {available_platforms})',
    )
    parser.add_argument('--file', type=str, help='File containing usernames to check')

    args = parser.parse_args(argv)
    usernames = [args.username]

    if args.file:
        usernames.extend(process_input(Path(args.file)))

    selected_platforms = []
    if args.platforms:
        requested_platforms = [p.strip().upper() for p in args.platforms.split(',')]
        for platform in requested_platforms:
            if '*' in requested_platforms:
                selected_platforms = list(Platforms)
                break
            if hasattr(Platforms, platform):
                selected_platforms.append(getattr(Platforms, platform))
            else:
                print(f'Warning: Platform "{platform}" is not supported.')

    for platform in selected_platforms:
        print(f'{platform.name.lower()} : {platform.value().are_available(usernames)}')

    raise SystemExit(0)
