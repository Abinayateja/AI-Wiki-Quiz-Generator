# 🚀 AI Wiki Quiz Generator
DeepKlarity Technologies Assignment

An AI-powered web application that generates structured quizzes automatically from Wikipedia articles using FastAPI, React, LangChain, and Large Language Models.

The system accepts a Wikipedia URL, extracts article content using web scraping, and generates high-quality quiz questions with difficulty levels, explanations, and related topics.

---

# 🌐 Live Deployment

Frontend: https://ai-wiki-quiz-generator-smp3.onrender.com/
Backend API: https://ai-wiki-backend-lfjm.onrender.com/

---

# 🧠 Tech Stack

## Frontend
- React.js
- JavaScript (ES6+)
- HTML5 + CSS3

## Backend
- Python
- FastAPI
- LangChain
- Groq LLM

## Database
- PostgreSQL (Render hosted)

## Scraping
- BeautifulSoup (HTML parsing only, no Wikipedia API)

## Deployment
- Render (Backend)
- Render (Frontend)

---

# ✨ Features

## TAB 1 — Generate Quiz

- Accepts Wikipedia article URL input
- Validates URL format (Wikipedia-only validation)
- Scrapes article content dynamically
- Uses LangChain PromptTemplate with LLM
- Generates:

  - Title
  - Summary
  - Key entities
  - Sections
  - 5–10 quiz questions
  - Multiple choice options
  - Correct answer
  - Explanation
  - Difficulty levels (easy / medium / hard)
  - Related reading topics

- Structured card-based UI
- Loading animation during generation

---

## TAB 2 — Past Quizzes (History)

- Displays previously generated quizzes
- Database-backed history table
- Modal view showing full quiz details
- Reuses structured layout from Generate tab

---

# 🏆 Bonus Features Implemented

✅ URL validation  
✅ Database caching (prevents duplicate scraping)  
✅ Raw HTML stored in database  
✅ Related topics extraction  
✅ Section extraction from Wikipedia  
✅ LangChain prompt templating  
✅ Clean structured UI layout  

---

# 🧱 Architecture

                ┌──────────────────────┐
                │        User          │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │   React Frontend UI  │
                │  (Generate + History)│
                └──────────┬───────────┘
                           │ REST API
                           ▼
                ┌──────────────────────┐
                │     FastAPI Backend  │
                └──────────┬───────────┘
                           │
        ┌──────────────────┼──────────────────┐
        ▼                  ▼                  ▼

┌────────────────┐   ┌─────────────────┐   ┌────────────────┐
│ Wikipedia      │   │ LangChain Prompt│   │ PostgreSQL DB  │
│ Scraper        │   │ Template + LLM  │   │ (Quiz Storage) │
│ (BeautifulSoup)│   │ (Groq Model)    │   │                │
└────────────────┘   └─────────────────┘   └────────────────┘

        │                    │
        └──────────► Structured Quiz JSON ◄──────────┘
                           │
                           ▼
                Returned to React Frontend

# 🚀 How to Run Locally

1️⃣ Clone Repository
Copy code
Bash
git clone https://github.com/YOUR_USERNAME/ai-wiki-quiz-generator.git

cd ai-wiki-quiz-generator
2️⃣ Backend Setup (FastAPI)
Navigate to backend folder
Copy code
Bash
cd backend
Create virtual environment
Copy code
Bash
python -m venv venv
Activate environment
Windows:
Copy code
Bash
venv\Scripts\activate
Mac/Linux:
Copy code
Bash
source venv/bin/activate
Install dependencies
Copy code
Bash
pip install -r requirements.txt
Set Environment Variables
Create .env
Copy code

GROQ_API_KEY=your_api_key_here
DATABASE_URL=postgresql://username:password@host:port/dbname
Run Backend Server
Copy code
Bash
uvicorn main:app --reload
Backend runs at:
Copy code

http://127.0.0.1:8000
Swagger docs:
Copy code

http://127.0.0.1:8000/docs
3️⃣ Frontend Setup (React)
Navigate to frontend:
Copy code
Bash
cd ../frontend
Install dependencies:
Copy code
Bash
npm install
Run development server:
Copy code
Bash
npm run dev
Frontend runs at:
Copy code

http://localhost:5173


# 🧪 Testing :

Open frontend UI.
Enter Wikipedia URL.
Click Generate Quiz.
View generated quiz.
Check History tab for saved quizzes.

---

## 📸 Screenshots

### 🟢 1. Generate Quiz (Tab 1)

User provides a Wikipedia URL and the system generates a structured AI-powered quiz using LangChain + LLM.

Features demonstrated:

- Wikipedia scraping
- LLM quiz generation
- Structured UI display
- Difficulty levels
- Related topics

![Generate Quiz](docs/screenshots/Generate-quiz.png)

---

### 🟢 2. Loading State

Loading animation displayed while backend processes scraping and quiz generation.

Features demonstrated:

- Async request handling
- Improved user experience

![Loading State](docs/screenshots/Generation-loading.png)

---

### 🟢 3. Past Quizzes History (Tab 2)

Displays previously generated quizzes stored in PostgreSQL database.

Features demonstrated:

- Database persistence
- History tracking
- Table-based UI

![History Tab](docs/screenshots/history.png)

---

### 🟢 4. Quiz Details Modal

Clicking “Details” opens modal showing full quiz layout.

Features demonstrated:

- Modal reuse
- API retrieval from database
- Structured quiz rendering

![Details Modal](docs/screenshots/Details-modal.png)

---

### 🟢 5. API Documentation (Swagger UI)

FastAPI automatic API documentation showing structured JSON response.

Features demonstrated:

- REST API design
- Proper JSON structure
- Backend validation

![Request](docs/screenshots/Swagger.png)
![Response](docs/screenshots/Swagger-1.png)

---

---

## ❤️ Made with Love

Built with passion and curiosity by  

**Abinayateja Gaddam**  

📧 Email: gaddamabinayateja@gmail.com  

---