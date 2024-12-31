import openai

# Set your OpenAI API key
openai.api_key = "your-api-key-here"

# Make a simple API call
response = openai.Completion.create(
    engine="text-davinci-003",  # Choose an engine, e.g., "text-davinci-003"
    prompt="Say Hello, World!",
    max_tokens=10  # Limit the response length
)

# Print the response
print(response.choices[0].text.strip())