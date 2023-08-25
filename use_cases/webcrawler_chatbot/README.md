In this use case, web combines web crawling with Scrapy, data enhancement through FFM embeddings, and interactive user engagement using Streamlit and Langchain which integrated with FFM in [AFS Cloud](https://docs.twcc.ai/en/docs/user-guides/twcc/afs/afs-cloud). 


## Step 1: Generate Essential Dataset for Embedding

1. Open the "scrapy" folder.
2. Follow the instructions outlined in the "README.md" file located within the "scrapy" folder. This will guide you on how to generate the required dataset for embedding.

## Step 2: Install Required Packages

1. Open your command prompt or terminal.
2. Enter the command: `python -m pip install -r requirements.txt`
3. This command will install the necessary packages that are required for the process.

## Step 3: Update Parameters

1. Update the following parameters as needed:

    - Modify the `GENERATED_JSON_FILE_PATH` parameter to point to your JSON data file.
    - Update your AFS Cloud endpoint information in the ".env" file:
        - Set `AFS_CLOUD_EMBEDDING` to your embedding service's URL (e.g., https://203-145-216-185.ccs.twcc.ai:5xxx1).
        - Set `API_KEY_EMBEDDING` to your embedding service's API key (e.g., 853e8046-xxx-xxx-xxx-d8dcf0bcf025).
        - Set `AFS_CLOUD_FFM` to your FFM (Formosa Foundataion Model) service's URL in [AFS Cloud](https://docs.twcc.ai/en/docs/user-guides/twcc/afs/afs-cloud).
        - Set `API_KEY_FFM` to your FFM service's API key.
2. To test your embedding service, run: `python test_ffm.py`

## Step 4: Vectorize Website Dataset

1. Run the command: `python load_embedding_website.py`
2. This will initiate the process of creating vectors for the website dataset.
3. All generated vectors will be stored in the "embeddings/" folder.

## Step 5: Start API Server

1. Launch the API server using the command: `uvicorn chat_api_server:app --host 0.0.0.0 --port 8000`

## Step 6: Start Chat UI Server

Start the chat user interface server by running: `streamlit run chat_ui_server.py`

Following these steps will help you successfully complete the process, from generating essential dataset for embedding, updating parameters, vectorizing website data, to launching the API server and chat user interface server. Keep these instructions as a reference whenever needed.