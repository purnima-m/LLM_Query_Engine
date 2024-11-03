# LLM_Query_Engine
## Project Overview
This is a streamlined Q&amp;A application powered by Google’s Gemini Large Language Model (LLM). It provides accurate, real-time answers through a clean and user-friendly Streamlit interface. With secure API handling, Gemini LLM Hub offers a professional, on-demand solution for quick insights.

## Goals
- Develop a simple and interactive Q&A interface using an LLM (Gemini Pro).
- Allow users to input questions and receive AI-generated answers.
- Demonstrate secure handling of API keys using environment variables.

## What We Can Achieve
- **Real-time Q&A**: Users can ask questions and receive answers generated by the Gemini Pro model in real-time.
- **Educational Use**: This app can answer questions on various topics, making it useful for learning and exploration.
- **Customer Support Potential**: With some enhancements, this app could answer frequently asked questions, acting as a virtual assistant.

## How Did We Achieve This?
- Integrated Google’s Generative AI API to access the Gemini Pro model for natural language processing.
- Built the application interface using Streamlit, allowing users to input questions and display the AI-generated responses.
- Managed API keys securely with the `dotenv` library, loading them from a `.env` file and excluding it from the repository using `.gitignore`.

## Tools & Technologies Used
- **Streamlit**: Used to build a simple and interactive web application interface.
- **google-generativeai**: Python library to interact with Google’s Generative AI API and access the Gemini Pro model.
- **python-dotenv**: Used to load environment variables (like the API key) from a `.env` file, ensuring secure and modular access to sensitive data.

## How to Run the Application

### Requirements
- Python 3.x
- Libraries listed in `requirements.txt`

### Setup
1. **Clone the repository**: Download the code from GitHub.
2. **Install dependencies**: Run the following command to install required libraries:
   ```bash
   pip install -r requirements.txt
3. **Set up the API key**:
   - Create a `.env` file in the project directory.
   - Add your Google API key to the `.env` file:
     ```plaintext
     GOOGLE_API_KEY=your_actual_api_key_here
     ```
### Running the Application
1. Start the Streamlit app with this command:
   ```bash
   streamlit run main.py
2. Open the provided URL (typically localhost:8501) in your browser to access the application.

## Project Components

- **main.py**: Contains the primary code for the application, including functions to interact with the Gemini model and display the Q&A interface.
- **.env**: Stores the Google API key (not uploaded to GitHub).
- **requirements.txt**: Lists all the dependencies required to run the project.
- **.gitignore**: Ensures the `.env` file is excluded from version control to keep sensitive data secure.

## Future Enhancements
- **UI Improvements**: Add a more interactive interface with options for different question types or categories.
- **Error Handling**: Improve error handling for cases when the API key is missing or when the model response is delayed.
- **Logging**: Implement logging to track usage patterns and errors.
