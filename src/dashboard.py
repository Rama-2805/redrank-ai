def get_dashboard_stats(df):

    return {
        "avg_score": round(df["score"].mean(), 2),
        "max_score": round(df["score"].max(), 2),
        "min_score": round(df["score"].min(), 2)
    }