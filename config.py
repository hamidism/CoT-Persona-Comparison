import os

# Put your real key in an environment variable — never hardcode it here
# (yaad hai push-protection wala scene? isliye os.environ use karo)
API_KEY = os.environ.get("OPENROUTER_API_KEY", "YOUR_OPENROUTER_API_KEY")
MODEL = "openai/gpt-4o-mini"  # same model jo Nova ke liye use kiya tha, ya jo bhi available ho
API_URL = "https://openrouter.ai/api/v1/chat/completions"