from flask import render_template, current_app as app
from .models import Article

@app.route('/')
def home():
    cancer_types = [
        'Breast Cancer', 'Lung Cancer', 'Prostate Cancer', 'Colorectal Cancer',
        'Melanoma (Skin Cancer)', 'Bladder Cancer', 'Kidney Cancer', 'Liver Cancer',
        'Pancreatic Cancer', 'Thyroid Cancer', 'Leukemia', 'Lymphoma (Hodgkin and Non-Hodgkin)',
        'Ovarian Cancer', 'Endometrial Cancer', 'Cervical Cancer', 'Esophageal Cancer',
        'Stomach Cancer', 'Brain and Spinal Cord Tumors', 'Testicular Cancer', 'Bone Cancer',
        'Soft Tissue Sarcoma'
    ]
    return render_template('index.html', cancer_types=cancer_types)

@app.route('/cancer/<cancer_type>')
def cancer_articles(cancer_type):
    articles = Article.query.filter_by(cancer_type=cancer_type).all()
    return render_template('cancer.html', cancer_type=cancer_type, articles=articles)
