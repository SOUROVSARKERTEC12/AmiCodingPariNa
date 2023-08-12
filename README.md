# Ami Coding Pari Na Web Application

Ami Coding Pari Na is a web application that allows users to perform searches on input values and stores them in a database along with user information. This README provides an overview of the project's structure, features, and usage instructions.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Features

- User registration and authentication
- Input value search functionality
- Storing input values in a database with user information
- API endpoint for retrieving user input values within a date range
- Dynamic navigation links based on user authentication status

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/ami-coding-pari-na.git

2. Navigate to the project directory:

   ```bash
   cd ami-coding-pari-na
   pip install -r requirements.txt
3. Run the development server:
    ```bash
   python manage.py runserver

##  Usage
1. Access the application in your web browser at http://127.0.0.1:8000/.
2. Register an account and log in to use the application.
3. Visit the "Khoj the Search" page to perform input value searches and see the search results.
4. Explore the API endpoints to retrieve user input values within a date range.

## API Endpoints
*   Get All Input Values
    * Endpoint: /api/get_all_input_values/
    * Parameters: start_datetime, end_datetime, user_id 
    * Returns: JSON response containing user input values within the specified date range.

## Contributing
Contributions to this project are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
