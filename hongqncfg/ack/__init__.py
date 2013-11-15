from occupy import File, Package, read


def apply():
    yield File("~hongqn/.ackrc",
               content=read(__name__, 'ackrc'),
               owner='hongqn',
               )
    yield Package('sys-apps/ack')
