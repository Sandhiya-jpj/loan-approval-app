from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Temporary in-memory store for loans
loans = []

@app.route('/api/loans', methods=['GET'])
def get_loans():
    return jsonify(loans)

@app.route('/api/loans', methods=['POST'])
def add_loan():
    data = request.get_json()

    # Basic validation (optional)
    required_fields = ['borrower_name', 'amount', 'interest_rate', 'term_months']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing fields'}), 400

    loans.append(data)
    return jsonify({'message': 'Loan added successfully'}), 201

if __name__ == '__main__':
    app.run(debug=True, port=5000)
{
  "borrower_name": "John Doe",
  "amount": 1000,
  "interest_rate": 5,
  "term_months": 12
}

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


