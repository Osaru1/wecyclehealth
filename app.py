
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_message = request.json.get('message')
    response = generate_response(user_message)
    return jsonify({'response': response})

def generate_response(user_message):
    user_message = user_message.lower()  # Convert the user message to lowercase once
    
    # Checking for keywords
    if 'headache' in user_message:
        return 'It seems like you have a headache. Try resting or drinking water.'
    elif 'breast cancer' in user_message:
        return 'For breast cancer, it’s best to consult a doctor.'
    elif any(greeting in user_message for greeting in ['hi', 'hello', 'yo', 'sup']):
        return 'Hi, welcome to WeCycle! We are very pleased to assist you today.'
    elif 'pcos' in user_message:
        return 'Do not worry about PCOS, love your body! Head over to Nutritional log to see the nutritional values on your food! Please consult a doctor.'
    elif any(mental in user_message for mental in ['mental health', 'depression', 'sad', 'suicide', 'depressed']):
        return 'Cheer up!! You are enough!! If it persists, consult a therapist.'
    elif any(offensive in user_message for offensive in ['dick', 'ass', 'fuck', 'pussy']):
        return 'HEY DONT SAY THAT ASSHOLE'
    else:
        return 'Sorry, I didn’t understand. Can you please clarify?'


if __name__ == '__main__':
    app.run(debug=True)