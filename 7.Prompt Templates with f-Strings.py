#Using Prompt Templates with f-Strings...

def generate_flexible_prompt(action, subject, tone):
    prompt = f"Write a {tone} {action} about {subject}."
    return prompt

# Example Inputs.
action = "Story"
subject = "The first Human on Mars"
tone = "Adventurous"

# Generate Prompt.
prompt = generate_flexible_prompt(action, subject, tone)
print("Generated Prompt:", prompt)
