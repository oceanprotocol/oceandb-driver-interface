import configparser
import argparse
import sys
import os
import site
import importlib.util
import importlib.machinery
from oceandb_driver_interface.constants import CONFIG_OPTION
from oceandb_driver_interface.exceptions import ConfigError


def parse_args():
    """Parse command line arguments given to the agent"""
    parser = argparse.ArgumentParser(description="OceanDB Plugin System")
    parser.add_argument('--config', metavar='path', required=False,
                        help='path to the oceandb_plugin_sysyem.ini file')
    try:
        args = parser.parse_args()
        return args
    except Exception:
        raise Exception("There was a problem parsing the configuration.")


def parse_config(file_path):
    """Loads the configuration file given as parameter"""
    config_parser = configparser.ConfigParser()
    config_parser.read(file_path)
    plugin_config = {}
    options = config_parser.options(CONFIG_OPTION)
    for option in options:
        try:
            plugin_config[option] = config_parser.get(CONFIG_OPTION, option)
            if plugin_config[option] == -1:
                print("skip: %s" % option)
        except Exception as e:
            print("exception on %s!" % option)
            print(e.message)
            plugin_config[option] = None
    return plugin_config


def start_plugin(file_path):
    """This function initialize the Ocean plugin"""
    try:
        args = parse_args()
        if (args is None or args.config is None) and not file_path:
            raise Exception('Configuration file is required to load the BigchainDB plugin')
        if not file_path:
            file_path = args.config
        config = parse_config(file_path)
    except Exception:
        raise ConfigError("You should provide a valid config.")
    plugin_instance = load_plugin(config)
    return plugin_instance(config)


def load_plugin(config):
    module = config['module']
    try:
        if 'module.path' in config:
            module_path = config['module.path']
        elif os.getenv('VIRTUAL_ENV') is not None:
            module_path = "%s/lib/python3.%s/site-packages/oceandb_%s_driver/plugin.py" % (
                os.getenv('VIRTUAL_ENV'), sys.version_info[1], module)
        else:
            module_path = "%s/oceandb_%s_driver/plugin.py" % (
                site.getsitepackages()[0], module)
    except Exception:
        raise ConfigError("You should provide a valid config.")
    if sys.version_info < (3, 5):
        from importlib.machinery import SourceFileLoader

        mod = SourceFileLoader("plugin.py", module_path).load_module()
        return mod.Plugin
    else:
        spec = importlib.util.spec_from_file_location("plugin.py", module_path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod.Plugin


def print_help():
    """Print the default help in stdout"""
    pass
