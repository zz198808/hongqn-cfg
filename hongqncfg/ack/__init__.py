from occupy import File, Package, read


def apply():
    yield File("~hongqn/.ackrc",
               content=read(__name__, 'ackrc'))
    yield Package('sys-apps/ack')
