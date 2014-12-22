"""Xtrabackup script

Usage:
    pyxtrabackup <repository> --user=<user> [--password=<pwd>] [--tmp-dir=<tmp>] [--log-file=<log>] [--backup-threads=<threads>] 
    pyxtrabackup (-h | --help)
    pyxtrabackup --version


Options:
    -h --help                   Show this screen.
    --version                   Show version.
    --user=<user>               MySQL user.
    --password=<pwd>            MySQL password.
    --tmp-dir=<tmp>             Temporart directory [default: /tmp].
    --log-file=<log>            Log file [default: /var/log/pyxtrabackup.log].
    --backup-threads=<threads>  Threads count [default: 1].

"""
from docopt import docopt
import sys
import logging
from xtrabackup.backup_tools import BackupTool


def main():
    arguments = docopt(__doc__, version='1.0')
    backup_tool = BackupTool(arguments['--log-file'])
    try:
        backup_tool.start_full_backup(arguments['<repository>'],
                                      arguments['--tmp-dir'],
                                      arguments['--user'],
                                      arguments['--password'],
                                      arguments['--backup-threads'])
    except Exception:
        logger = logging.getLogger(__name__)
        logger.error("An error occured during the backup process.", exc_info=True)
        exit(1)
    exit(0)


if __name__ == '__main__':
    sys.exit(main())
