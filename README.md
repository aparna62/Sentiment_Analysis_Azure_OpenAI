# Sentiment Analysis Using Azure OpenA
## 📚 Project Scope
 
**Title:** Sentiment Analysis Using Azure OpenAI
 
**Objectives:**
- Use Azure OpenAI GPT models to perform accurate sentiment analysis on text data.
- Leverage Azure's scalable cloud platform for efficient data processing.
- Apply advanced language models to understand context and nuances in text sentiment.
- Compare performance with other sentiment analysis techniques.
- Deliver actionable insights to stakeholders based on data sentiment.
- Demonstrate integration of Azure OpenAI services into real-world analytical apps.

## 🚀 Deliverables
- Comprehensive documentation of project scope, methodology, and tools.
- Cleaned dataset(s) suitable for sentiment analysis (optional if only using live input).
- Implementation of an AI-driven sentiment analysis tool using Azure OpenAI GPT.
- Responsive demo/prototype web application.
- Instructions for setup, configuration, and usage.
  
## 🏗️ Design Description 
The system is engineered for high accuracy and usability in determining sentiment (Positive, Negative, Neutral) from input text.  
It leverages a robust, cloud-based Azure OpenAI backend, with secure preprocessing and modular, scalable architecture. Users interact through an attractive frontend interface, sending text that is preprocessed and analyzed in real time.
 
**Key Features:**
- Secure API key and endpoint management via `.env`
- Robust web interface (Flask + HTML/CSS) for user input and result display
- Cleaned and normalized text processing
- Responsive error handling and attractive UI
  
## 🔄 Workflow
1. **User Input:** Web frontend collects and sends text to backend.
2. **Preprocessing:** Backend cleans and prepares the text.
3. **API Integration:** Text sent securely to Azure OpenAI API.
4. **Analysis:** Model returns "Positive", "Negative", or "Neutral".
5. **Results:** Sentiment displayed on the frontend in real time.

## ✅ Positive Test Cases
 
| Input Example                                                 | Expected Output |
|--------------------------------------------------------------|----------------|
| This product is a game-changer! I couldn't be happier.       | Positive       |
| Loving the new features in the app! Great job, team.         | Positive       |
| I've been using this service for years, and it never disappoints. | Positive   |
 
## ❌ Negative Test Cases
 
| Input Example                             | Expected Output      |
|-------------------------------------------|---------------------|
| This is trash, totally useless, smh.      | Negative            |
| Buy now! Limited offer! Click here.       | No sentiment/error  |
| The meeting is scheduled for 3 PM tomorrow. | Neutral           |
 
## 🛠️ Third-Party Tools & Technologies
 
| Tool/Service        | Purpose                                      |
|---------------------|----------------------------------------------|
| Azure OpenAI        | Access GPT models for sentiment analysis     |
| Python (3.8+)       | Application development                      |
| OpenAI Python SDK   | API integration for Azure OpenAI             |
| Flask               | Lightweight web application framework        |
| Requests            | HTTP requests for API calls                  |
| python-dotenv       | Secure environment variable handling         |
| Git                 | Version control                              |
| Visual Studio Code  | Code editing                                 |
