from enum import Enum

from handles.platforms.bluesky import Bluesky
from handles.platforms.github import Github
from handles.platforms.instagram import Instagram
from handles.platforms.medium import Medium
from handles.platforms.npm import Npm
from handles.platforms.youtube import Youtube


class Platforms(Enum):
    BLUESKY = Bluesky
    GITHUB = Github
    INSTAGRAM = Instagram
    MEDIUM = Medium
    NPM = Npm
    YOUTUBE = Youtube
