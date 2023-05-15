# Django-AICodeBot

Django-AICodeBot is an open-source project that utilizes Django and a pre-trained AI model to generate Python code based on natural language instructions. This project aims to provide developers with an interactive and efficient tool for generating code snippets and automating repetitive coding tasks.

The AI model behind Django-AICodeBot is trained to understand natural language instructions and convert them into executable Python code. By leveraging the power of AI, developers can write code more quickly and effectively, reducing the time and effort required for manual coding.

## Features

- Natural language to code conversion: Write code instructions in plain English and let the AI model generate the corresponding Python code.
- Interactive code generation: The web interface allows developers to enter instructions, view generated code, and make adjustments as needed.
- Pre-trained AI model: Django-AICodeBot comes with a pre-trained AI model specifically designed for code generation tasks. However, it can also be extended with custom models trained on specific domains or datasets.
- Code customization: Developers have the flexibility to modify and enhance the generated code according to their requirements.
- Code snippet repository: The project includes a repository of commonly used code snippets that can be easily accessed and integrated into projects.

## Installation

To use Django-AICodeBot locally, follow these steps:
Note: Please make sure you have your OpenAI API Key Replaced in the Code.

1. Clone the repository:

   ```shell
   git clone https://github.com/tejayy/Django-AICodeBot.git
   ```

2. Change to the project directory:

   ```shell
   cd Django-AICodeBot
   ```

3. Create a virtual environment (optional but recommended):

   ```shell
   python3 -m venv env
   source env/bin/activate
   ```

4. Install the required dependencies:

   ```shell
   pip install -r requirements.txt
   ```

5. Apply database migrations:

   ```shell
   python manage.py migrate
   ```

6. Start the development server:

   ```shell
   python manage.py runserver
   ```

7. Access the application by visiting `http://localhost:8000` in your web browser.

Note: Please make sure you have Python 3.x and pip installed on your system.

## Usage

1. Open your web browser and access the application at `http://localhost:8000`.

2. Enter a natural language instruction or code snippet in the provided input field.

3. Click the "Generate Code" button to let the AI model process the instruction and generate the corresponding Python code.

4. Review the generated code in the output section. If needed, you can modify the code to fit your requirements.

5. Click the "Copy to Clipboard" button to copy the generated code snippet to the clipboard.

6. You can also explore the code snippet repository to access commonly used code snippets by clicking the "Code Snippets" tab.

## Contributing

Contributions to Django-AICodeBot are welcome! If you would like to contribute to the project, please follow these guidelines:

1. Fork the repository.

2. Create a new branch for your feature or bug fix:

   ```shell
   git checkout -b my-feature
   ```

3. Make your changes and commit them with descriptive commit messages.

4. Push your changes to your forked repository:

   ```shell
   git push origin my-feature
   ```

5. Open a pull request in the main repository, explaining your changes and their benefits.

Please ensure that your contributions adhere to the project's code of conduct.

## License

Django-AICodeBot is released under the [MIT License](https://opensource.org/licenses/MIT). You are free to use, modify, and distribute the code in accordance with the terms of this license.
