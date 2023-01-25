'''
In this file, we are freezing the requirements for our configuration file.

OR

We are defining the structure for our config file.
'''

from collections import namedtuple


# Data Ingestion Config:
DataIngestionConfig = namedtuple("DataIngestionConfig",
["dataset_download_url","tgz_download_dir","raw_data_dir","ingested_train_dir","ingested_test_dir"])


# Data Validation Config:
DataValidationConfig = namedtuple("DataValidationConfig",["schema_file_path"])


# Data Transformation Config:
DataTransformationConfig = namedtuple("DataTransformationConfig",
["add_bedroom_per_room","transformed_train_dir","transformed_dir","preprocessed_object_file_path"])


# Model Trainer Config:
ModelTrainerConfig = namedtuple("ModelTrainerConfig", 
["trained_model_file_path","base_accuracy","model_config_file_path"])


# Model Evaluation Config:
ModelEvaluationConfig = namedtuple("ModelEvaluationConfig", ["model_evaluation_file_path","time_stamp"])


# Model Pusher Config:
ModelPusherConfig = namedtuple("ModelPusherConfig", ["export_dir_path"])


# Training Pipeline Config:
TrainingPipelineConfig = namedtuple("TrainingPipelineConfig", ["artifact_dir"])
