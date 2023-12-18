# app.py

from flask import Flask, render_template, request

app = Flask(__name__)

def choose_credit_card(cards, purchase_amount, category):
    max_rewards = 0
    selected_card = None

    for card_name, categories in cards.items():
        if category in categories:
            rewards_rate = categories[category]
            rewards = rewards_rate * purchase_amount
            if rewards > max_rewards:
                max_rewards = rewards
                selected_card = card_name

    return selected_card

@app.route('/', methods=['GET', 'POST'])
def index():
    selected_card = None
    category = None

    if request.method == 'POST':
        purchase_amount = float(request.form['purchase_amount'])
        category = request.form['category']

        # Example credit cards and their rewards rates for different categories (as percentages)
        credit_cards = {
        "Bilt": {"dining": 5,"travel": 2,"lyft": 3, "rent": 1, "shopping": 1},
        "ChaseSapphirePreferred": {"dining": 3, "streaming": 3, "online groceries": 3, "travel": 2, "groceries": 2},
        "ChaseSapphireReserve": {"shopping": 4, "gas": 3}
        # Add more cards and categories as needed
    }

        # Choose the best credit card for the given category
        selected_card = choose_credit_card(credit_cards, purchase_amount, category)

        # Generate static HTML content
        with open("docs/index.html", "w") as f:
            if selected_card:
                f.write(f"<p>Use {selected_card} for maximum rewards in the {category} category.</p>")
            else:
                f.write(f"<p>No cards available for the {category} category.</p>")

    return render_template('index.html', selected_card=selected_card, category=category)

if __name__ == '__main__':
    app.run(debug=True)
