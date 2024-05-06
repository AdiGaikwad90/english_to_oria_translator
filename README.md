# English-Odia Translator Web Application

Welcome to the English-Odia Translator web application! This application allows users to translate English text into Odia language quickly and easily. It provides a simple interface for entering English text and selecting Odia as the destination language for translation.

## Project Structure

Here's a detailed breakdown of the project structure and what each file contains:

1. **app.py**:
   - This file contains the Flask application setup and route definitions.
   - It includes routes for rendering the HTML template (`index.html`) and handling translation requests.
   - The translation route uses the `mtranslate` library to perform English-Odia translation.
   - It also handles both JSON and form data for translation requests.

2. **templates/index.html**:
   - This HTML file serves as the main template for the web application.
   - It includes a form for users to enter English text and select the destination language.
   - JavaScript is used to handle form submission via AJAX and update the page dynamically with the translated text.

3. **static/css/style.css**:
   - This CSS file contains styles for the HTML elements in the `index.html` template.
   - It defines the visual appearance of the user interface, including fonts, colors, margins, and padding.

4. **static/js/script.js**:
   - This JavaScript file contains client-side code to handle form submission and AJAX requests.
   - It listens for form submission events, captures the input data, sends a POST request to the Flask server, and updates the page with the translated text.

5. **requirements.txt**:
   - This file lists the Python dependencies required for the project.
   - It includes Flask for the web framework and mtranslate for performing translation.

6. **venv/** (optional):
   - This directory contains the virtual environment used for the project.
   - It is created when setting up the virtual environment using `python -m venv venv`.
   - It includes Python packages installed within the virtual environment to isolate project dependencies.


## Usage

To use the translator web application, follow these steps:

1. **Clone the Repository**: Clone the repository to your local machine using Git:

    ```bash
    git clone https://github.com/your-username/english-to-odia-translator.git
    ```

2. **Navigate to the Project Directory**: Change into the project directory:

    ```bash
    cd english-to-odia-translator
    ```

3. **Set Up a Virtual Environment** (optional but recommended): Set up a virtual environment to isolate project dependencies:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    # or
    .\venv\Scripts\activate  # On Windows
    ```

4. **Install Dependencies**: Install the required dependencies listed in the `requirements.txt` file:

    ```bash
    pip install -r requirements.txt
    ```

5. **Start the Flask Server**: Run the Flask development server:

    ```bash
    python app.py
    ```

6. **Access the Web Application**: Open your web browser and go to `http://localhost:5000` to access the translator web application.

7. **Translate Text**: Enter English text into the input field, select "Odia" as the destination language from the dropdown menu, and click the "Translate" button to see the translated text.

## API Usage

If you want to test the translation API on localhost using tools like Postman, follow these steps:

1. **Send a POST Request**: Send a POST request to `http://localhost:5000/translate` with the following payload:

    ```json
    {
        "input_text": "Hello, how are you?",
        "dest_language": "or"
    }
    ```

    - Replace `"input_text"` with the English text you want to translate.
    - Replace `"dest_language"` with `"or"` for Odia language.

2. **Set Content-Type Header**: Ensure that the Content-Type header of the request is set to `application/json`.

3. **Receive Translated Text**: You should receive a JSON response with the translated text.

## Future Scope

This project can be further enhanced in several ways:

- **User Authentication**: Implement user authentication to allow registered users to save their translation history or personalize their experience.
- **Improved UI/UX**: Enhance the user interface with additional features such as error handling, input validation, and better feedback messages.
- **Support for More Languages**: Extend the translator to support additional languages apart from English and Odia.
- **Offline Mode**: Implement offline functionality using service workers to enable translation even without an internet connection.
- **Integration with External APIs**: Integrate with external translation APIs to improve translation accuracy and support more languages.

## Contributing

Contributions to this project are welcome! If you have any ideas for improvements or bug fixes, feel free to submit a pull request. Please follow the existing code style and guidelines when making changes.

## License

This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute the code as per the terms of the license.
