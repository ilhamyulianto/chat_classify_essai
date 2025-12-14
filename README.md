# Project Overview & Quick Walkthrough

This document provides a **short explanation and quick walkthrough** of the two main markdown documents included in this project, along with guidance for the **Essay Task submission**.

---

## 1. AI Assistant Demo (Streamlit + Ollama)

**Referenced file:** `Readme.md`

### What this document covers

This markdown explains a lightweight **AI chat assistant demo** built using **Streamlit** and a **local Ollama LLM server**. The assistant uses Google's **Gemma 3 (1B)** model and demonstrates how to connect a frontend UI to a locally hosted language model via a REST API.

### Key points

* Purpose: Local demo and experimentation with LLMs
* Tech stack:

  * Python
  * Streamlit (UI)
  * Ollama (LLM runtime)
  * Gemma 3:1B model
* Features:

  * Chat-style interface
  * Session-based conversation history
  * Sidebar controls (clear chat)

### Quick walkthrough

1. Install Python dependencies (`streamlit`, `requests`)
2. Install and run Ollama
3. Pull the `gemma3:1b` model
4. Start the app using `streamlit run app.py`
5. Interact with the AI assistant via the browser

This document is mainly focused on **application setup, environment configuration, and usage**.

---

## 2. ISP Customer Question Classification (Machine Learning)

**Referenced file:** `ReadMe.md`

### What this document covers

This markdown describes an **end-to-end NLP and Machine Learning pipeline** for classifying ISP customer questions into three categories: **Information, Request, and Problem**. It emphasizes **auto-labeling (weak supervision)** to overcome the lack of manually labeled data.

### Key points

* Problem domain: ISP customer service text classification
* Categories:

  * Information
  * Request
  * Problem
* Core methodology:

  * Text preprocessing & normalization
  * Weak supervision / auto-labeling
  * TF-IDF feature extraction
  * Linear SVM classification
  * Stratified K-Fold cross-validation

### Quick walkthrough

1. Load and explore raw customer question data
2. Clean and normalize text (Indonesian-focused)
3. Auto-label data using keywords and semantic similarity
4. Generate TF-IDF features
5. Train a Linear SVM classifier
6. Evaluate using cross-validation metrics

This document focuses on **ML methodology, reasoning, evaluation, and limitations** rather than application deployment.

---

## 3. Essay Task Submission

For the **Essay Task**, supporting materials and additional explanations will be provided via **Google Drive links**.

### What to expect

* Detailed written explanations (PDF or DOCX)
* Supporting notebooks or datasets (if applicable)
* Additional analysis, diagrams, or experiment notes

### Access

> **Google Drive Link:**
>
> *https://drive.google.com/file/d/1X9dll9_-mMEwZx5NN8KEzXBpySwFNMg1/view?usp=sharing*


---

## Summary

* `Readme.md` → Practical **AI application demo** (Streamlit + Ollama)
* `ReadMe.md` → **Machine Learning & NLP pipeline** for text classification
* Essay Task → Extended explanation and supporting materials via Google Drive

This overview is intended to help reviewers quickly understand the **structure, intent, and scope** of each component in the project.
