# PAN Card Tampering Detection App

![GitHub repo size](https://img.shields.io/github/repo-size/shriyani18/pan-card-tampering-app?style=for-the-badge)
![Python](https://img.shields.io/badge/python-v3.8+-blue?style=for-the-badge)
![TensorFlow](https://img.shields.io/badge/tensorflow-v2.x-orange?style=for-the-badge)
![Flask](https://img.shields.io/badge/flask-v2.0-green?style=for-the-badge)

---

## Overview

AI-powered **PAN Card Tampering Detection App** to automatically identify tampered PAN card images.  
Built with **TensorFlow (ResNet50)** for feature extraction and **Flask** for the web interface.

---

## Features

- Upload PAN card images for tampering verification  
- Extract features using pretrained ResNet50 model  
- Compare uploaded images with trusted database  
- Clear tampering alerts with visual feedback  
- Responsive UI with assets served from `app/static` directory

---

## Installation & Setup

```bash
git clone https://github.com/shriyani18/pan-card-tampering-app.git
cd pan-card-tampering-app
python -m venv venv
source venv/bin/activate       # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
