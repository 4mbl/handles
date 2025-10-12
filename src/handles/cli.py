# flake8: noqa: T201
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any

from handles.mapping import Platforms

DEFAULT_INPUT_DIR = Path(Path.cwd(), 'input.txt')

YES_CHAR = '✔️'
NO_CHAR = '❌'


def process_input(input_file: Path = DEFAULT_INPUT_DIR) -> list[str]:
    usernames = []
    with Path(input_file).open() as f:
        for line in f:
            if line == '\n':
                continue
            if input_file.as_posix().endswith('.csv'):
                usernames.append(line.split(';')[0].rstrip())
            else:
                usernames.append(line.strip())
    return usernames


def check_availability(platform: Platforms, usernames: list[str]) -> list[tuple[str, str]]:
    results: list[tuple[str, str]] = []
    for username in usernames:
        result = YES_CHAR if platform.value().is_available(username) else NO_CHAR
        results.append((username, result))
    return results


def cli(argv: list[str] | None = None) -> None:  # noqa: C901, PLR0912
    available_platforms = ', '.join([platform.name.lower() for platform in Platforms])

    parser = argparse.ArgumentParser(
        description='Check username availability across platforms.',
        formatter_class=lambda prog: argparse.HelpFormatter(prog, max_help_position=30),
    )
    parser.add_argument('username', type=str, help='The username to check', nargs='?')

    parser.add_argument('--file', type=str, help='File containing usernames to check')

    parser.add_argument(
        '--platforms',
        type=str,
        help=f'Comma-separated list of platforms to check (available: "*", {available_platforms}).',
        default='*',
    )

    args = parser.parse_args(argv)

    if not args.username and not args.file:
        parser.error('You must provide either a username or a file with usernames.')
    if args.username and args.file:
        parser.error('You cannot provide both a username and a file with usernames.')

    usernames = []
    if args.username:
        usernames.append(args.username)

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

    name_width = max(len(p.name) for p in selected_platforms) + 2
    results_dict: dict[str, Any] = {platform.name.lower(): [] for platform in selected_platforms}

    with ThreadPoolExecutor() as executor:
        future_to_platform = {
            executor.submit(check_availability, platform, usernames): platform
            for platform in selected_platforms
        }
        for future in as_completed(future_to_platform):
            platform = future_to_platform[future]
            try:
                results = future.result()
                results_dict[platform.name.lower()] = results
            except Exception as exc:  # noqa: BLE001
                print(f'Platform {platform.name} generated an exception: {exc}')

    for platform, results in results_dict.items():
        for username, result in results:
            print(f'{platform:<{name_width}} : {username} {result}')

    raise SystemExit(0)
