import transformers
import torch

# os.environ['']

# "meta-llama/Meta-Llama-3.1-8B-Instruct"
model_id = "D:\\Codes\\NLP\\Meta-Llama-3.1-8B-Instruct"

pipeline = transformers.pipeline(
    "text-generation",
    model=model_id,
    model_kwargs={"torch_dtype": torch.bfloat16},
    device_map="auto",
)

messages = [
    # {"role": "system", "content": "You are a pirate chatbot who always responds in pirate speak!"},
    {"role": "user", "content": "Who are you?"},
]

outputs = pipeline(
    messages,
    max_new_tokens=100,
)
print(outputs[0]["generated_text"][-1])
