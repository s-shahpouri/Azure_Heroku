# Speech-to-Text Transcription App

This project is a web-based application that transcribes audio files into text using Azure Speech-to-Text SDK. It is built with Python, powered by Streamlit, and deployed on Heroku.

## Features
- Upload audio files for transcription.
- Utilizes Azure Speech-to-Text SDK for accurate and fast transcriptions.
- Simple and user-friendly web interface created with Streamlit.
- Secure and scalable deployment on Heroku.

---

## Getting Started

### Prerequisites
To run this project locally, ensure you have the following installed:
- Python 3.8 or later
- [Azure Subscription](https://azure.microsoft.com/en-us/free/) to access the Speech-to-Text service
- [Streamlit](https://streamlit.io/)
- [Azure SDK for Python](https://learn.microsoft.com/en-us/azure/developer/python/)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/s-shahpouri/your-repo-name.git
   ```bash
   cd your-repo-name
   
2. Create and activate a virtual environment:
  ```bash
  python -m venv venv
```bash
  source venv/bin/activate  # On Windows: venv\Scripts\activate

   
3. Install the required packages:
  ```bash
  pip install -r requirements.txt

   
4. Set up your .env file:
  - Create a .env file in the root directory.
  - Add your Azure Speech-to-Text key and region:

  ```bash
  AZURE_SPEECH_KEY=your_azure_key

   

### Local Usage

1. Run the Streamlit app:
  ```bash
streamlit run app.py

   
2. Open the provided URL in your browser (e.g., http://localhost:8501).
3. Upload an audio file and click the "Transcribe" button to see the transcription.

### Deployment

1. Install the Heroku CLI and log in:
  ```bash
heroku login

   
2. Create a Heroku app:

  ```bash
heroku create your-app-name

   
3. Set your environment variables on Heroku:
  ```bash
heroku config:set AZURE_SPEECH_KEY=your_azure_key AZURE_REGION=your_azure_region

   
4. Push your code to Heroku:
  ```bash
git push heroku main

   

## Built With

* [Python](https://www.python.org/) - Programming language
* [Streamlit](https://streamlit.io/) - Web framework
* [Azure Speech-to-Text SDK](https://learn.microsoft.com/en-us/azure/cognitive-services/speech-service/) - Speech recognition
* [Heroku](https://www.heroku.com/) - Deployment platform

---

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## Acknowledgments

* [Azure Speech Service Documentation](https://learn.microsoft.com/en-us/azure/cognitive-services/speech-service/)
* Streamlit Documentation
* Heroku Documentation

