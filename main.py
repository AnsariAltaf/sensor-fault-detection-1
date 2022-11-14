# from sensor.configuration.mongo_db_connection import MongoDBClient
# from sensor.logger import logging
# from sensor.exception import SensorException
# import os,sys
from sensor.pipeline.training_pipeline import TrainingPipeline

if __name__ == '__main__':

    # logging.info("Started program")
    # logging.info("Ended program")

    training_pipeline = TrainingPipeline()
    training_pipeline.run_pipeline()

