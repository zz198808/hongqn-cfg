from . import zsh, ack, codecli, git, gentoo


def apply():
    yield zsh
    yield ack
    yield codecli
    yield git
    yield gentoo
