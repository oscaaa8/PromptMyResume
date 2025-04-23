from rewrite_engine import get_critique, rewrite_text

text = "Assisted in the lab with data collection and cleaning tasks."

critique = get_critique(text)
print("\n--- CRITIQUE ---")
print(critique["content"])
print("Model:", critique["model"])
print("Tokens:", critique["token_usage"])

rewrite = rewrite_text(text)
print("\n--- REWRITE ---")
print(rewrite["content"])
print("Model:", rewrite["model"])
print("Tokens:", rewrite["token_usage"])


# Function for printing the cost of using chat-gpt 3.5 turbo per request
def estimate_cost(token_usage):
    prompt_cost = token_usage["prompt_tokens"] * 0.001 / 1000
    completion_cost = token_usage["completion_tokens"] * 0.002 / 1000
    return round(prompt_cost + completion_cost, 6)

print("Estimated cost: $", estimate_cost(critique["token_usage"]))
