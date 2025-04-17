# Symptom_Analyzer
🩺 MediAI - Symptom Checker AI
This is a mobile app that helps people check their health condition by just entering symptoms like "fever", "headache", etc. It uses AI to suggest a possible diagnosis based on the symptoms you enter.

The app is built using:

React Native (for the mobile UI)

Django (for backend and API)

Groq LLM (AI model to generate diagnosis)

🔧 Features
Type in symptoms (like “fever and cough”)

Press a button to get a possible diagnosis

See the AI-generated response in the app

Works on Android and can be converted to a real APK

Mobile friendly and very easy to use

💡 AI Customization (Mock Fine-Tuning)
We created a small custom dataset of 30 symptom-diagnosis pairs. These are added inside the AI prompt so it understands how to respond better.

This method is called few-shot prompting — it helps the AI behave like it's been trained on medical data without actually doing full training.

Example:

yaml
Copy
Edit
- Symptoms: fever and sore throat → Diagnosis: Flu
- Symptoms: joint pain and swelling → Diagnosis: Arthritis
📱 How to Run (Frontend - React Native)
1. Install dependencies
bash
Copy
Edit
npm install
2. Start the app with Expo
bash
Copy
Edit
npx expo start
Use Expo Go app on your phone to scan the QR code.

Make sure your phone and laptop are on the same Wi-Fi.

🔙 How to Run (Backend - Django)
1. Install Python packages
bash
Copy
Edit
pip install -r requirements.txt
2. Run the server
bash
Copy
Edit
python manage.py runserver 0.0.0.0:8000
⚙️ Configuration
Set your Groq API key in .env
env
Copy
Edit
GROQ_API_KEY=your_key_here
Update the backend URL in App.js or config.js
js
Copy
Edit
const BACKEND_URL = "http://your-ip:8000/analyze/";
If deployed, use:

js
Copy
Edit
const BACKEND_URL = "https://your-app.onrender.com/analyze/";
🗂️ Project Structure
arduino
Copy
Edit
symptom-checker/
├── backend/ (Django)
│   ├── symptom_data.json (30 entries)
│   └── views.py (AI logic)
│
├── frontend/ (React Native)
│   ├── App.js (UI + axios)
│   └── config.js (backend URL)
📦 Deliverables
✅ Mobile app (React Native)

✅ AI-powered backend (Django + Groq LLM)

✅ Mock fine-tuned dataset

✅ Fully working demo

✅ Production-ready code structure
