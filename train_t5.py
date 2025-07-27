import pandas as pd
from datasets import Dataset
from transformers import T5Tokenizer, T5ForConditionalGeneration, Trainer, TrainingArguments

# Load dataset
df = pd.read_csv("data/college_qa_data.csv")
dataset = Dataset.from_pandas(df)

# Load tokenizer and model
model_name = "t5-small"
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

# Preprocessing function
def preprocess(example):
    inputs = tokenizer(example["input"], padding="max_length", truncation=True, max_length=64)
    targets = tokenizer(example["target"], padding="max_length", truncation=True, max_length=64)
    inputs["labels"] = targets["input_ids"]
    return inputs

# Tokenize dataset
tokenized_dataset = dataset.map(preprocess)

# Training arguments
training_args = TrainingArguments(
    output_dir="./t5_college_model",
    per_device_train_batch_size=4,
    num_train_epochs=5,
    logging_dir="./logs",
    logging_steps=10,
    save_steps=50,
    save_total_limit=2,
)

# Trainer setup
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset,
    tokenizer=tokenizer,
)

# Start training
trainer.train()

# Save the final model
model.save_pretrained("t5_college_model")
tokenizer.save_pretrained("t5_college_model")
