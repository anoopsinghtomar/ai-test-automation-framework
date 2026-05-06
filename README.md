# AI Test Automation Framework 🧠⚙️

An **AI-powered QA automation framework** that combines **local Large Language Models** and **multimodal vision models** to generate, analyze, and execute intelligent test workflows.

It uses:
- 🧠 LLaMA 3 (8B) → reasoning, test case generation, bug reporting  
- 👁️ Qwen2-VL (7B) → image/UI understanding and visual bug detection  
- ⚙️ Python + Pytest → automation execution layer  
- 💻 Ollama → local LLM runtime  

---

## 🚀 Key Features

### 🧪 AI Test Generation
Automatically generates:
- Functional test cases  
- Edge cases  
- Negative scenarios  
- API test coverage  

### 👁️ UI / Visual Bug Detection
- Analyze UI screenshots  
- Detect layout issues  
- Identify missing validations  
- Extract visible text (OCR-like behavior)

### 🧠 AI Bug Report Generator
- Converts raw analysis into structured bug reports  
- Assigns severity levels  
- Suggests root causes  

### 🔄 End-to-End Pipeline
Image / input → Vision Model → LLM reasoning → Test cases + bug report

---

## 🏗️ Architecture

```text
Input (UI Screenshot / Description)
            ↓
     Qwen2-VL (Vision Model)
            ↓
   UI Analysis / Issue Detection
            ↓
     LLaMA 3 (Reasoning Model)
            ↓
 Test Cases + Bug Reports + Severity
            ↓
   Pytest Execution Layer

```
ai-test-automation-framework/
│
├── models/
│   └── ollama_client.py
│
├── services/
│   ├── image_analyzer.py
│   ├── text_reasoner.py
│   └── pipeline.py
│
├── tests/
│   ├── test_ui_analysis.py
│   └── test_api_generation.py
│
├── data/
│   └── sample_ui.png
│
├── utils/
│   └── helpers.py
│
├── main.py
└── requirements.txt
```

.
