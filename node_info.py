import subprocess


def get_node_info():
    """Get node system os version and serial."""
    version_dict = {}
    with open('/etc/os-release') as f:
        for line in f.readlines():
            if '=' not in line:
                continue
            key = line.split('=')[0]
            value = line.split('=')[1].strip().replace('\"', '')
            version_dict[key] = value
    cmd = ('dmidecode', '-s', 'system-serial-number')
    serial = subprocess.check_output(cmd)
    hostname = subprocess.check_output(('hostname'))

    print '# HELP example_metric Metric'
    print '# TYPE example_metric'
    metric = 'node_info{serial="%s", os_family="%s", os_version="%s",' + \
        'hostname="%s"}'
    print(metric % (serial.strip(), version_dict['NAME'],
                    version_dict['VERSION_ID'], hostname.strip()))


if __name__ == "__main__":
    get_node_info()
