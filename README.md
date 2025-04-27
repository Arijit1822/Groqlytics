Groqlytics---Real-time-analytics

# 🖥️ System Monitor Dashboard with Productivity Tracker

A Django-based desktop and web-integrated system monitoring tool that tracks CPU, RAM, and Disk usage, while also logging active applications and offering AI-generated productivity tips.

## 🚀 Features

- 🔐 User authentication (login/logout)
- 📊 Live system stats:
  - CPU usage
  - RAM usage
  - Disk usage
- 📌 Active window tracker (Windows-only)
- ⏱️ App usage timer and history
- 📃 Save activity logs as PDF
- 🧠 AI-powered productivity suggestions using Groq API
- 🗨️ Chat assistant (optional integration with OpenAI or Groq)
- 🧪 Real-time dashboard with auto-refresh via AJAX

---

## 🛠️ Tech Stack

- **Backend:** Django 5.x
- **Frontend:** HTML5, Bootstrap 5, Chart.js
- **AI Integration:** Groq API / OpenAI (optional)
- **PDF Generation:** LibreOffice (`soffice`) + `python-docx`
- **System Info:** `psutil`, `win32gui`, `win32process`

---

⚠️ Notes
This app uses win32gui and psutil, so it currently supports Windows only for app tracking.
LibreOffice (soffice) must be installed and in system PATH to export PDFs.
Designed for development/demo use. Not production-ready.

📝 License
This project is licensed under the MIT License.

## Login details-
username & password: admin

## ⚙️ Setup Instructions

### 1. Clone the repository
### 2. Install dependencies
### 3. Navigate to sysmon in terminal
```bash
git clone https://github.com/Arijit1822/Groqlytics
cd Groqlytics
python -m pip install pywin32 
pip install -r requirements.txt
cd sysmon
python manage.py runserver



