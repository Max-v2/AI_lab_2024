# scripts/model_training.py
from transformers import GPT2LMHeadModel, GPT2Tokenizer, Trainer, TrainingArguments

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

def train_model(texts):
    inputs = tokenizer(texts, return_tensors="pt", max_length=512, truncation=True, padding="max_length")
    training_args = TrainingArguments(output_dir="./results", num_train_epochs=1, per_device_train_batch_size=2)
    trainer = Trainer(model=model, args=training_args, train_dataset=inputs)
    trainer.train()

# Example usage
texts = ["This is a sample text for training."]
train_model(texts)