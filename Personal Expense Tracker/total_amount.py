from flask import Flask, render_template, request
import matplotlib.pyplot as plt
from datetime import datetime
from io import BytesIO
import base64

app = Flask(__name__)
expenses = []
total_amount = 0


@app.route('/', methods=['GET', 'POST'])
def expense_tracker():
    global total_amount

    if request.method == 'POST':
        name = request.form['name']
        amount = round(float(request.form['amount']), 4)
        date = datetime.strptime(request.form['date'], '%Y-%m-%d').strftime('%m/%d/%Y')
        category = request.form['category']
        expenses.append({'name': name, 'amount': amount, 'date': date, 'category': category})
        total_amount += amount

    chart_base64 = generate_pie_chart()

    return render_template('dashboard.html', expenses=expenses, total_amount=total_amount, chart=chart_base64)


@app.route('/expenses')
def show_expenses():
    return render_template('expenses.html', expenses=expenses, total_amount=total_amount)


def generate_pie_chart():
    if not expenses:
        return None

    category_totals = {}
    for expense in expenses:
        category = expense['category']
        amount = expense['amount']
        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount

    labels = list(category_totals.keys())
    sizes = list(category_totals.values())
    explode = [0.05] * len(labels)

    fig, ax = plt.subplots(figsize=(4, 4))

    ax.pie(sizes, labels=labels, explode=explode, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  

    chart_buffer = BytesIO()
    plt.savefig(chart_buffer, format='png')
    chart_buffer.seek(0)
    chart_base64 = base64.b64encode(chart_buffer.getvalue()).decode('utf-8')

    plt.clf()

    return chart_base64


if __name__ == '__main__':
    app.run(debug=True)
