import matplotlib.pyplot as plt
import numpy as np
import json


def load_transactions(filepath="data/transactions.json"):
    with open(filepath, "r") as file:
        transactions = json.load(file)
    return transactions


def process_data(transactions):
    income_categories = ["Salary", "Pension", "Interest", "Others"]
    expense_categories = ["Food", "Rent", "Clothing", "Car", "Health", "Others"]

    income_sums = {category: 0 for category in income_categories}
    expense_sums = {category: 0 for category in expense_categories}

    for transaction in transactions:
        if transaction["type"] == "Income":
            if transaction["category"] in income_sums:
                income_sums[transaction["category"]] += transaction["amount"]
        elif transaction["type"] == "Expense":
            if transaction["category"] in expense_sums:
                expense_sums[transaction["category"]] += transaction["amount"]

    return income_sums, expense_sums


def bar_chart(income_sums, expense_sums):
    categories = list(income_sums.keys()) + list(expense_sums.keys())
    values = list(income_sums.values()) + list(expense_sums.values())

    fig, ax = plt.subplots()
    index = np.arange(len(categories))
    bar_width = 0.35

    ax.bar(
        index[: len(income_sums)], list(income_sums.values()), bar_width, label="Income"
    )
    ax.bar(
        index[len(income_sums) :],
        list(expense_sums.values()),
        bar_width,
        label="Expenses",
    )

    ax.set_xlabel("Category")
    ax.set_ylabel("Amount")
    ax.set_title("Income and Expenses by Category")
    ax.set_xticks(index)
    ax.set_xticklabels(categories, rotation=45)
    ax.legend()

    plt.tight_layout()
    return fig


def pie_chart(transactions, chart_type="Income"):
    # filter transactions based on type
    filtered_transactions = [t for t in transactions if t["type"] == chart_type]

    # aggregate data by category
    category_sums = {}
    for transaction in filtered_transactions:
        if transaction["category"] in category_sums:
            category_sums[transaction["category"]] += transaction["amount"]
        else:
            category_sums[transaction["category"]] = transaction["amount"]

    # data for plotting
    labels = list(category_sums.keys())
    sizes = list(category_sums.values())

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)
    ax.axis("equal")

    plt.title(f"{chart_type} Categories Pie Chart")
    return fig
