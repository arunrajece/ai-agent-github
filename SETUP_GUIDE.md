# Complete Setup Guide for AI Digital Market Analysis Agent

This guide provides step-by-step instructions for setting up and running the AI agent locally, perfect for following along with the Medium post.

## 📋 Prerequisites Checklist

Before starting, ensure you have:

- [ ] Python 3.9 or higher installed
- [ ] Google Cloud Platform account
- [ ] SendGrid account (free tier available)
- [ ] Git installed
- [ ] Text editor (VS Code recommended)

## 🚀 Step-by-Step Setup

### Step 1: Clone and Setup Project

```bash
# Clone the repository
git clone https://github.com/yourusername/ai-digital-market-agent.git
cd ai-digital-market-agent

# Create virtual environment
python -m venv ai_agent_env

# Activate virtual environment
# On macOS/Linux:
source ai_agent_env/bin/activate
# On Windows:
ai_agent_env\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Step 2: Google Cloud Platform Setup

#### 2.1 Install Google Cloud CLI

**macOS:**
```bash
brew install google-cloud-sdk
```

**Windows:**
Download from: https://cloud.google.com/sdk/docs/install

**Linux:**
```bash
curl https://sdk.cloud.google.com | bash
exec -l $SHELL
```

#### 2.2 Authenticate and Configure

```bash
# Login to Google Cloud
gcloud auth login

# Set up application default credentials
gcloud auth application-default login

# Create a new project (or use existing)
gcloud projects create your-ai-agent-project --name="AI Agent Project"

# Set the project
gcloud config set project your-ai-agent-project

# Enable required APIs
gcloud services enable aiplatform.googleapis.com
gcloud services enable compute.googleapis.com
```

### Step 3: SendGrid Setup

#### 3.1 Create SendGrid Account
1. Go to https://sendgrid.com/
2. Sign up for free account
3. Verify your email address

#### 3.2 Get API Key
1. Go to SendGrid Dashboard
2. Navigate to Settings > API Keys
3. Create new API Key with "Full Access"
4. Copy the API key (you won't see it again!)

#### 3.3 Verify Sender Email
1. Go to Marketing > Sender Authentication
2. Verify your sender email address
3. Complete the verification process

### Step 4: Environment Configuration

```bash
# Copy environment template
cp .env.example .env

# Edit the .env file
nano .env  # or use your preferred editor
```

**Fill in your .env file:**

```bash
# Google Cloud Configuration
GOOGLE_GENAI_USE_VERTEXAI=true
GOOGLE_CLOUD_PROJECT_ID=your-ai-agent-project
GOOGLE_CLOUD_LOCATION=us-central1

# SendGrid Configuration  
SENDGRID_API_KEY=SG.your-sendgrid-api-key-here
FROM_EMAIL=your-verified-email@example.com
TO_EMAIL=recipient@example.com

# Optional Configuration
ANALYSIS_DEPTH=detailed
PREDICTION_MONTHS=12
PORT=8080
```

### Step 5: Test the Setup

#### 5.1 Test Google Cloud Connection
```bash
python -c "
import os
from dotenv import load_dotenv
load_dotenv()
print('Project ID:', os.getenv('GOOGLE_CLOUD_PROJECT_ID'))
print('Location:', os.getenv('GOOGLE_CLOUD_LOCATION'))
"
```

#### 5.2 Test Agent Import
```bash
python -c "
from ai_agent import root_agent
print('✅ Agent loaded successfully')
print('Agent name:', root_agent.name)
print('Model:', root_agent.model)
print('Tools:', len(root_agent.tools))
"
```

#### 5.3 Test Email Configuration
```bash
python -c "
import os
from dotenv import load_dotenv
load_dotenv()
print('SendGrid API Key:', 'SET' if os.getenv('SENDGRID_API_KEY') else 'MISSING')
print('From Email:', os.getenv('FROM_EMAIL'))
print('To Email:', os.getenv('TO_EMAIL'))
"
```

### Step 6: Run the Agent

```bash
# Start the ADK web interface
adk web --port 8080 ai_agent
```

You should see:
```
✅ Initialized AI Platform for project: your-ai-agent-project
Starting ADK web server on port 8080...
```

### Step 7: Access and Test

1. Open your browser to `http://localhost:8080`
2. You should see the ADK interface
3. Try asking the agent: "Run a complete market analysis"
4. Check your email for the generated report

## 🔧 Troubleshooting

### Common Issues and Solutions

#### Issue: "gcloud not found"
**Solution:** Install Google Cloud CLI and restart terminal

#### Issue: "Authentication failed"
**Solution:** 
```bash
gcloud auth login
gcloud auth application-default login
```

#### Issue: "API not enabled"
**Solution:**
```bash
gcloud services enable aiplatform.googleapis.com --project=your-project-id
```

#### Issue: "SendGrid authentication failed"
**Solution:** 
- Verify API key is correct
- Check sender email is verified
- Ensure API key has proper permissions

#### Issue: "Agent import failed"
**Solution:**
- Verify virtual environment is activated
- Check all dependencies are installed: `pip install -r requirements.txt`

#### Issue: "Email not received"
**Solution:**
- Check spam/junk folder
- Verify TO_EMAIL is correct
- Check SendGrid dashboard for delivery status

### Debug Commands

```bash
# Check Python version
python --version

# Check installed packages
pip list

# Check environment variables
python -c "import os; print(os.getenv('GOOGLE_CLOUD_PROJECT_ID'))"

# Test Google Cloud access
gcloud auth list
gcloud projects list

# Check ADK installation
python -c "import google.adk; print('ADK version:', google.adk.__version__)"
```

## 📝 Verification Steps

Before proceeding, verify:

- [ ] Virtual environment is activated
- [ ] All dependencies are installed
- [ ] Google Cloud authentication is working
- [ ] SendGrid API key is valid
- [ ] Agent can be imported successfully
- [ ] ADK web server starts without errors
- [ ] Agent responds to queries
- [ ] Email reports are delivered

## 🎯 Next Steps

Once setup is complete:

1. **Explore the Agent**: Try different analysis requests
2. **Customize Reports**: Modify the HTML report templates
3. **Add Features**: Extend the agent with new tools
4. **Deploy to Cloud**: Use the provided deployment scripts
5. **Monitor Usage**: Track agent performance and usage

## 📚 Additional Resources

- [Google ADK Documentation](https://cloud.google.com/agent-builder/docs)
- [Vertex AI Documentation](https://cloud.google.com/vertex-ai/docs)
- [SendGrid API Documentation](https://docs.sendgrid.com/api-reference)
- [Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html)

## 🆘 Getting Help

If you encounter issues:

1. Check the troubleshooting section above
2. Review the logs for error messages
3. Verify your configuration matches the guide
4. Check GitHub issues for similar problems
5. Open a new issue with detailed error information

---

**Happy coding! 🚀**