actions = {
    'accept_java_license': {
        'command': 'echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | '
                   '/usr/bin/debconf-set-selections',
        'unless': 'debconf-show oracle-java8-installer | grep accepted-oracle-license-v1-1'
    }
}
files = {}

if node.has_bundle('apt'):
    # this is a ubuntu only repo, so wi install trusty on debain
    release = node.metadata.get('ubuntu', {}).get('release_name', 'trusty')

    files['/etc/apt/sources.list.d/webupd8team-java.list'] = {
        'content': f'deb http://ppa.launchpad.net/webupd8team/java/ubuntu {release} main\n',
        'content_type': 'text',
        'needs': ['file:/etc/apt/trusted.gpg.d/webupd8team-java.gpg', ],
        'triggers': ["action:force_update_apt_cache", ],
    }

    files['/etc/apt/trusted.gpg.d/webupd8team-java.gpg'] = {
        'content_type': 'binary',
    }

pkg_apt = {
    'oracle-java8-installer': {
        'needs': ['action:accept_java_license'],
        'cascade_skip': False
    }
}
