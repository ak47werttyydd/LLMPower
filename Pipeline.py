from transformers import pipeline
import torch

#macOS gpu
classifier = pipeline("sentiment-analysis", device=torch.device("mps"))
print(classifier("I've been waiting for a HuggingFace course my whole life."))

