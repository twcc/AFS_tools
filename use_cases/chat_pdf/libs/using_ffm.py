import dotenv
import os, sys
import re
dotenv.load_dotenv(dotenv.find_dotenv())

from libs.FormosaEmbedding import FormosaEmbedding
from libs.FormosaFoundationModel import FormosaFoundationModel
import re
from loguru import logger


def validating_ffm_host(endpoint_url):
    if re.match(r"https://5\d{4}\.(gai|afscloud)\.twcc\.ai", endpoint_url):
        return True
    raise Exception("Not valid FFM inference host: ", endpoint_url)
    
def get_ffm():
    ffm_host = os.getenv('AFS_CLOUD_FFM')
    ffm_model = os.getenv('FFM_MODEL_NAME')
    if validating_ffm_host(ffm_host):
        return FormosaFoundationModel(
            endpoint_url = ffm_host + "/text-generation/api/models/generate",
            max_new_tokens = 1024,
            temperature = 0.01,
            top_k = 50,
            top_p = 1.,
            frequence_penalty = 1.1,
            ffm_api_key = os.getenv('API_KEY_FFM'),
            model= ffm_model, # AFS Cloud
        )

def get_embed():
    return FormosaEmbedding(endpoint_url=os.getenv('AFS_CLOUD_EMBEDDING') + "/embeddings/api/embeddings",
                            api_key=os.getenv('API_KEY_EMBEDDING')
                            )


