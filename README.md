# Student Performance Indicator - MLOps Project

This is an End-to-End Machine Learning project that predicts students' math scores based on various demographic and academic factors. The project demonstrates a full MLOps workflow including data ingestion, transformation, model training, and deployment via a Flask web application.

## 🛠️ Project Structure

```
mlops/
│
├── artifacts/              # Generated artifacts (models, preprocessor, datasets)
│   ├── data.csv
│   ├── train.csv
│   ├── test.csv
│   ├── model.pkl
│   └── proprocessor.pkl
│
├── notebook/               # Jupyter Notebooks for experimentation
│   └── EDA STUDENT PERFORMANCE .ipynb
│   └── stud.csv
│
├── src/                    # Source code
│   ├── components/         # ML Components
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   │
│   ├── pipeline/           # Prediction pipeline
│   │   └── predict_pipeline.py
│   │
│   ├── logger.py           # Logging utility
│   ├── exception.py        # Custom exception handling
│   └── utils.py            # Utility functions (save/load objects)
│
├── templates/              # HTML templates for Flask
│   ├── index.html
│   └── home.html
│
├── app.py                  # Flask Application entry point
├── requirement.txt         # Project dependencies
└── setup.py                # Package setup
```

## 🚀 How to Run Step-by-Step

### 1. Environment Setup
First, create a virtual environment (conda or venv) and install dependencies.

```bash
# Clone the repository
git clone https://github.com/Subamprasad/mlops.git
cd mlops

# Install dependencies
pip install -r requirement.txt
```

### 2. Run Data Ingestion & Model Training
The training pipeline ingests data from `notebook/stud.csv`, transforms it, and trains multiple models (Random Forest, XGBoost, CatBoost, etc.) to find the best one.

```bash
# Run the ingestion script (which triggers transformation and training)
python -m src.components.data_ingestion
```

**Output:**
- The script will split data into train/test.
- It will create `proprocessor.pkl` (scaling/encoding logic) in `artifacts/`.
- It will train models, select the best one (score > 0.6), and save it as `model.pkl` in `artifacts/`.
- You will see the R2 Score of the best model in the terminal.

### 3. Run the Web Application
Start the Flask app to use the prediction interface.

```bash
python app.py
```

- Open your browser and go to: `http://localhost:5000`
- Click on "Predict your data" or navigate to `http://localhost:5000/predictdata`
- Fill in the form (Gender, Ethnicity, Scores, etc.) and click **Predict**.

## 🔧 Technologies Used
- **Python 3.8+**
- **Flask** (Web Framework)
- **Scikit-Learn, CatBoost, XGBoost** (Machine Learning)
- **Pandas, NumPy** (Data Manipulation)
- **Logging & Exception Handling** (Custom implementations)
