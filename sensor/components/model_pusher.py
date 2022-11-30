from sensor.exception import SensorException
from sensor.logger import logging
from sensor.entity.artifact_entity import DataValidationArtifact,ModelTrainerArtifact,ModelEvaluationArtifact,ModelPusherArtifact
from sensor.entity.config_entity import ModelEvaluationConfig,ModelPusherConfig
import os,sys,shutil
from sensor.ml.metric.classification_metric import get_classification_score
from sensor.ml.model.estimator import SensorModel
from sensor.utils.main_utils import save_object,load_object,write_yaml_file
from sensor.ml.model.estimator import ModelResolver

class ModelPusher:
    
    def __init__(self,model_eval_artifact:ModelEvaluationArtifact,
                 model_pusher_config:ModelPusherConfig):
        try:
            self.model_pusher_config = model_pusher_config
            self.model_eval_artifact = model_eval_artifact
        except Exception as e:
            raise SensorException(e,sys)

        
    def initiate_model_pusher(self,)->ModelPusherArtifact:
        
        '''
        Here we are trying to save the model in 2 directories.
        Make directory and save the file
        '''
        try:
            trained_model_path=self.model_eval_artifact.trained_model_path
           
            # creating model directory          
            model_file_path=self.model_pusher_config.model_file_path
            
            os.makedirs(os.path.dirname(model_file_path),exist_ok=True)
            shutil.copy(src=trained_model_path,dst=model_file_path)
            
            # Saved Model directory
            saved_model_path=self.model_pusher_config.saved_model_path
            os.makedirs(os.path.dirname(saved_model_path),exist_ok=True)
            shutil.copy(src=trained_model_path,dst=saved_model_path)
            
            # Prepare Artifact 
            
            model_pusher_artifact=ModelPusherArtifact(saved_model_path=saved_model_path, model_path=model_file_path)
            return model_pusher_artifact
        except Exception as e:
            raise SensorException(e,sys)
                