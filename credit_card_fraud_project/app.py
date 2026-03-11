from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    
    if request.method == 'POST':
        # 1. Retrieve form data
        try:
            amount = float(request.form['amount'])
            time = request.form['time']  # Format: "HH:MM"
            location = request.form['location']
            merchant = request.form['merchant']
            tx_count = int(request.form['tx_count'])
            
            # 2. Initialize Risk Score
            risk_score = 0
            
            # 3. Fraud Detection Logic (Rule-based Simulation)
            
            # Rule A: High Transaction Amount
            if amount > 5000:
                risk_score += 40
            elif amount > 1000:
                risk_score += 20
                
            # Rule B: Unusual Time (e.g., Midnight to 5 AM)
            hour = int(time.split(':')[0])
            if hour >= 0 and hour < 5:
                risk_score += 20
                
            # Rule C: High-Risk Locations
            if location == 'International':
                risk_score += 25
            elif location == 'Unrecognized IP/Device':
                risk_score += 35
                
            # Rule D: High-Risk Merchants
            if merchant in ['Crypto Exchange', 'Online Casino', 'Wire Transfer']:
                risk_score += 20
                
            # Rule E: Rapid Successive Transactions
            if tx_count > 10:
                risk_score += 35
            elif tx_count > 5:
                risk_score += 15
                
            # 4. Finalize Score & Classify
            # Cap the maximum risk score at 100%
            risk_score = min(risk_score, 100)
            
            # Threshold: If score is 50% or more, flag as Fraud
            if risk_score >= 50:
                status = "Potential Fraud"
                status_class = "fraud" # Used for CSS styling (Red)
            else:
                status = "Safe Transaction"
                status_class = "safe"  # Used for CSS styling (Green)
                
            # 5. Pack result to send to frontend
            result = {
                'score': risk_score,
                'status': status,
                'status_class': status_class,
                'amount': f"${amount:,.2f}",
                'tx_count': tx_count
            }
            
        except Exception as e:
            result = {'error': 'Invalid input. Please check your data and try again.'}

    return render_template('index.html', result=result)

if __name__ == '__main__':
    # Run the application in debug mode for easy development
    app.run(debug=True)