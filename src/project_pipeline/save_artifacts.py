from pathlib import Path
import pickle
import pandas as pd
import logging

logger = logging.getLogger(__name__)

def save_model(best_model, model_filename: Path):
    """
    Saves the best model to the specified path using pickle.

    Parameters:
        best_model: The model to be saved.
        model_filename (Path): The path (including filename) where the model should be saved.
    """

    # Make sure the parent directory is created
    model_filename.parent.mkdir(exist_ok=True, parents=True)  # Ensures all parent directories are created if necessary

    # Save the best model
    with open(model_filename, 'wb') as file:
        pickle.dump(best_model, file)
        logger.info("Saved the model artifact to path %s successfully!", model_filename)



def save_data(df: pd.DataFrame, data_file: Path):
    # make sure the parent directory is created
    data_file.parent.mkdir(exist_ok=True)

    # Save the best model
    df.to_pickle(data_file)
    logger.info("Save the artifacts %s to path %s successfully!", df, data_file)