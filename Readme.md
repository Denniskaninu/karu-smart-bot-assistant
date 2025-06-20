# 🎓 **KaruBot** – *Your Smart Virtual Assistant for Karatina University* 🚀

**KaruBot** is a cutting-edge, AI-powered chatbot built with **Flask** and powered by **Google Gemini Pro**. Designed to deliver *fast*, *accurate*, and *friendly* answers about **Karatina University (KARU)**, it covers everything from admissions to academic programs, facilities, and more! 🌟

---

## ✨ **Features**

- 🤖 **Intelligent AI Responses**: Harnesses *Google Gemini Pro* for context-aware, dynamic replies.  
- 🏛️ **KARU Knowledge Hub**: Packed with info on programs, admissions, departments, facilities, and contacts.  
- ⚡ **Quick Info API**: Instant access to categorized data via endpoints like `/quick-info/admissions`.  
- 🌐 **Sleek Web Frontend**: User-friendly homepage built with Flask, supporting CORS for seamless integration.  
- 🔒 **Secure Setup**: API keys and secrets safely managed with environment variables.  

---

## 🛠️ **Tech Stack**

| **Layer**         | **Technology**                     |
|-------------------|------------------------------------|
| **Backend**       | 🐍 Flask (Python)                 |
| **AI Engine**     | 🧠 Google Gemini Pro              |
| **Web Parsing**   | 📜 BeautifulSoup                 |
| **Environment**   | ⚙️ `python-dotenv`               |
| **API/Frontend**  | 🌍 Flask + CORS + JSON           |

---

## 🚀 **Get Started**

### 1️⃣ **Clone the Repo**
```bash
git clone https://github.com/your-username/karubot.git
cd karubot

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Set Up Environment
Create a .env file in the root directory:
GEMINI_API_KEY=your_gemini_api_key_here

4️⃣ Launch the App
python app.py

Access KaruBot at http://localhost:5000! 🎉

🌐 API Endpoints
📩 POST /chat
Sends a user query and returns an AI-generated response.
Request:
{
  "message": "What are the admission requirements for undergraduate programs?"
}

Response:
{
  "response": "Karatina University requires a KCSE mean grade of C+ and above for undergraduate admission...",
  "status": "success",
  "timestamp": "2025-06-20T10:34:00"
}

📚 GET /quick-info/
Fetches predefined info instantly. Supported info_type values:

admissions 📝
programs 🎓
contacts 📞
links 🔗

Example:
GET /quick-info/admissions


📖 Knowledge Base
KaruBot answers questions on a wide range of KARU topics, including:

🎓 Academic Programs  
📝 Admissions & Requirements  
🏢 Campus Facilities  
📞 Department Contacts  
🔗 Quick Links (KUCCPS, Student Portal, etc.)  
💰 Fee Structures  
🧑‍🎓 Student Services  
🔬 Research Areas


🛡️ Error Handling

🔌 API Downtime: Falls back to static responses for uninterrupted service.  
❓ Invalid Queries: Returns friendly prompts to guide users.  
🚫 Bad Routes: Serves clear error messages for unrecognized requests.


🧠 AI Prompt Magic
KaruBot’s responses are powered by a carefully crafted prompt that includes:

🏫 KARU-Specific Facts: Ensures accurate, relevant answers.  
😊 Friendly Persona: Professional yet approachable tone.  
📋 Structured Output: Consistent formatting for clarity.


📂 Project Structure
karubot/
├── app.py              # 🚀 Main Flask app & API endpoints
├── templates/
│   └── index.html      # 🌐 Web homepage
├── .env                # 🔐 Environment variables (not committed)
├── README.md           # 📖 Project documentation
└── requirements.txt    # 📦 Dependencies


🤝 Contributing
We’d love your contributions! Here’s how to get started:

🍴 Fork the repository.  
🌿 Create a feature branch: git checkout -b feature/YourFeature.  
💾 Commit changes: git commit -m 'Add YourFeature'.  
🚀 Push to the branch: git push origin feature/YourFeature.  
📬 Open a pull request.

For major changes, open an issue first to discuss your ideas. 💡

📜 License
KaruBot is open-source under the MIT License. 🖌️

👨‍💻 Author
Dennis Kaninu🎓 BSc Computer Science – Karatina University📧 info@karu.ac.ke | 🌐 karu.ac.ke

🌍 Connect with Karatina University

🌐 Website: karu.ac.ke  
📝 Admissions: admissions.karu.ac.ke  
🧑‍🎓 Student Portal: portal.karu.ac.ke


KaruBot – Your guide to Karatina University, powered by AI! 🌟```
