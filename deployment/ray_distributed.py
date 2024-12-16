import ray
import pandas as pd

ray.init()

@ray.remote
def process_chunk(chunk):
    # Perform data processing on a chunk
    chunk['processed'] = chunk['value'] * 1.1
    return chunk

if __name__ == "__main__":
    # Load large dataset
    df = pd.read_csv("large_dataset.csv")

    # Split data into chunks
    chunks = np.array_split(df, 10)

    # Process chunks in parallel
    results = ray.get([process_chunk.remote(chunk) for chunk in chunks])

    # Combine results
    processed_df = pd.concat(results)
    processed_df.to_csv("processed_large_dataset.csv", index=False)
    print("Processing complete.")
