from transformers import pipeline 

summarizer = pipeline("summarization")  

text = input("Enter your long paragraph or article:\n")

summary = summarizer(text, max_length=130, min_length=30, do_sample=False)

print("\n--- Summary ---")

print(summary[0]['summary_text'])
