from prediction_model.config import config
from prediction_model.processing.data_management import load_dataset, save_pipeline
import prediction_model.pipeline as pl


def run_training():
    """Train the model"""
    # Read Data
    train = load_dataset(config.TRAIN_FILE)
    # separating Loan_status in y
    y = train[config.TARGET].map({'N':0 , 'Y':1})
    pl.loan_pipe.fit(train[config.FEATURES], y)
    save_pipeline(pipeline_to_save=pl.loan_pipe)


if __name__ == '__main__':
    run_training()
