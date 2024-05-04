import argparse
import yaml


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ant_config_path", required=True, type=str)
    parser.add_argument("--plotting_config_path", required=True, type=str)
    args = parser.parse_args()
    return args


def load_yaml_file_to_json(path):
    with open(path, "r") as stream:
        return yaml.safe_load(stream)

