import random
from datetime import datetime, timedelta
import time
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Função para gerar dados simulados
def generate_simulated_data():
    vehicles = [
        "ABC-1234", "XYZ-5678", "DEF-9012", "GHI-3456", "JKL-7890", "MNO-4567", "PQR-8901", "STU-2345", "VWX-6789", "YZA-0123",
        "BCD-3456", "EFG-7890", "HIJ-1234", "KLM-5678", "NOP-9012", "QRS-3456", "TUV-7890", "WXY-1234", "ZAB-5678", "CDE-9012"
    ]
    points_of_sale = [
        {"name": "Posto Alpha", "city": "São Paulo", "state": "SP", "lat": -23.55052, "lon": -46.633308},
        {"name": "Posto Beta", "city": "Rio de Janeiro", "state": "RJ", "lat": -22.906847, "lon": -43.172896},
        {"name": "Posto Gamma", "city": "Belo Horizonte", "state": "MG", "lat": -19.916681, "lon": -43.934493},
        {"name": "Posto Delta", "city": "Curitiba", "state": "PR", "lat": -25.428954, "lon": -49.267137},
        {"name": "Posto Epsilon", "city": "Porto Alegre", "state": "RS", "lat": -30.034647, "lon": -51.217658},
        {"name": "Posto Zeta", "city": "Brasília", "state": "DF", "lat": -15.794229, "lon": -47.882166},
        {"name": "Posto Eta", "city": "Fortaleza", "state": "CE", "lat": -3.71722, "lon": -38.543369},
        {"name": "Posto Theta", "city": "Salvador", "state": "BA", "lat": -12.9714, "lon": -38.5014},
        {"name": "Posto Iota", "city": "Florianópolis", "state": "SC", "lat": -27.595377, "lon": -48.54805},
        {"name": "Posto Kappa", "city": "Manaus", "state": "AM", "lat": -3.119028, "lon": -60.021731}
    ]

    common_products = ["Arla 32", "Diesel Comum", "Diesel S-10"]
    less_common_products = ["Gasolina", "Etanol"]

    records = []
    for _ in range(200):  # Aumentar o número de registros simulados
        vehicle = random.choice(vehicles)
        point_of_sale = random.choice(points_of_sale)
        
        # 90% de chance de ser um produto comum, 10% de chance de ser gasolina ou etanol
        if random.random() < 0.9:
            product = random.choice(common_products)
        else:
            product = random.choice(less_common_products)
        
        quantity = random.uniform(50, 200)
        unit_price = random.uniform(4.0, 6.0)
        total_price = quantity * unit_price
        odometer = random.randint(10000, 50000)
        
        # Gerar data/hora aleatória nos últimos 15 dias
        transaction_date = (datetime.now() - timedelta(days=random.randint(0, 15))).isoformat()
        
        records.append({
            "vehicle": vehicle,
            "transaction_date": transaction_date,
            "odometer": odometer,
            "point_of_sale": point_of_sale,
            "product": product,
            "quantity": quantity,
            "unit_price": unit_price,
            "total_price": total_price
        })

    return records

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/data')
def data():
    data = generate_simulated_data()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
