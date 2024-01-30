import pytest
from flask import Flask
from app import predict_insurance

@pytest.fixture
def app():
    app = Flask(__name__)
    app.config['TESTING'] = True
    app.config['DEBUG'] = False  # Set to True if you want detailed error messages
    app.add_url_rule('/predict', 'predict_insurance', predict_insurance, methods=['POST'])
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_predict_insurance(client):
    # Prepare test data
    test_data = {
        'exercise': 1,
        'junkFood': 1,
        'smoking': 1,
        'alcohol': 1,
        'sedentary': 1,
        'stress': 1,
        'drug': 1,
        'age': 10,
        'sex': 1,
        'weight': 70,
        'height': 170,
        'children': 2,
        'region': 1,
        'disease': 1  # Replace with an actual disease
    }

    # Make a POST request to the Flask app
    response = client.post('/predict', json=test_data, content_type='application/json')

    # Check if the response status code is 200 (OK)
    assert response.status_code == 200

    # Parse the JSON response
    result = response.get_json()

    # Check if the expected keys are present in the result
    assert 'message' in result
    assert 'type' in result
    assert 'text11_header' in result
    assert 'text11' in result
# Comments
