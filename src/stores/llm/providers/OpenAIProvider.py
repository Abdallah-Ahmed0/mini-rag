from ..LLMinterface import LLMinterface
from openai import OpenAI

class OpenAIProvider(LLMinterface):

    def __init__(self, api_key: str, api_url: str=None,
                 default_input_max_characters: int=1000,
                 default_generation_max_output_tokens: int=1000,
                 default_generation_temperature: float=0.1):
        pass