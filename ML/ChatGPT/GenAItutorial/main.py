# Step 1: Install Required Libraries
# Step 2: Import Libraries and Load GPT-2
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load the pre-trained GPT-2 model and tokenizer from Hugging Face
model_name = "gpt2-medium"  # You can also use "gpt2-medium", "gpt2-large", etc. for larger models
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Set the model to evaluation mode
model.eval()


# Step 3: Generate Text
# Function to generate text based on a given prompt
def generate_text(prompt, max_length=100):
    # Tokenize the input prompt
    inputs = tokenizer.encode(prompt, return_tensors="pt")

    # Generate text
    outputs = model.generate(inputs, max_length=max_length, num_return_sequences=1, no_repeat_ngram_size=2,
                             temperature=0.7, top_k=50, top_p=0.95)

    # Decode the generated text and return it
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return generated_text


# Example prompt
prompt = "In the future, artificial intelligence will"
generated_text = generate_text(prompt)
print(generated_text)


# Step 4: Understanding the Parameters:
# Step 5: Run and Generate Text