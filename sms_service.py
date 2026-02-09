"""
SMS service module for Shemsu SMS application.
Provides functionality to send SMS messages using different providers.
"""
import logging
from typing import Dict, Optional

from config import config

# Set up logging
logging.basicConfig(
    level=getattr(logging, config.LOG_LEVEL),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class SMSService:
    """Base SMS service class."""
    
    def __init__(self):
        self.provider = config.SMS_PROVIDER
        logger.info(f"SMS Service initialized with provider: {self.provider}")
    
    def send_sms(self, to_number: str, message: str) -> Dict[str, any]:
        """
        Send an SMS message.
        
        Args:
            to_number: The recipient's phone number (E.164 format recommended)
            message: The message content to send
            
        Returns:
            Dict with status and message details
        """
        if self.provider == 'mock':
            return self._send_mock_sms(to_number, message)
        elif self.provider == 'twilio':
            return self._send_twilio_sms(to_number, message)
        elif self.provider == 'nexmo':
            return self._send_nexmo_sms(to_number, message)
        else:
            raise ValueError(f"Unsupported SMS provider: {self.provider}")
    
    def _send_mock_sms(self, to_number: str, message: str) -> Dict[str, any]:
        """
        Mock SMS sending for testing purposes.
        
        Args:
            to_number: The recipient's phone number
            message: The message content
            
        Returns:
            Dict with mock success response
        """
        logger.info(f"[MOCK] Sending SMS to {to_number}")
        logger.info(f"[MOCK] Message: {message}")
        
        return {
            'success': True,
            'provider': 'mock',
            'to': to_number,
            'message': message,
            'status': 'sent',
            'message_id': 'mock_msg_12345'
        }
    
    def _send_twilio_sms(self, to_number: str, message: str) -> Dict[str, any]:
        """
        Send SMS using Twilio.
        
        Note: Requires twilio package and proper configuration.
        Install with: pip install twilio
        """
        try:
            from twilio.rest import Client
            
            client = Client(config.TWILIO_ACCOUNT_SID, config.TWILIO_AUTH_TOKEN)
            message_obj = client.messages.create(
                body=message,
                from_=config.TWILIO_PHONE_NUMBER,
                to=to_number
            )
            
            logger.info(f"[TWILIO] SMS sent successfully. SID: {message_obj.sid}")
            
            return {
                'success': True,
                'provider': 'twilio',
                'to': to_number,
                'message': message,
                'status': message_obj.status,
                'message_id': message_obj.sid
            }
        except ImportError:
            logger.error("Twilio package not installed. Install with: pip install twilio")
            return {
                'success': False,
                'error': 'Twilio package not installed'
            }
        except Exception as e:
            logger.error(f"[TWILIO] Error sending SMS: {str(e)}")
            return {
                'success': False,
                'error': str(e)
            }
    
    def _send_nexmo_sms(self, to_number: str, message: str) -> Dict[str, any]:
        """
        Send SMS using Nexmo/Vonage.
        
        Note: Requires nexmo package and proper configuration.
        Install with: pip install nexmo
        """
        try:
            import nexmo
            
            client = nexmo.Client(
                key=config.NEXMO_API_KEY,
                secret=config.NEXMO_API_SECRET
            )
            
            response = client.send_message({
                'from': config.NEXMO_PHONE_NUMBER,
                'to': to_number,
                'text': message
            })
            
            if response['messages'][0]['status'] == '0':
                logger.info(f"[NEXMO] SMS sent successfully")
                return {
                    'success': True,
                    'provider': 'nexmo',
                    'to': to_number,
                    'message': message,
                    'status': 'sent',
                    'message_id': response['messages'][0]['message-id']
                }
            else:
                error_text = response['messages'][0]['error-text']
                logger.error(f"[NEXMO] Error: {error_text}")
                return {
                    'success': False,
                    'error': error_text
                }
        except ImportError:
            logger.error("Nexmo package not installed. Install with: pip install nexmo")
            return {
                'success': False,
                'error': 'Nexmo package not installed'
            }
        except Exception as e:
            logger.error(f"[NEXMO] Error sending SMS: {str(e)}")
            return {
                'success': False,
                'error': str(e)
            }
    
    def validate_phone_number(self, phone_number: str) -> bool:
        """
        Basic phone number validation.
        
        Args:
            phone_number: Phone number to validate
            
        Returns:
            True if valid, False otherwise
        """
        # Basic validation - should start with + and contain only digits after that
        if not phone_number:
            return False
        
        if phone_number.startswith('+'):
            return phone_number[1:].isdigit() and len(phone_number) > 8
        
        return phone_number.isdigit() and len(phone_number) >= 10
