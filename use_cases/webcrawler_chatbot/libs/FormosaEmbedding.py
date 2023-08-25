import sys
from typing import Any, Dict, List, Mapping
import importlib
import requests

try:
    pydantic_v1 = importlib.import_module("pydantic.v1")
except ImportError:
    pydantic_v1 = importlib.import_module("pydantic")

if "pydantic_v1" not in sys.modules:
    # Use a conditional because langchain experimental
    # will use the same strategy to add pydantic_v1 to sys.modules
    # and may run prior to langchain core package.
    sys.modules["pydantic_v1"] = pydantic_v1

from pydantic_v1 import BaseModel, root_validator

from langchain.embeddings.base import Embeddings


class FormosaEmbedding(BaseModel, Embeddings):
    """Formosa Embedding service

    To use, you should have api key and endpoint from TWSC

    Example:
        .. code-block:: python

            from langchain.embeddings import FormosaEmbedding

            embeddings = FormosaEmbedding(endpoint_url="..", api_key="..")
    """

    client: Any  #: :meta private:
    model_name: str = "Formosa Embedding"
    endpoint_url: str = ""
    api_key: str = ""

    def __init__(self, **kwargs: Any):
        super().__init__(**kwargs)

    @property
    def _llm_type(self) -> str:
        return self.model_name

    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        '''Get the identifying parameters.'''

        return {
            **{"endpoint_url": self.endpoint_url},
            **self._default_params
        }

    def __str__(self):
        return self._llm_type

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        """Embed a list of documents using Formosa Embedding.

        Args:
            texts: The list of texts to embed.

        Returns:
            List of embeddings, one for each text.
        """
        
        embeddings = [self.embed_query(text) for text in texts]

        return [list(map(float, e)) for e in embeddings]

    def embed_query(self, text: str) -> List[float]:
        """Embed a query using Formosa Embedding.

        Args:
            text: The text to embed.

        Returns:
            Embeddings for the text.
        """
        headers = {
            'X-API-KEY': self.api_key,
            'Content-Type': 'application/json',
        }

        parameter_payload = {"input": [text]}

        # send request
        try:
            response = requests.post(
                self.endpoint_url, headers=headers, json=parameter_payload
            )
            if response.status_code != 200:
                return f'http error: {response.reason}'

        except requests.exceptions.RequestException as e:  # This is the correct syntax
            raise ValueError(f"Error raised by inference endpoint: {e}")

        embeddings = response.json()

        if embeddings.get('details') is not None:
            msg = embeddings['details']
            raise ValueError(
                f'Error raised by inference API: {msg}'
            )

        if embeddings.get('data') is None:
            return 'Response format error'

        
        return embeddings['data'][0]['embedding']