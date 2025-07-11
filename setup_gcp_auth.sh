#!/bin/bash

# Google Cloud Authentication Setup for AI Agent
# This script helps set up authentication for Google Cloud Platform and Vertex AI

set -e

echo "🔐 Setting up Google Cloud Authentication for AI Agent"
echo "=================================================="

# Check if gcloud is installed
if ! command -v gcloud &> /dev/null; then
    echo "❌ Google Cloud CLI not found."
    echo "Please install it first:"
    echo "  macOS: brew install google-cloud-sdk"
    echo "  Linux: https://cloud.google.com/sdk/docs/install"
    echo "  Windows: https://cloud.google.com/sdk/docs/install"
    exit 1
fi

echo "✅ Google Cloud CLI found"

# Check if user is authenticated
if ! gcloud auth list --filter=status:ACTIVE --format="value(account)" | grep -q .; then
    echo "🔑 No active authentication found. Please login:"
    gcloud auth login
fi

echo "✅ User authentication verified"

# Set application default credentials for local development
echo "🔧 Setting up application default credentials..."
gcloud auth application-default login

echo "✅ Application default credentials configured"

# List available projects
echo "📋 Available Google Cloud projects:"
gcloud projects list --format="table(projectId,name,projectNumber)"

echo ""
echo "🎯 Next Steps:"
echo "1. Copy .env.example to .env"
echo "2. Set GOOGLE_CLOUD_PROJECT_ID to your project ID from the list above"
echo "3. Enable required APIs:"
echo "   gcloud services enable aiplatform.googleapis.com --project=YOUR_PROJECT_ID"
echo "4. Install Python dependencies:"
echo "   pip install -r requirements.txt"
echo "5. Run the agent:"
echo "   adk web --port 8080 ai_agent"
echo ""
echo "✅ Authentication setup complete!"