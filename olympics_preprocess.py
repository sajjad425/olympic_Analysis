#import pandas library
import pandas as pd

def preprocess(df, region_df):
    # Filter data to summer Olympics
    df = df[df['Season'] == "Summer"]

    # Merge athlete data with region data based on NOC
    df = df.merge(region_df, on='NOC', how='left')

    # Remove duplicate rows
    df.drop_duplicates(inplace=True)

    # Create one-hot encoded columns for medal types
    df = pd.concat([df, pd.get_dummies(df['Medal'])], axis=1)
    return df
