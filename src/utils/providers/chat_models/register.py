from langchain_dev_utils.chat_models import register_model_provider


def register_all_model_providers():
    register_model_provider(
        provider_name="zai",
        chat_model="openai-compatible",
    )
