# 🌐 Website Summarizer & Rephraser using Gemini API

This project allows users to summarize the content of any website in clean **Markdown format** and then rephrase that summary into a more **human-like, reader-friendly** tone using **Google's Gemini 2.0 Flash Lite** model. It also includes a typewriter-style text display for a fun and interactive experience.

---

## 🚀 Features

### ✅ Website Summarizer
- Fetches website content using `requests` and `BeautifulSoup`
- Filters out unwanted tags like `<script>`, `<style>`, etc.
- Extracts internal and external links
- Summarizes content in **Markdown format** using Gemini 2.0 Flash Lite
- Automatically saves the summary in a `.md` file with a clean filename

### ✅ Markdown Rephraser
- Reads saved Markdown summaries
- Rephrases the summary using Gemini into a **natural, human-like** tone
- Displays output with a **typewriter animation**
- Saves the rephrased version into a new file

---

## 🛠️ Tech Stack

- **Language:** Python
- **AI Model:** Gemini 2.0 Flash Lite (Google Generative AI)
- **Web Scraping:** BeautifulSoup, Requests
- **UX/Terminal Display:** Typewriter effect using `time` and `sys`
- **File Handling:** Markdown summary saving and rephrasing

---

## 📦 Requirements

Install dependencies with:

pip install google-generativeai beautifulsoup4 requests
