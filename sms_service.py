"""
SMS service module for Shemsu SMS application.
Provides functionality to send SMS messages using different providers.
"""
import logging
from typing import Dict, Any

from config import config

# Set up logging
logging.basicConfig(
    level=getattr(logging, config.LOG_LEVEL),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Phone number validation constants
MIN_PHONE_DIGITS = 10  # Minimum number of digits in a phone number


class SMSService:
    """Base SMS service class."""
    
    def __init__(self):
        self.provider = config.SMS_PROVIDER
        logger.info(f"SMS Service initialized with provider: {self.provider}")
    
    def send_sms(self, to_number: str, message: str) -> Dict[str, Any]:
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
        elif self.provider == 'vonage':
            return self._send_vonage_sms(to_number, message)
        else:
            raise ValueError(f"Unsupported SMS provider: {self.provider}")
    
    def _send_mock_sms(self, to_number: str, message: str) -> Dict[str, Any]:
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
    
    def _send_twilio_sms(self, to_number: str, message: str) -> Dict[str, Any]:
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
    
    def _send_vonage_sms(self, to_number: str, message: str) -> Dict[str, Any]:
        """
        Send SMS using Vonage (formerly Nexmo).
        
        Note: Requires vonage package and proper configuration.
        Install with: pip install vonage
        
        API may vary by Vonage SDK version. This is a basic implementation.
        Refer to Vonage documentation for the latest API: https://developer.vonage.com/
        """
        try:
            import vonage
            
            client = vonage.Client(
                key=config.VONAGE_API_KEY,
                secret=config.VONAGE_API_SECRET
            )
            
            # Note: API syntax may vary by SDK version
            # For newer versions, you might need to use:
            # from vonage import Sms
            # sms = vonage.Sms(client)
            # response = sms.send_message({...})
            
            response = client.sms.send_message({
                'from': config.VONAGE_PHONE_NUMBER,
                'to': to_number,
                'text': message
            })
            
            if response['messages'][0]['status'] == '0':
                logger.info(f"[VONAGE] SMS sent successfully")
                return {
                    'success': True,
                    'provider': 'vonage',
                    'to': to_number,
                    'message': message,
                    'status': 'sent',
                    'message_id': response['messages'][0]['message-id']
                }
            else:
                error_text = response['messages'][0]['error-text']
                logger.error(f"[VONAGE] Error: {error_text}")
                return {
                    'success': False,
                    'error': error_text
                }
        except ImportError:
            logger.error("Vonage package not installed. Install with: pip install vonage")
            return {
                'success': False,
                'error': 'Vonage package not installed'
            }
        except Exception as e:
            logger.error(f"[VONAGE] Error sending SMS: {str(e)}")
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
            # With '+' prefix: check that digits after '+' meet minimum length
            digits = phone_number[1:]
            return digits.isdigit() and len(digits) >= MIN_PHONE_DIGITS
        
        # Without '+' prefix: check that all characters are digits and meet minimum length
        return phone_number.isdigit() and len(phone_number) >= MIN_PHONE_DIGITS
