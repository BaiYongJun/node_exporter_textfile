import subprocess


def get_node_info(self):
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
    serial = subprocess.check_output(*cmd)
    hostname = subprocess.check_output(('hostname'))
    {
        'os': version_dict['NAME'],
        'version': version_dict['VERSION_ID'],
        'serial': serial.strip()
    }
    print '# HELP example_metric Metric read from /some/path/textfile/example.prom'
    print '# TYPE example_metric untyped'

if __name__ == "__main__":
    get_node_info()
