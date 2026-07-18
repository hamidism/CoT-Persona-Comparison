from client import ask

PROBLEM = """A factory has two machines. Machine A can complete one production batch in 8 hours.
Machine B is 50% slower than Machine A.
If both machines start working together at the same time, how many hours will it take them to complete one batch together?"""


def run_plain():
    """RUN 1: Plain prompt — no reasoning instruction, no persona."""
    messages = [
        {"role": "user", "content": PROBLEM}
    ]
    return ask(messages)


def run_cot_persona():
    """RUN 2: Chain-of-Thought + Persona."""
    messages = [
        {"role": "system", "content": "You are a senior data analyst who is meticulous and precise with numbers."},
        {"role": "user", "content": PROBLEM + "\n\nThink step-by-step before giving your final answer."},
    ]
    return ask(messages)


if __name__ == "__main__":
    print("===== RUN 1: Plain Prompt (no persona, no CoT) =====")
    print(run_plain())

    print("\n===== RUN 2: CoT + Persona =====")
    print(run_cot_persona())
