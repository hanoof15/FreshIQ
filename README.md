# FreshIQ - Starter Repo

FreshIQ is a hybrid AI-based Food Expiry & Freshness Detection project starter repository.

## Structure
- backend/: FastAPI backend with CRUD endpoints (SQLite)
- frontend/: Placeholder for Flutter app
- data/: Place datasets here
- models/: Place trained models here
- docs/: Documentation and presentation assets

## Quick start (backend)

1. Create and activate virtual environment:
   ```
   python3 -m venv venv
   source venv/bin/activate    # Windows: venv\Scripts\activate
   ```

2. Install requirements:
   ```
   pip install -r backend/requirements.txt
   ```

3. Run FastAPI server:
   ```
   uvicorn backend.main:app --reload
   ```

4. Open http://127.0.0.1:8000/ and http://127.0.0.1:8000/docs

## How to add README to GitHub (via CLI)
1. Initialize git (if not already):
   ```
   git init
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/FreshIQ.git
   ```

2. Add and commit:
   ```
   git add README.md
   git commit -m "Add README"
   git push -u origin main
   ```

(If you prefer the GitHub web UI, see instructions in the repository docs.)

## Notes
- This starter includes a simple SQLite-backed CRUD API for inventory management.
- Tesseract/OCR and AI modules are not required to run the CRUD API.
