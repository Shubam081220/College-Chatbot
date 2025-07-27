# backend/chatbot.py

from backend.faq_data import FAQS
from transformers import T5ForConditionalGeneration, T5Tokenizer
import torch
from fuzzywuzzy import fuzz

# Load T5 model and tokenizer
tokenizer = T5Tokenizer.from_pretrained("t5-small")
model = T5ForConditionalGeneration.from_pretrained("t5-small")

def generate_t5_response(user_input):
    # Instruction-style prompt improves output quality
    input_text = "answer the question: " + user_input
    input_ids = tokenizer.encode(input_text, return_tensors="pt", max_length=512, truncation=True)
    output_ids = model.generate(input_ids, max_length=100, num_beams=4, early_stopping=True)
    return tokenizer.decode(output_ids[0], skip_special_tokens=True)

def get_response(user_input):
    best_score = 0
    best_answer = None

    # Fuzzy matching to find FAQ-like answers
    for question, answer in FAQS.items():
        score = fuzz.partial_ratio(user_input.lower(), question.lower())
        if score > best_score:
            best_score = score
            best_answer = answer

    if best_score > 80:  # Acceptable match threshold
        return best_answer

    # Fallback to T5 model if no good FAQ match
    return generate_t5_response(user_input)
