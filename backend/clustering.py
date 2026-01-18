import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN

def detect_hotspots(csv_path):
    df = pd.read_csv(csv_path) #full_data

    coords = df[['lat', 'lng']].values

    model = DBSCAN(
        eps=0.0015,     # distance threshold (~150m)
        min_samples=3
    )

    df['cluster'] = model.fit_predict(coords)

    # -1 means noise (safe-ish)
    hotspots = df[df['cluster'] != -1] #hotspots

    return hotspots, df
