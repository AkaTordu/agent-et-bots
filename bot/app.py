from flask import Flask, request, jsonify, render_template
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load the dataset
file_path = './ParisHousingClass.csv'
data = pd.read_csv(file_path)

# Preprocess the data
data.dropna(inplace=True)
le = LabelEncoder()
data['category'] = le.fit_transform(data['category'])  # Encode the target variable

# Select features and target
X = data.drop('category', axis=1)
y = data['category']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalize numerical features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train the model
clf = RandomForestClassifier(random_state=42)
clf.fit(X_train, y_train)

# Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    user_input = request.json
    user_features = pd.DataFrame([user_input])
    user_features = scaler.transform(user_features)
    prediction = clf.predict(user_features)
    category = le.inverse_transform(prediction)
    return jsonify({'category': category[0]})

if __name__ == '__main__':
    app.run(debug=True)
