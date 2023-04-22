import chromadb

def main():
    client = chromadb.Client()

    collection = client.create_collection("example_collection")

    collection.add(
        documents=[
            "This is a document about squirrels",
            "This is a document about dogs",
            "This is a document about cats",
            "This is a document about quantum physics",
        ],
        metadatas=[
            {"animal": "squirrel"},
            {"animal": "dog"},
            {"animal": "cat"},
            {"animal": "cat"},
        ],
        ids=["squirrel", "dog", "cat", "quantum"],
    )

    results = collection.query(
        query_texts=["physics"],
        n_results=4,
    )

    print(results)
if __name__ == "__main__":
    main()