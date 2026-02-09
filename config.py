"""
Configuration management for Shemsu SMS application.
"""
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Config:
    """Application configuration class."""
    
    # SMS Provider settings
    SMS_PROVIDER = os.getenv('SMS_PROVIDER', 'mock')  # Options: 'twilio', 'vonage', 'mock'
    
    # Twilio Configuration (if using Twilio)
    TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID', '')
    TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN', '')
    TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER', '')
    
    # Vonage Configuration (if using Vonage, formerly Nexmo)
    VONAGE_API_KEY = os.getenv('VONAGE_API_KEY', '')
    VONAGE_API_SECRET = os.getenv('VONAGE_API_SECRET', '')
    VONAGE_PHONE_NUMBER = os.getenv('VONAGE_PHONE_NUMBER', '')
    
    # Application settings
    DEBUG = os.getenv('DEBUG', 'True').lower() == 'true'
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')


# Create config instance
config = Config()
