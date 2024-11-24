# Remove-Punctuations-using-Django
This is a simple web application built using Django and HTML that allows users to input text and remove all punctuation marks. The application is designed to clean up any text by eliminating unnecessary characters, such as commas, periods, exclamation marks, question marks, and more, leaving only the words.

Features:
- Text Input: Users can input text through a textarea.
- Punctuation Removal: Users can check a box to remove all punctuation from the text.
- Clean Output: The cleaned text (without punctuation) is displayed on a new page.
- Easy to Use: Simple form-based interface for submitting text and selecting options

Technologies Used:
- Django: A high-level Python web framework for building the web application.
- HTML: For the front-end structure, including the form and text display.

1.Clone this repository:
git clone https://github.com/7310038081/Remove-Punctuations-using-Django

2.Navigate into the project folder:
cd .\Project\textutils  

3.Run the Django development server:
python manage.py runserver

4.Open your browser and navigate to:
http://127.0.0.1:8000/

How It Works:
The user navigates to the homepage where they can input a block of text into a form.
After submitting the form, if the "Remove Punctuation" checkbox is checked, the text will be processed by the server to remove all punctuation marks.
The cleaned text is displayed on a new page with the processed content.

Example Use Case:
- Content Clean-up: Remove punctuation from text that needs to be cleaned up before further processing or analysis.
- Data Preprocessing: Ideal for scenarios where text data needs to be stripped of non-essential symbols before performing tasks like tokenization or sentiment analysis.

Future Enhancements:
1. Add more text processing options (e.g., removing whitespace, converting text to lowercase).
2. Add a feature to save or download the cleaned text.
3. Extend the application to handle text files or bulk text inputs.


![Screenshot (308)](https://github.com/user-attachments/assets/e30c5760-9778-4ce5-9ca3-8b052d98f430)
![Screenshot (310)](https://github.com/user-attachments/assets/eb7c8bdc-b822-49ac-b563-0f32f21301a9)
![Screenshot (311)](https://github.com/user-attachments/assets/d4e4f8ae-62cd-4959-be9f-c787115b40f7)





