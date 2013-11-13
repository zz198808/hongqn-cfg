from occupy import File, render, read


def apply():
    yield File('~hongqn/.gitconfig', content=render(__name__, 'gitconfig.mako'))
    yield File('~hongqn/.gitignore', content=read(__name__, 'gitignore'))
