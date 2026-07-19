<div align="center">
<img src="./banner.png" width="140" height="140" style="border-radius:50%; object-fit:cover;" alt="NeuroFive Solutions"/>

# Chain-of-Thought + Persona Prompting — Before/After Comparison

A small experiment tool that proves out a core prompt engineering technique: combining **Chain-of-Thought (CoT)** instructions with **persona/role prompting** and comparing the result against a plain, direct prompt — for the same reasoning problem, run through the same model.

## The Idea

- **Control (Plain Prompt):** the question is sent to the model with no reasoning instruction and no persona.
- **Treatment (CoT + Persona):** the same question is sent with a system-level persona (e.g. *"You are a senior financial analyst"*) and an added instruction to *"think step-by-step before answering."*

Both responses are captured side by side so correctness and clarity can be compared directly.

## Tech Stack

- Python
- Flask
- OpenRouter API (`openai/gpt-4o-mini`)

## Project Structure

```
.
├── app.py              # Flask server + /api/compare endpoint
├── client.py            # Handles the API call to OpenRouter
├── config.py             # Model + API key configuration
├── main.py                # CLI version — runs both prompts and prints results
├── templates/
│   └── index.html          # Chat-style interface for live comparison
└── .gitignore
```

## Setup

1. Install dependencies:
   ```
   pip install flask requests
   ```

2. Set your OpenRouter API key as an environment variable (never hardcode it):
   ```
   $env:OPENROUTER_API_KEY="your_key_here"        # PowerShell
   export OPENROUTER_API_KEY="your_key_here"      # macOS/Linux
   ```

3. Run the web interface:
   ```
   py app.py
   ```
   Then open **http://127.0.0.1:5000** in your browser.

   Or run the CLI version for a single fixed comparison:
   ```
   py main.py
   ```

## Using the Interface

The page includes a few preset reasoning questions (a rate/work problem, a sunk-cost business decision, a classic math riddle, and a logic puzzle) that can be run with one click. A free-text input is also available to test any custom reasoning question — each submission logs a new entry showing the Control (plain) and Treatment (CoT + persona) answers side by side.

## Findings

Testing across a few problem types showed that the effect of CoT + persona prompting depends heavily on the problem:

- On a straightforward rate/work problem, both prompting styles reached the correct answer, since the model already applies step-by-step reasoning internally for familiar problem types. The main difference was in precision — the plain prompt used exact fractions, while the CoT + persona run relied on decimal approximations.
- On a business decision scenario involving a **sunk cost trap**, the framing of the question mattered more than the prompting style, since the correct answer requires explicitly disregarding an already-spent cost that a fast, unstructured answer is more likely to fold back into the decision.

The overall takeaway: CoT + persona prompting is not a guaranteed win in every case — its impact is most visible on problems that are ambiguous, prone to a plausible-but-wrong shortcut answer, or fall outside a model's well-trained patterns. On simpler or highly familiar problems, a strong model may already reason carefully without being asked to.

## Security Note

API keys are read from an environment variable via `os.environ.get()` and are never hardcoded in the source. A `.gitignore` excludes `.env` files and virtual environments from version control.
