# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

MSUtrition — a nutrition tracker for Michigan State University dining hall food items. Users log meals by day, track calories/macros/micros against personal goals, search campus food items, save meal templates, and manage favorites.

## Commands

### Backend

```bash
cd backend/nutritionbackend
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver          # http://localhost:8000
```

Run a single test:
```bash
python manage.py test nutritionAPI.tests
```

Restore the database from the included dump:
```bash
createdb nutrition_db
pg_restore -d nutrition_db ../nutrition_backup.dump
```

### Frontend

```bash
cd frontend/nutrition-front-end
npm install
npm run dev      # http://localhost:5173
npm run build
npm run lint
npm run preview
```

## Architecture

### Backend — Django REST Framework

The Django app lives in `backend/nutritionbackend/`. The single app is `nutritionAPI/`.

**Data model** (see `nutritionAPI/models.py`):
- `Day` — one row per user per date (unique constraint enforced)
- `Meal` — belongs to a `Day`, named (Breakfast, Lunch, etc.)
- `FoodData` — a food item as logged into a specific `Meal`; nutrients are copied (and scaled) from `Foods` at log time
- `Foods` — the food catalog (MSU dining hall items); has `favorite` flag and `date_last_used` for sort ordering
- `Progress` — one-to-one with User, stores calorie/macro goals and weight
- `SavedMeal` — M2M to `Foods` with a `serving_multipliers` JSON field (food_id → scale factor)

**Authentication** — JWT via `djangorestframework-simplejwt`. Tokens are stored in `httponly` cookies (not localStorage). `CookiesJWTAuthentication` in `nutritionAPI/authentication.py` reads them from cookies. The refresh view falls back to request body for Safari compatibility.

**Views** — mix of `ModelViewSet` classes and `@api_view` decorated functions. `FoodsView.list` supports `sort` (`recent` / `id` / `favorite`) and `search` query params; always returns at most 20 results.

**Env** — `DATABASE_URL` and `SECRET_KEY` go in `backend/nutritionbackend/nutritionbackend/.env`. The settings file loads that file explicitly via `load_dotenv`.

**Deployment** — Railway (backend via `Procfile`/gunicorn), Neon (PostgreSQL), Vercel (frontend).

### Frontend — React + Vite

The frontend lives in `frontend/nutrition-front-end/src/`.

**Routing** (React Router v7):
- `/login` → `Auth.jsx` (login + sign-up tabs)
- `/` → `Header` + `MainBox` (requires auth; redirects to `/login` otherwise)
- `/onboarding` → `Onboarding.jsx` (first-time goal setup)

**State / Context**:
- `Context/Context.js` — `MealsContext`: the list of meal names (`["Breakfast", "Lunch", "Dinner", "Snacks"]`)
- `Context/DayContext.jsx` — `DaysProvider` / `useDaysContext`: tracks `selectedDate` (ISO string, local timezone)
- `Context/MealContext.js` — meal state (check file for current shape)

`App.jsx` holds auth state (`isLoggedIn`, `username`). `MainBox.jsx` is the dashboard shell — it fetches all data on mount (food log, progress, food catalog) and passes it down to child panels.

**Dashboard panels** (rendered inside `MainBox`):
- `Calories.jsx` — calorie ring, daily totals
- `Meals.jsx` + `Meal.jsx` — meal list; each meal expands to show logged foods
- `Micronutrients.jsx` + `MicroProgress.jsx` — compact micro summary
- `Progress.jsx` — macro progress bars
- `FullMicronutrients.jsx` — modal with full micronutrient breakdown
- `FullProgress.jsx` — modal with full macro/goal breakdown

**Add food flow**: `AddFood.jsx` (search modal) → `AddFoodData.jsx` (nutrition fact review + serving size adjustment before confirming). These are opened from `Meals.jsx` via `isModalOpen` / `isDataModalOpen` state in `MainBox`.

**API layer** (`src/api/`):
- `authApi.js` — login, register, logout, token refresh
- `mealApi.js` — food data CRUD, food catalog search
- `userApi.js` — user profile, progress goals
- `src/api.js` — legacy `is_authenticated` call (still used in `App.jsx`)

All API calls use `fetch` with `credentials: "include"` to send the JWT cookie. Base URL comes from `VITE_API_URL` in `.env`.

## Design System

`src/assets/tokens.css` is the single source of truth for all design tokens. It is imported in `index.css` and available globally.

**Typography rule** (enforced across all components):
- Numeric values (calorie counts, weights, macro grams) → `font-family: var(--font-mono)` (JetBrains Mono)
- All other text → `font-family: var(--font-sans)` (Inter)

**Color** — dark-first theme. Use semantic tokens (`--bg`, `--fg`, `--accent`, `--border`, etc.) in components, not raw ink/green values. Light theme is available via `[data-theme="light"]` but is not the default.

**Macro colors**: `--macro-protein` (blue), `--macro-carbs` (red), `--macro-fat` (yellow), `--macro-fiber` (purple).

Each component has a paired CSS file in `src/assets/` with the same base name.
