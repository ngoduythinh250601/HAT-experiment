from basicsr.models import build_model
from basicsr.utils.options import dict2str, parse_options
from basicsr.utils.img_util import img2tensor, tensor2img
import yaml
from collections import OrderedDict 
from hat.models.hat_model import HATModel
import os.path as osp

def ordered_yaml():
    """Support OrderedDict for yaml.

    Returns:
        yaml Loader and Dumper.
    """
    try:
        from yaml import CDumper as Dumper
        from yaml import CLoader as Loader
    except ImportError:
        from yaml import Dumper, Loader

    _mapping_tag = yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG

    def dict_representer(dumper, data):
        return dumper.represent_dict(data.items())

    def dict_constructor(loader, node):
        return OrderedDict(loader.construct_pairs(node))

    Dumper.add_representer(OrderedDict, dict_representer)
    Loader.add_constructor(_mapping_tag, dict_constructor)
    return Loader, Dumper

class Model:
    def __init__(self, yml_dir):
        with open(osp.abspath(yml_dir), mode='r') as f:
            self.opt = yaml.load(f, Loader=ordered_yaml()[0])
        self.load()

    def load(self):
        self.model = HATModel(self.opt)
    
    def process(self, cv2_image):
        img = img2tensor(cv2_image)
        img = img.unsqueeze(0)
        data = dict()
        data['lq'] = img
        self.model.feed_data(data)
        self.model.pre_process()
        self.model.process()
        self.model.post_process()
        visuals = self.model.get_current_visuals()
        sr_img = tensor2img([visuals['result']])
        return sr_img


if __name__ == '__main__':
    models = Model()