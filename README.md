# Food Lover App

FoodLover is a comprehensive software solution designed to boost the food ordering and delivery process for both customers and food stores. This section provides an overview of the system’s key features including its purpose, functions, characteristics and dependencies.

## Features

1. **Login and Registration**:
   - Users can log in with their email and password.
   - New users can register by providing their name, email, and password.

2. **Main Window**:
   - The main window displays the login and registration forms.
   - Users can click the "Login" or "Register" buttons to navigate to the respective screens.

3. **Login Validation**:
   - The app validates user input during login:
     - If the email or password fields are empty, an error message is displayed.
     - If the email exists in the database but the password is incorrect, an error message is shown.
     - If the email is not found in the database, the user is informed.

4. **Registration Validation**:
   - During registration:
     - The app checks if the email is already registered.
     - If the email is already in use, an error message is displayed.
     - Otherwise, the user's data is inserted into the database.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/food-lover-app.git
   ```

2. Install the required dependencies:
   ```bash
   pip install PyQt5 pymongo
   ```

3. Set up MongoDB:
   - Create a MongoDB Atlas account and set up a cluster.
   - Replace the connection string in `main.py` with your own.

4. Run the app:
   ```bash
   python main.py
   ```

## Credits

- Developed by [Team F]

---
