actions = {
    'install_java_key': {
        'cascade_skip': False,
        'command': 'apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886',
        'unless': 'apt-key list | grep "EEA1 4886"',
        'needs': ['pkg_apt:dirmngr'],
    },
    'accept_java_license': {
        'command': 'echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections',
        'unless': 'debconf-show oracle-java8-installer | grep accepted-oracle-license-v1-1'
    }
}

pkg_apt = {
    'dirmngr': {
    },
    'oracle-java8-installer': {
        'needs': ['action:accept_java_license'],
        'cascade_skip': False
    }
}

files = {
    '/etc/apt/sources.list.d/webupd8team-java.list': {
        'source': "webupd8team-java.list",
        'content_type': "mako",
        'owner': "root",
        'group': "root",
        'mode': "0444",
        'needs': ['action:install_java_key'],
        'triggers': ['action:update_apt_cache']
    }
}
