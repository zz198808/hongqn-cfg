from occupy import File, read


def apply():
    yield File('/gentoo/etc/portage/make.conf',
               content=read(__name__, 'make.conf'),
               owner='hongqn')
    yield File('/gentoo/etc/portage/package.use/local',
               content=read(__name__, 'package.use'),
               owner='hongqn')
    yield File('/gentoo/etc/portage/package.mask/local',
               content=read(__name__, 'package.mask'),
               owner='hongqn')
