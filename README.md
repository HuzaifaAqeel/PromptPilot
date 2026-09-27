# 🧭 PromptPilot (with Gemini support)

A fast, lightweight Python library and CLI tool for **versioning, testing, and optimizing AI prompts** across multiple providers — now with a native **Gemini** provider.

> **Attribution:** This project is based on [doganarif/promptpilot](https://github.com/doganarif/promptpilot) (MIT License). I added Gemini as a first-class provider and made provider imports lazy.

## What it does

- 📝 Version your prompts and track every change
- 🧪 A/B test the same prompt across providers (Gemini, Claude, OpenAI, HuggingFace, Llama…)
- 💻 Simple CLI: `promptpilot init`, `promptpilot run`, `promptpilot versions`

## What changed from the original

- Added a **native Gemini provider** via the `google-genai` SDK — works with `GOOGLE_API_KEY`/`GEMINI_API_KEY` and a configurable model
- Made provider imports **lazy**, so using Gemini doesn't require installing torch/transformers
- Extended the CLI docs and options for the Gemini provider

## Quick start

```bash
pip install -e .
export GOOGLE_API_KEY=your-key-here
promptpilot init my-prompt --provider gemini
promptpilot run my-prompt
```

## License

MIT — see [LICENSE.md](LICENSE.md) (original license by Arif Doğan, preserved).
