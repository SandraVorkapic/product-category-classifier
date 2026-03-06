Product Category Classifier

Ovaj projekat služi za automatsku klasifikaciju proizvoda na osnovu naslova proizvoda koristeći mašinsko učenje.

Struktura projekta
.
├── data/
│   └── products.csv
├── models/
│   ├── model.pkl
│   └── vectorizer.pkl
├── notebooks/
│   └── analysis.ipynb
├── train_model.py
├── predict_category.py
├── requirements.txt
└── README.md
Instalacija

Kloniraj repozitorij i instaliraj zavisnosti:

git clone https://github.com/SandraVorkapic/product-category-classifier.git
cd product-category-classifier
pip install -r requirements.txt
Korišćenje
Treniranje modela
python train_model.py
Predviđanje kategorije proizvoda
python predict_category.py

Program traži unos naslova proizvoda i vraća predviđenu kategoriju.

Analiza podataka

Notebook notebooks/analysis.ipynb sadrži analizu skupa podataka i pripremu za treniranje modela.