Personal Finance Tracker
This is a simple web application built with Flask for tracking personal expenses. It allows users to add their expenses, view a list of expenses, and visualize expense distribution using a pie chart.

Prerequisites
Before running the application, ensure you have the following dependencies installed: Python, Flask, matplotlib

Getting Started
To run the application, follow these steps:
1. Clone the repository or download the code files.
2. Install the required dependencies by running the following command: pip install flask matplotlib
3. Navigate to the project directory in your terminal.
4. Run the following command to start the Flask development server: python app.py
5. Open your web browser and go to http://localhost:5000 to access the Personal Finance Tracker.

Usage
Adding Expenses
- On the home page, you can add your expenses by filling in the expense details:
  - Expense Name: Enter a descriptive name for the expense.
  - Amount: Specify the expense amount.
  - Date: Select the date when the expense was made.
  - Category: Provide a category for the expense.
- Click on the "Add Expense" button to add the expense.

Viewing Expenses
- To view a list of all expenses, click on the "Expenses" link in the navigation bar.
- The expenses will be displayed in a table format, showing the expense value, date, category, and name.

Pie Chart Visualization
- On the home page, you can find a pie chart that visualizes the distribution of expenses across different categories.
- If there are no expenses recorded, the pie chart will display a message indicating no data available.
- The pie chart provides a visual representation of the proportion of expenses in each category.

Code Structure
- The code files are organized as follows:
  - app.py: This is the main application file that initializes the Flask application, defines the routes, and handles the HTTP requests and responses.
- dashboard.html: This template file contains the HTML structure and styling for the web page. It includes placeholders for displaying expenses, the pie chart, and the expense entry form.
- expenses.html: This template file displays a table of all expenses.
- Other dependencies: The code also imports necessary libraries such as Flask, render_template, request, matplotlib.pyplot, datetime, io.BytesIO, and base64 for various functionalities.
