

# MSU Nutrition Tracking App
### A nutrition tracker built specifically for Michigan State University dining halls.

---

## What This Is

Most nutrition apps are built around grocery store barcodes. If you eat at an MSU dining hall, that does not help you. This app is built to track the specific food items served on campus — so you can actually log what you ate at Brody or South Pointe, hit your macros, and not have to guess.

The backend is a Django REST API connected to a PostgreSQL database. The frontend is React. Users can create an account, log meals by day, search campus food items, save meal templates, and track their daily progress against nutrition goals.

---

## Demo

> [https://youtu.be/d6WFwL0KVgs](https://youtu.be/rPGX2NBiTEs)

---

## User Guide

You do not need to know how to code to use this app. Here is how it works:

1. **Create an account** — go to the app and register with your email and a password.
2. **Set your goals** — enter your daily calorie and macro targets in your profile.
3. **Log your meals** — each day is split into meals (breakfast, lunch, dinner, etc.). Search for a food item, select it, and add it to the right meal.
4. **Track your progress** — the dashboard shows your totals for the day compared to your goals.
5. **Save meal templates** — if you eat the same thing often, save it as a meal template and load it in one click next time.
6. **Favorites** — star foods you eat regularly so they show up faster when you search.

---

## Tech Stack

| Technology | Why It Was Used |
|------------|-----------------|
| **Django** | Chosen for its ORM and built-in admin interface. FastAPI would be faster, but Django was the right tradeoff for a project this size. The admin panel and ORM made building and testing significantly faster. |
| **Django REST Framework** | Built on top of Django to handle the REST API. Clean, well-documented, and integrates directly with the ORM. |
| **React** | Frontend framework. Chosen over plain HTML/CSS/JS for its state management and reusable component model. |
| **PostgreSQL** | All data in this app is relational by nature: users, days, meals, and foods all reference each other. PostgreSQL was the obvious choice. |
| **Simple JWT** | Token-based authentication built directly into Django. Secure and straightforward to set up. |
| **Neon Database** | Hosted PostgreSQL. Cheap and easy to spin up for a project like this. |
| **Railway** | Backend hosting. Simple deployment from GitHub and cheap for low-traffic projects. |
| **Vercel** | Frontend hosting. Works well with Vite/React and deploys in seconds. |

---

## Project Structure

```
nutrition-tracking/
├── backend/
│   └── nutritionbackend/
│       ├── manage.py
│       ├── requirements.txt
│       ├── Procfile                  ← Process config for hosting
│       ├── addFood.py                ← Script to seed food database
│       ├── nutrition_backup.dump     ← PostgreSQL database backup
│       ├── nutritionAPI/
│       │   ├── models.py             ← Day, Meal, Food, Progress, SavedMeal models
│       │   ├── serializers.py
│       │   ├── views.py
│       │   ├── urls.py
│       │   └── authentication.py    ← Custom JWT views
│       └── nutritionbackend/
│           ├── settings.py
│           ├── urls.py
│           ├── wsgi.py
│           └── .env                 ← DATABASE_URL goes here (not committed)
└── frontend/
    └── nutrition-front-end/
        ├── package.json
        ├── vite.config.js
        ├── vercel.json
        ├── index.html
        └── src/
            ├── App.jsx
            ├── main.jsx
            ├── api/
            │   ├── authApi.js        ← Login, register, token refresh
            │   ├── mealApi.js        ← Meal and food API calls
            │   └── userApi.js        ← User profile and progress
            ├── Context/
            │   ├── Context.js        ← Global auth/user state
            │   ├── DayContext.jsx    ← Active day state
            │   └── MealContext.js    ← Meal state
            └── assets/
                └── tokens.css        ← Design tokens (colors, spacing)
```

---

## Local Setup

### Prerequisites

- Python 3.11+
- Node.js 18+
- PostgreSQL

### Backend

```bash
cd backend/nutritionbackend
```

1. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file inside `nutritionbackend/nutritionbackend/` (next to `settings.py`):

```env
DATABASE_URL=postgres://USER:PASSWORD@localhost:5432/nutrition_db
SECRET_KEY=your-secret-key
DEBUG=True
```

4. Run migrations and start the server:

```bash
python manage.py migrate
python manage.py runserver
```

The API will be available at `http://localhost:8000`.

#### Restore from dump (optional)

A database dump is included at `backend/nutrition_backup.dump`. To restore it:

```bash
createdb nutrition_db
pg_restore -d nutrition_db backend/nutrition_backup.dump
```

### Frontend

```bash
cd frontend/nutrition-front-end
```

1. Install dependencies:

```bash
npm install
```

2. Start the dev server:

```bash
npm run dev
```

The app will be available at `http://localhost:5173`. Make sure the backend is running first.

---

## API Endpoints

### Auth
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/token/` | Obtain JWT access + refresh tokens |
| POST | `/token/refresh/` | Refresh access token |
| POST | `/register/` | Create a new user account |
| POST | `/logout/` | Invalidate session |
| GET | `/authenticated/` | Check if current user is authenticated |

### User & Progress
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET/PUT | `/api/user/` | Get or update user profile |
| GET/PUT | `/api/progress/` | Get or update daily progress |
| POST | `/api/update-progress/` | Update progress metrics |

### Days & Meals
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET/POST | `/api/days/` | List or create days |
| GET/PUT/DELETE | `/api/days/{id}/` | Retrieve, update, or delete a day |
| GET/POST | `/api/meals/` | List or create meals |
| GET/PUT/DELETE | `/api/meals/{id}/` | Retrieve, update, or delete a meal |

### Foods
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET/POST | `/api/foods/` | List or create foods |
| GET | `/api/food-data/` | Get food nutrition data |
| POST | `/api/add-food/` | Add a food to a meal |
| POST | `/api/add-multiple-foods/` | Add multiple foods to a meal at once |

### Saved Meals & Favorites
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET/POST | `/api/saved-meals/` | List or create saved meals |
| POST | `/api/add-saved-meal/` | Save a meal template |
| POST | `/api/add-saved-meal-to-meal/` | Load a saved meal into a day's meal |
| POST | `/api/add-favorite/` | Save a food to favorites |
| DELETE | `/api/remove-favorite/` | Remove a food from favorites |

### Misc
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/health/` | Health check |

---

## Known Issues

- Food database is limited to a subset of MSU dining hall locations. Not all locations or menu items are covered yet.
- No barcode scanning support for packaged foods sold at Sparty's Markets.

---

## Future Improvements

- Full food data coverage across all MSU dining hall locations
- Barcode scanning for Sparty's Market packaged items

## Development Notes

This project was built with AI-assisted development. Claude was used throughout
for code generation, and debugging. Claude was heavily used for design and frontend applications, to 
avoid tedious styling. All architecture decisions, feature scoping, data
modeling, and deployment were done independently. The goal was to ship a real,
working product — AI was a tool to do that faster, not a shortcut around
understanding the code.
