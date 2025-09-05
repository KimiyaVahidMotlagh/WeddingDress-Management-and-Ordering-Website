# WeddingDress-Management-and-Ordering-Website  
This project is a **web-based platform for wedding dress management and ordering**. The system allows brides to register, enter their body measurements, receive intelligent dress recommendations, and book appointments online. It also provides an **admin panel** for managing users, dresses, bookings, and orders. Additionally, an **AI-powered image generation module** is included to create custom dress designs using Stable Diffusion and LoRA.  

## Table of Content  
- Project Overview  
- Features  
- Technologies  
- System Modules  
- AI Dress Generation  
- Installation & Setup  
- Future Improvements  

## Project Overview  
The aim of this project is to **digitalize and simplify the process of selecting and ordering wedding dresses**. Traditional methods require multiple in-person visits, limited model availability, and lack intelligent recommendations.  
Our system addresses these issues by:  
- Providing **smart recommendations** based on body shape.  
- Offering an **online booking system** for trying on dresses.  
- Enabling **custom dress design** using artificial intelligence.  

## Features  
- User registration and profile management  
- Body measurement input & **body type classification**  
- Personalized dress recommendations  
- Gallery of wedding dresses with **favorites list**  
- Online booking system for appointments  
- Order management & tracking system  
- Admin dashboard (CRUD operations for models, users, and orders)  
- AI-based custom dress image generation  

## Technologies  
- **Backend:** Django (Python)  
- **Frontend:** HTML, CSS, JavaScript  
- **Database:** SQLite (upgradeable to PostgreSQL/MySQL)  
- **AI Models:** Stable Diffusion + LoRA for image generation  

## System Modules  
- **Accounts:** User authentication and body profile management  
- **Dresses:** Gallery display, favorites, and filtering  
- **Recommendation:** Content-based recommendation engine + AI generator  
- **Bookings:** Appointment scheduling with availability validation  
- **Orders:** Online order creation and status tracking  
- **Dashboard:** Admin tools for managing dresses, bookings, and users  

## AI Dress Generation  
The recommendation module integrates **Stable Diffusion with LoRA fine-tuning**. Users can choose parameters such as skirt type, neckline, and fabric. The system then generates a **unique wedding dress image** based on the chosen attributes.  

Process includes:  
- Text-to-image generation using Stable Diffusion  
- LoRA fine-tuning for wedding dress domain  
- Saving generated results into the user’s gallery  

## Installation & Setup  

```bash
# Clone repository
git clone https://github.com/KimiyaVahidMotlagh/WeddingDress-Management-and-Ordering-Website.git
cd WeddingDress-Management-and-Ordering-Website

# Create virtual environment
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start development server
python manage.py runserver
```
App will run on: http://127.0.0.1:8000/
