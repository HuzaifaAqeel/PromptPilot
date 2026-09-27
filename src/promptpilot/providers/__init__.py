"""
Provider implementations for different AI backends.
Imports are lazy so that using one provider never requires the
heavy optional dependencies of the others.
"""

from .base import BaseProvider


def _lazy(name):
    if name == "openai":
        from .openai_provider import OpenAIProvider
        return OpenAIProvider
    if name == "claude":
        from .claude_provider import ClaudeProvider
        return ClaudeProvider
    if name == "llama":
        from .llama_provider import LlamaProvider
        return LlamaProvider
    if name == "hf":
        from .hf_provider import HFProvider
        return HFProvider
    if name == "gemini":
        from .gemini_provider import GeminiProvider
        return GeminiProvider
    raise ValueError(f"Unsupported provider: {name}")


def __getattr__(name):
    # allow `from promptpilot.providers import OpenAIProvider` etc.
    mapping = {
        "OpenAIProvider": "openai",
        "ClaudeProvider": "claude",
        "LlamaProvider": "llama",
        "HFProvider": "hf",
        "GeminiProvider": "gemini",
    }
    if name in mapping:
        return _lazy(mapping[name])
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def get_provider(provider_name: str = None, model: str = None) -> BaseProvider:
    """
    Get an instance of the specified provider.

    Args:
        provider_name: Name of the provider to use (openai, claude, llama, hf, gemini)
        model: Specific model to use with the provider

    Returns:
        An instance of the appropriate provider

    Raises:
        ValueError: If the provider name is not recognized
    """
    provider_name = provider_name.lower() if provider_name else 'openai'

    if provider_name == 'openai':
        return _lazy("openai")(model=model)
    elif provider_name == 'claude':
        return _lazy("claude")(model=model)
    elif provider_name == 'llama':
        return _lazy("llama")(model=model)
    elif provider_name == 'hf':
        return _lazy("hf")(model_name=model)
    elif provider_name == 'gemini':
        return _lazy("gemini")(model=model)
    else:
        raise ValueError(f"Unsupported provider: {provider_name}")


__all__ = ["BaseProvider", "OpenAIProvider", "ClaudeProvider", 'LlamaProvider', "HFProvider", "GeminiProvider", "get_provider"]
