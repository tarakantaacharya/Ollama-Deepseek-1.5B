### DeepSeek Mini - AI Chatbot

This project is a simple AI chatbot using **Ollama** for LLM inference and a frontend built with **HTML, JavaScript (Tailwind CSS)**.

## **1. Install Ollama**
Ollama is required to run the model locally. Follow these steps:

### **Step 1: Download Ollama**
- Visit the official website: [https://ollama.com](https://ollama.com)
- Download and install **Ollama** for your OS (Windows, macOS, or Linux).

### **Step 2: Verify Installation**
After installation, open a terminal (CMD, PowerShell, or Terminal) and check if Ollama is installed:

```sh
ollama --version
```
If Ollama is installed correctly, it will return the version number.

### **Step 3: Pull a Model**
Ollama works with different models. To pull **DeepSeek-Mini**, run:

```sh
ollama pull deepseek
```

## **2. Running Locally**
Once Ollama is set up, follow these steps to run the project.

### **Step 1: Clone the Repository**
```sh
git clone https://github.com/your-username/deepseek-mini.git
cd deepseek-mini
```

### **Step 2: Install Dependencies**
Ensure Python is installed (`python --version`). Then, install the required dependencies:

```sh
pip install flask
```

### **Step 3: Start the Backend**
Run the Python server (`deepseek.py`):

```sh
python deepseek.py
```
This will start the API server for processing requests.

### **Step 4: Start the Frontend**
Open `index.html` in a browser, or start a simple local server:

```sh
python -m http.server 8000
```
Then, visit **`http://localhost:8000`** in your browser.

---

## **3. File Structure & Explanation**
### **deepseek.py (Backend)**
- A **Flask API** that connects to **Ollama** and sends user questions to the model.
- The model processes queries and returns responses.
- Handles **POST** requests from the frontend.

### **index.html (Frontend)**
- Provides a **chat interface** using **HTML, Tailwind CSS, and JavaScript**.
- Sends user input to the backend (`deepseek.py`) via a fetch request.
- Displays the AI-generated responses dynamically.
- Supports **LaTeX** rendering for mathematical expressions.

---

## **4. API Workflow**
1. **User asks a question** → `index.html` sends it to `deepseek.py` via `fetch()`.
2. **deepseek.py processes the request** using Ollama.
3. **Response is streamed back** to `index.html` and displayed in the chatbox.

---

## **5. Additional Commands**
### **To Update the Project (Git Commands)**
```sh
git add .
git commit -m "Updated chatbot"
git push origin main
```

---

### 🎯 **Now, your chatbot is running locally with Ollama! 🚀**
```
