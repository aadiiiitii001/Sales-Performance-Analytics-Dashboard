from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

# Load dataset
df = pd.read_csv("sales_data.csv")

@app.route('/')
def home():
    return {"message": "Sales API is running!"}

@app.route('/sales', methods=['GET'])
def get_sales():
    return jsonify(df.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
