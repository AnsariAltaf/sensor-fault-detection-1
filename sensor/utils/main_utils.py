import yaml
from sensor import SensorException
from sensor.logger import logging
import os,sys

def read_yaml_file(file_path:str)->dict:
    try:
        pass
    except Exception as e:
        raise SensorException(e,sys)

    
    with open(file_path,'rb') as yaml_file:
        return yaml.safe_load(yaml_file)


def write_yaml_file(file_path:str,content:object,replace=False):
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path),exist_ok=True)
        with open(file_path,'w') as file:
            yaml.dump(content,file)

    except Exception as e:
        raise SensorException(e,sys)
