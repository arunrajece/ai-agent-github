# AI-Powered Digital Market Analysis Agent

A comprehensive AI agent built with Google's Agent Development Kit (ADK) that analyzes digital product marketplaces and generates market intelligence reports using Gemini 2.0 Flash.

## 🚀 Features

- **AI-Powered Analysis**: Uses Gemini 2.0 Flash for intelligent market analysis
- **No Web Scraping**: Leverages AI knowledge instead of fragile web scraping
- **Professional Reports**: Generates beautiful HTML reports with interactive sections
- **Email Delivery**: Automated email delivery with SendGrid integration
- **Scalable Deployment**: Ready for local development and cloud deployment
- **Comprehensive Intelligence**: Covers pricing, trends, and strategic insights

## 🏗️ Architecture

```
├── ai_agent/
│   ├── __init__.py                 # Package initialization
│   └── root_agent.py              # Main ADK agent definition
├── agent_tools.py                 # AI analysis functions
├── adk.yaml                       # ADK configuration
├── requirements.txt               # Python dependencies
├── .env.example                   # Environment template
└── setup_gcp_auth.sh             # Authentication setup script
```

## 🔧 Prerequisites

- Python 3.9+
- Google Cloud Platform account
- SendGrid account (for email reports)
- Google Cloud CLI installed

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/arunrajece/ai-digital-market-agent.git
cd ai-digital-market-agent
```

### 2. Set Up Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Google Cloud Authentication

```bash
# Run the authentication setup script
./setup_gcp_auth.sh

# Or manually:
# 1. Install Google Cloud CLI
# 2. Login to Google Cloud
gcloud auth login
gcloud auth application-default login

# 3. Enable required APIs
gcloud services enable aiplatform.googleapis.com --project=YOUR_PROJECT_ID
```

### 5. Configure Environment Variables

```bash
# Copy the environment template
cp .env.example .env

# Edit .env with your configuration
nano .env
```

Required environment variables:

```bash
# Google Cloud Configuration
GOOGLE_GENAI_USE_VERTEXAI=true
GOOGLE_CLOUD_PROJECT_ID=your-gcp-project-id
GOOGLE_CLOUD_LOCATION=us-central1

# SendGrid Configuration
SENDGRID_API_KEY=your-sendgrid-api-key
FROM_EMAIL=your-verified-sender@example.com
TO_EMAIL=recipient@example.com
```

## 🚀 Usage

### Start the AI Agent

```bash
# Launch the ADK web interface
adk web --port 8080
```

### Access the Agent

1. Open your browser to `http://localhost:8080`
2. Interact with the AI agent through the web interface
3. Request market analysis and reports

### Available Commands

The agent provides several analysis tools:

- **Complete Analysis**: Full market analysis with email report
- **Market Summary**: Quick market overview
- **Trend Predictions**: AI-powered trend forecasting
- **Email Reports**: Professional HTML reports delivered via email

## 🧪 Testing

Test individual components:

```bash
# Test the agent structure
python -c "from ai_agent import root_agent; print('✅ Agent loaded successfully')"

# Test email functionality (requires .env configuration)
python -c "
from agent_tools import send_ai_analysis_report
result = send_ai_analysis_report({'predictions': {'hot_categories': ['AI Tools']}}, 'test@example.com')
print(f'Email test result: {result}')
"

# Test complete analysis pipeline
python -c "
from agent_tools import run_ai_complete_analysis
result = run_ai_complete_analysis()
print(f'Analysis result: {result[\"status\"]}')
"
```

## 📊 What the Agent Analyzes

### Digital Platforms
- **Etsy**: Creative digital products, templates, printables
- **Shopify**: E-commerce apps, themes, business tools
- **Gumroad**: Direct creator sales, courses, software
- **Other Platforms**: Creative Market, Envato, Udemy, Patreon

### Analysis Categories
- Market size and growth trends
- Pricing strategies and evolution
- Consumer behavior patterns
- Technology adoption rates
- Seller performance metrics
- Emerging opportunities

### Prediction Areas
- Hot product categories for July 2025
- Pricing evolution forecasts
- Technology integration trends
- Market consolidation patterns
- Success strategies for sellers

## 📈 Sample Output

The agent generates comprehensive reports including:

- **AI-Predicted Hot Categories**: Top trending product categories
- **Pricing Evolution**: Price trend forecasts across market segments
- **Technology Predictions**: Future tech adoption patterns
- **Success Strategies**: AI-recommended approaches for sellers
- **Market Opportunities**: Emerging niches and opportunities

## 🔍 How It Works

### AI-Powered Analysis
Instead of traditional web scraping, the agent uses Gemini 2.0 Flash to:
1. Analyze current market patterns
2. Apply domain knowledge to raw data
3. Generate predictive insights
4. Create professional reports

### Advantages Over Web Scraping
- **Reliability**: No breaking due to website changes
- **Speed**: Instant analysis without loading delays
- **Intelligence**: Understands context and nuances
- **Scalability**: Works in any environment
- **Maintainability**: No fragile scraping code

## 🚀 Deployment

### Local Development
```bash
adk web --port 8080
```

### Cloud Deployment
The agent is ready for deployment to:
- Google Cloud Run
- AWS Lambda
- Azure Functions
- Docker containers

## 🔧 Configuration

### ADK Configuration (`adk.yaml`)
```yaml
name: digital-market-analysis-agent
agent:
  name: digital_market_analysis_agent
  model: gemini-2.0-flash-exp
  description: AI agent for digital market analysis
```

### Environment Variables
- `GOOGLE_GENAI_USE_VERTEXAI`: Enable Vertex AI backend
- `GOOGLE_CLOUD_PROJECT_ID`: Your GCP project ID
- `SENDGRID_API_KEY`: SendGrid API key for email delivery
- `FROM_EMAIL`: Verified sender email address
- `TO_EMAIL`: Report recipient email address

## 📝 Generated Reports

Reports include:
- **Executive Summary**: Key findings and recommendations
- **Market Analysis**: Detailed platform and category analysis
- **Trend Predictions**: Future market forecasts
- **Interactive Sections**: Collapsible detailed data
- **Methodology**: Transparent analysis approach
- **Data Sources**: Clear attribution and limitations

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License. See LICENSE file for details.

## 🙋‍♂️ Support

- **Issues**: [GitHub Issues](https://github.com/arunrajece/ai-digital-market-agent/issues)
- **Documentation**: See README and inline code comments
- **Questions**: Open a GitHub Discussion

## 🔒 Security

- Never commit API keys or credentials
- Use environment variables for sensitive data
- Follow Google Cloud security best practices
- Regularly update dependencies

## 📊 Metrics and Monitoring

The agent provides:
- Execution status and error tracking
- Analysis completion metrics
- Email delivery confirmation
- Performance monitoring capabilities

---

**Built with ❤️ using Google ADK and Gemini 2.0 Flash**