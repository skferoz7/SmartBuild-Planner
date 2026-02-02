# SmartBuild Planner

SmartBuild Planner is a Python Flask–based web application that automatically generates **residential building floor plans**, 
estimates **construction cost**, and exports the plan as a **PDF** based on user inputs like plot size, number of bedrooms, 
floors, and budget.

This project demonstrates **automation in construction planning** using Python, data-driven logic, and dynamic PDF generation.

---

## Features

- 🧮 Automatic floor plan generation based on user input
- 🏠 Dynamic room layout (Bedroom, Hall, Kitchen, Bath, Dining)
- 📐 Scaled 2D floor plan drawing
- 💰 Construction cost estimation
- 📄 PDF generation with floor plan image
- 🖥️ Clean UI with live plan preview
- 🗄️ Data storage using SQLite database

---

## Technologies Used

### Backend
- Python 3
- Flask
- SQLAlchemy (ORM)
- SQLite

### Frontend
- HTML
- CSS
- Bootstrap
- Jinja2 Templates

### Plan & PDF Generation
- Matplotlib (2D floor plan drawing)
- ReportLab (PDF generation)

---

##Project Structure
```
SmartBuild-Planner/
│
├── app.py
├── requirements.txt
├── README.md
│
├── static/
│ ├── css/
│ ├── js/
│ ├── images/ # Generated floor plans
│ └── pdfs/ # Generated PDFs
│
├── templates/
│ ├── layout.html
│ ├── index.html
│ ├── input_plan.html
│ └── result.html
│
├── models/
│ ├── user.py
│ ├── building_plan.py
│ ├── room.py
│ └── cost_estimation.py
│
├── routes/
│ ├── auth.py
│ └── planner.py
│
├── utils/
│ ├── plan_generator.py
│ ├── plan_drawer.py
│ ├── cost_calculator.py
│ └── pdf_generator.py
│
└── database/
└── smartbuild.db
```

---

##  Installation & Setup

### Step-1: Clone the Repository
windows
```
git clone https://github.com/your-username/SmartBuild-Planner.git
cd SmartBuild-Planner
```
# Step-2: Create Virtual Environment
windows
```
python -m venv construction
```
# Step-3: Activate Virtual Environment

Windows
```
construction\Scripts\activate
```
# Run the Application
windows
```
python app.py
```

Open browser and visit:

http://127.0.0.1:5000

---

# How It Works (Logic Flow)

User enters plot dimensions, floors, bedrooms, and budget

System calculates total built-up area

Rooms are generated proportionally

Floor plan is drawn using Matplotlib

Cost estimation is calculated

Plan and data are saved in database

PDF report is generated with plan image

# Sample Output

Floor plan image (PNG)

PDF report containing:

Project title

Total area

Estimated cost

Floor plan drawing

Footer branding

# Future Enhancements

Multi-floor plan generation

Vastu-compliant layouts

SVG-based high-resolution plans

Electrical & plumbing layout

3D visualization

AutoCAD / DXF export

# Limitations

This project generates conceptual plans, not municipality-approved drawings

Structural calculations are not included

Manual architect validation is required for real construction

---

# Author

Shaik Feroz

📍 Hyderabad, India

📧 Email: ferozzz0655@gmail.com

🔗 LinkedIn: https://www.linkedin.com/in/feroz-shaik-9b228a25b/