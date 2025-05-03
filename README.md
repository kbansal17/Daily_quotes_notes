# Daily Quote + Notes Flask App

This is a simple Flask web application that displays a new inspirational quote every day and allows users to write, view, edit, and delete personal notes. The app includes colorful animations, fun fonts, and an engaging user interface. It's designed to make it easy to manage daily thoughts and notes.

## Features

- **Daily Quote**: Displays a random quote each day.
- **Write Notes**: Add personal notes with timestamps.
- **View Notes**: View saved notes with options to delete or edit them.
- **Animations & Style**: Colorful, animated interface for an engaging user experience.

## Technologies Used

- **Flask**: A lightweight Python web framework.
- **HTML/CSS**: Basic frontend development with custom styles.
- **JavaScript (optional)**: For form validation and interactive elements.

## How to Run Locally

1. **Clone the repository**:
    ```bash
    git clone https://github.com/USERNAME/daily-quote-notes-app.git
    ```

2. **Navigate into the project folder**:
    ```bash
    cd daily-quote-notes-app
    ```

3. **Set up a virtual environment** (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # For Linux/MacOS
    venv\Scripts\activate  # For Windows
    ```

4. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

5. **Run the Flask app**:
    ```bash
    python app.py
    ```

6. Open your browser and go to `http://127.0.0.1:5000/` to use the app.

## File Structure

- `app.py`: The main Flask application file.
- `templates/`: Contains HTML templates for rendering the app pages (index, notes, and edit).
- `notes.json`: Stores the user's notes (will be created automatically when a note is added).

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

