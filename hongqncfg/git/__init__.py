from occupy import File, render, read


def apply():
    yield File('~hongqn/.gitconfig',
               content=render(__name__, 'gitconfig.mako'),
               owner='hongqn')
    yield File('~hongqn/.gitignore',
               content=read(__name__, 'gitignore'),
               owner='hongqn')
