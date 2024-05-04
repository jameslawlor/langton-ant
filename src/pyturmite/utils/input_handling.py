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


class Config:
    def __init__(self):
        input_args = parse_args()
        self.ant_config_path = input_args.ant_config_path
        self.plotting_config_path = input_args.plotting_config_path

        self.instructions = None
        self.ruleset = ""
        self.padding_size = 0
        self.canvas_size = 0
        self.cmap = ""
        self.plot_mode = ""
        self.n_steps = 0
        self.animation_interval = 0
        self.frame_skip = 0
        self.save_animation = False

    def __str__(self):
        return str(vars(self))

    def _set_attributes_from_dictionary(self, dictionary):
        for k, v in dictionary.items():
            setattr(self, k, v)

    def _load_config_from_path(self, path):
        raw_config = load_yaml_file_to_json(path)
        self._set_attributes_from_dictionary(raw_config)

    def load(self):
        self._load_config_from_path(self.ant_config_path)
        self._load_config_from_path(self.plotting_config_path)
