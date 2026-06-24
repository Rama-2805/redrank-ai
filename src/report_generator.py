import pandas as pd

def generate_report(df):

    file_name = "hiring_report.csv"

    report_df = df.copy()

    report_df.to_csv(
        file_name,
        index=False
    )

    return file_name