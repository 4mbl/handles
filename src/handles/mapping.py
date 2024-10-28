from enum import Enum

from handles.platforms.github import Github
from handles.platforms.instagram import Instagram
from handles.platforms.medium import Medium
from handles.platforms.npm import Npm
from handles.platforms.twitter import Twitter


class Platforms(Enum):
    GITHUB = Github
    INSTAGRAM = Instagram
    MEDIUM = Medium
    NPM = Npm
    TWITTER = Twitter
