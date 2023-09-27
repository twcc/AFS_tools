import dotenv
import os
dotenv.load_dotenv(dotenv.find_dotenv())

from libs.FormosaEmbedding import FormosaEmbedding
from libs.FormosaFoundationModel import FormosaFoundationModel


def get_ffm():
    return FormosaFoundationModel(
        endpoint_url = os.getenv('ENDPOINT_FFM'),
        max_new_tokens = 1024,
        temperature = 0.01,
        top_k = 50,
        top_p = 1.,
        frequence_penalty = 1.1,
        ffm_api_key = os.getenv('API_KEY_FFM'),
        model= os.getenv('FFM_MODEL_NAME'), # AFS Cloud
    )

def get_embed():
    return FormosaEmbedding(endpoint_url=os.getenv('ENDPOINT_EMBEDDING'),
                            api_key=os.getenv('API_KEY_EMBEDDING')
                            )


