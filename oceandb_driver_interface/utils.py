import configparser
import argparse
import sys
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
    except:
        pass


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
        except:
            print("exception on %s!" % option)
            plugin_config[option] = None
    return plugin_config


def start_plugin(file_path):
    """This function initialize the Ocean plugin"""
    try:
        args = parse_args()
        if args is not None:
            if args.config is not None:
                config = parse_config(args.config)
            else:
                config = parse_config(file_path)
        else:
            config = parse_config(file_path)
    except:
        raise ConfigError("You should provide a valid config.")
    plugin_instance = load_plugin(config)
    return plugin_instance(config)


def load_plugin(config):
    module = config['module']
    try:
        if 'module.path' in config:
            module_path = config['module.path']
        else:
            module_path = "../plugins/%s/plugin.py" % module
    except:
        raise ConfigError("You should provide a valid config.")
    if sys.version_info < (3,5):
        from importlib.machinery import SourceFileLoader

        foo = SourceFileLoader("plugin.py", module_path).load_module()
        return foo.Plugin
    else:
        spec = importlib.util.spec_from_file_location("plugin.py", module_path)
        foo = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(foo)
        return foo.Plugin


def print_help():
    """Print the default help in stdout"""
    pass
