#!/usr/bin/env python3
"""
Digital Market Analysis Agent - Google ADK Implementation

This module defines the main AI agent for digital product market analysis
using Google's Agent Development Kit (ADK) with Gemini 2.0 Flash model.

The agent provides comprehensive market analysis, trend predictions,
and automated reporting capabilities for digital product marketplaces.
"""

import os
import sys
from google.cloud import aiplatform
from google.adk import Agent
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Import analysis functions from parent directory
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agent_tools import (
    analyze_digital_marketplace_with_ai,
    predict_july_2025_trends_ai,
    send_ai_analysis_report,
    run_ai_complete_analysis,
    get_ai_market_summary
)


def run_complete_analysis():
    """
    Execute complete AI-powered market analysis pipeline.
    
    This function orchestrates the full analysis workflow including:
    - Digital marketplace analysis
    - Trend prediction
    - Report generation and email delivery
    
    Returns:
        dict: Analysis results with status and summary information
    """
    try:
        result = run_ai_complete_analysis()
        if result.get('status') == 'success':
            return {
                'status': 'success',
                'analysis_method': 'ai_powered_gemini',
                'summary': 'AI analysis completed successfully',
                'advantages': result.get('advantages', []),
                'confidence': result.get('predictions', {}).get(
                    'confidence_metrics', {}
                ).get('overall_confidence', 'high')
            }
        else:
            return result
    except Exception as e:
        return {
            'status': 'error', 
            'error': str(e), 
            'method': 'ai_powered_gemini'
        }


def get_market_summary():
    """
    Generate a quick AI-powered market summary.
    
    Provides high-level market insights and recommendations
    without full analysis pipeline execution.
    
    Returns:
        dict: Market summary with key insights and recommendations
    """
    try:
        summary = get_ai_market_summary()
        return summary
    except Exception as e:
        return {
            'status': 'error', 
            'error': str(e), 
            'method': 'ai_powered'
        }


# Configure Vertex AI backend through environment variables
os.environ['GOOGLE_GENAI_USE_VERTEXAI'] = 'true'

# Initialize Google Cloud AI Platform
project_id = os.getenv('GOOGLE_CLOUD_PROJECT_ID')
location = os.getenv('GOOGLE_CLOUD_LOCATION', 'us-central1')

if project_id:
    # Set environment variables for Google AI client
    os.environ['GOOGLE_CLOUD_PROJECT'] = project_id
    os.environ['GOOGLE_CLOUD_LOCATION'] = location
    
    try:
        # Initialize AI Platform client
        aiplatform.init(project=project_id, location=location)
        print(f"✅ Initialized AI Platform for project: {project_id}")
    except Exception as e:
        print(f"Warning: Could not initialize AI Platform: {e}")

# Create the ADK agent with Gemini 2.0 Flash model
root_agent = Agent(
    name="digital_market_analysis_agent",
    model="gemini-2.0-flash-exp",
    description=(
        "Advanced AI agent for digital product market analysis and trend prediction. "
        "Analyzes digital marketplaces, predicts market trends, and generates "
        "comprehensive reports with strategic insights and recommendations."
    ),
    tools=[
        run_complete_analysis,
        get_market_summary,
        analyze_digital_marketplace_with_ai,
        predict_july_2025_trends_ai,
        send_ai_analysis_report
    ]
)