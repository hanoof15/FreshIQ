🥗 FreshIQ – AI-Powered Food Expiry & Freshness Detection
From barcodes to bananas – track food expiry and freshness with AI.
<!-- optional, replace with screenshot later -->
📌 Table of Contents
About the Project
Features
Tech Stack
System Architecture
Screenshots
Installation
Usage
Project Roadmap
Datasets
Contributors
License
🚀 About the Project
FreshIQ is a hybrid mobile + backend system designed to detect expiry and freshness of food items:
Packaged food with barcodes → detects expiry from database.
Packaged food without barcode → extracts printed expiry using OCR.
Fresh produce (fruits/vegetables/meat) → predicts freshness using a CNN vision model.
Helps reduce food waste, ensures food safety, and supports sustainability goals.
✨ Features
📦 Barcode scanner → fetch expiry details from mock database / Open Food Facts.
🏷️ OCR expiry detection → reads printed labels (milk packets, bread, local chips).
🍎 AI freshness detection → CNN classifies food as Fresh / Near Expiry / Spoiled.
🗂️ Inventory management (CRUD) → Add, view, update, delete items.
🔔 Smart notifications → Alerts before expiry.
🍳 Recipe suggestions → Recommends recipes for items near expiry.
☁️ Deployable backend → FastAPI server, ready for Render/Railway.
🛠️ Tech Stack
Frontend (Mobile App):
Flutter (Dart)
tflite_flutter (on-device AI)
Firebase (push notifications)
Backend (API):
FastAPI (Python)
Uvicorn (ASGI server)
PostgreSQL / SQLite (database)
AI/ML:
TensorFlow / Keras (CNN model)
MobileNetV2 (transfer learning)
OpenCV + Tesseract OCR
Pyzbar (barcode scanning)
🏗️ System Architecture
flowchart TD
    User[User Mobile App] --> |Scan Barcode/OCR/Camera| Flutter[Flutter Frontend]
    Flutter --> |API Calls| FastAPI[FastAPI Backend]
    FastAPI --> |Barcode Lookup| DB[(Database)]
    FastAPI --> |OCR Text Extraction| OCR[OCR Engine (Tesseract)]
    FastAPI --> |Freshness Detection| CNN[AI Model (TFLite/TF)]
    FastAPI --> Flutter
    Flutter --> User
📸 Screenshots (to be added)
Splash Screen
Inventory Dashboard
Barcode Scan Flow
Freshness Detection
⚙️ Installation
Backend (FastAPI)
# Clone repo
git clone https://github.com/your-username/FreshIQ.git
cd FreshIQ/backend

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run server
uvicorn main:app --reload
Frontend (Flutter)
cd frontend
flutter pub get
flutter run
▶️ Usage
Launch the Flutter app.
Add items using Barcode / OCR / Camera.
View expiry/freshness in the inventory dashboard.
Get notified before items expire.
🛣️ Project Roadmap
✅ Week 1: Backend CRUD + Barcode
✅ Week 2: OCR + Inventory management
✅ Week 3: AI model training + TFLite integration
✅ Week 4: Notifications + Deployment + Presentation
📂 Datasets
Barcode: Open Food Facts + Mock DB.
OCR: Custom images of expiry labels + synthetic data.
Freshness: Kaggle Fruits Fresh & Rotten, Roboflow VegNet, self-collected samples.
👩‍💻 Contributors
Hanoof Marium – Developer & AI Researcher
Mentor / Guide – [Your Guide’s Name]
📜 License
MIT License © 2025 FreshIQ
