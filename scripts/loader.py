import pandas as pd
import os

def load_news_data(filepath):
    """
    Loads the news dataset and converts the date column to datetime objects.
    
    Args:
        filepath (str): Path to the CSV file.
        
    Returns:
        pd.DataFrame: Processed DataFrame.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"The file {filepath} was not found.")
        
    print(f"Loading data from {filepath}...")
    df = pd.read_csv(filepath)
    

   
        
    return df