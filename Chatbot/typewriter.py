import google.generativeai as genai
import time
import sys
import os
from urllib.parse import urlparse

# ✅ Step 1: Configure Gemini API
API_KEY = "AIzaSyBPfNPZenlNlsJ3RKlt6k4CFj84ZRl9hN0"
genai.configure(api_key=API_KEY)

# ✅ Step 2: Initialize Gemini Model
model = genai.GenerativeModel(
    model_name="models/gemini-2.0-flash-lite",
    system_instruction="You are a helpful assistant that rephrases markdown summaries in a friendly, human-like tone while keeping the meaning same."
)

# ✅ Step 3: Typewriter Effect Function
def typewriter(text, speed=0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

# ✅ Step 4: Rephrase Summary
def rephrase_summary(content):
    prompt = f"""
    Please rephrase the following markdown content to make it sound natural, reader-friendly, and human-like while keeping the same meaning.

    Return it in valid markdown format.

    Content:
    {content}
    """
    response = model.generate_content(prompt)
    return response.text

# ✅ Step 5: Read Markdown File
def read_markdown_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"❌ File not found: {filename}")
        return None

# ✅ Step 6: Save Rephrased Content to New File
def save_rephrased_summary(rephrased_text, original_filename):
    base = os.path.splitext(original_filename)[0]  # e.g., summary_example_com
    new_filename = f"rephrased_{base}.md"
    with open(new_filename, "w", encoding="utf-8") as f:
        f.write(rephrased_text)
    print(f"\n✅ Rephrased summary saved to: {new_filename}")

# ✅ Step 7: Main Logic
def main():
    print("📝 Rephrase Summary with Typewriter Effect\n")
    filename = input("📂 Enter summary markdown filename (e.g., summary_example_com.md): ").strip()

    content = read_markdown_file(filename)
    if not content:
        return

    print("\n🔄 Rephrasing summary using Gemini...\n")
    rephrased = rephrase_summary(content)

    print("\n📣 Rephrased Summary (Typewriter Style):\n")
    typewriter(rephrased, speed=0.01)

    # ✅ Save the rephrased output to a new file
    save_rephrased_summary(rephrased, filename)

if __name__ == "__main__":
    main()
