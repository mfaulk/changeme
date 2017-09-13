import argparse
from changeme import core
from core import cli_args
from copy import deepcopy
import logging
import mock



def reset_handlers():
    logger = logging.getLogger('changeme')
    logger.handlers = []

snmp_args = deepcopy(cli_args)
snmp_args['protocols'] = 'snmp'
snmp_args['name'] = 'apc'
snmp_args['target'] = '104.236.166.95' # demo.snmplabs.com
@mock.patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(**snmp_args))
def test_snmp(mock_args):
    reset_handlers()
    core.main()


