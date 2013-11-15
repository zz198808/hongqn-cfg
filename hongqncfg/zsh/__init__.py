from occupy import File, read


def apply():
    yield File("~hongqn/.zshrc",
               content=read(__name__, 'zshrc'),
               owner='hongqn')
