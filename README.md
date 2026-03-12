# Password Analyzer Web Tool

A simple web application to check the strength of passwords. Users can input a password and get feedback on how secure it is, along with tips to improve it.

---

## Live Demo

Check it live here: [Password Analyzer](https://secure-password-analyzer-web-tool.onrender.com)

---

## Features

- Analyze password strength (Weak, Medium, Strong)  
- Gives suggestions for improvement (missing uppercase, numbers, special characters)  
- Frontend built with a simple HTML interface  
- Backend powered by Flask with a REST API  
- Deployed on Render with Gunicorn

---

## Project Structure


```text
password-analyzer/
├ src/
│ ├ main.py 
│ ├ routes.py 
│ ├ analyzer.py 
│ └ public/
│ └ index.html 
└ requirements.txt


---

## Deployment 
- Deployed on Render using Gunicorn: gunicorn src.main:app
- Static folder served from src/public
