"""
Shemsu SMS Application - Main Entry Point

This is a basic SMS application for managing and sending SMS messages.
Perfect for starting an SMS business.
"""
import sys
import logging

from config import config
from sms_service import SMSService

# Set up logging
logging.basicConfig(
    level=getattr(logging, config.LOG_LEVEL),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class ShemsuApp:
    """Main Shemsu SMS Application class."""
    
    def __init__(self):
        """Initialize the application."""
        self.sms_service = SMSService()
        logger.info("Shemsu SMS Application initialized")
    
    def send_message(self, to_number: str, message: str) -> bool:
        """
        Send an SMS message to a recipient.
        
        Args:
            to_number: The recipient's phone number
            message: The message content
            
        Returns:
            True if successful, False otherwise
        """
        # Validate phone number
        if not self.sms_service.validate_phone_number(to_number):
            logger.error(f"Invalid phone number format: {to_number}")
            return False
        
        # Validate message
        if not message:
            logger.error("Message cannot be empty")
            return False
        
        # Send the SMS
        result = self.sms_service.send_sms(to_number, message)
        
        if result.get('success'):
            logger.info(f"Message sent successfully to {to_number}")
            logger.info(f"Message ID: {result.get('message_id')}")
            return True
        else:
            logger.error(f"Failed to send message: {result.get('error')}")
            return False
    
    def run_interactive(self):
        """Run the application in interactive mode."""
        print("=" * 60)
        print("Welcome to Shemsu SMS Application!")
        print("=" * 60)
        print(f"Current SMS Provider: {config.SMS_PROVIDER}")
        print()
        
        while True:
            print("\nOptions:")
            print("1. Send SMS")
            print("2. Exit")
            
            choice = input("\nEnter your choice (1-2): ").strip()
            
            if choice == '1':
                to_number = input("Enter recipient phone number (e.g., +1234567890): ").strip()
                message = input("Enter message: ").strip()
                
                print("\nSending message...")
                success = self.send_message(to_number, message)
                
                if success:
                    print("✓ Message sent successfully!")
                else:
                    print("✗ Failed to send message. Check logs for details.")
            
            elif choice == '2':
                print("\nThank you for using Shemsu SMS Application!")
                break
            
            else:
                print("Invalid choice. Please try again.")


def main():
    """Main function to run the application."""
    print("""
    ███████╗██╗  ██╗███████╗███╗   ███╗███████╗██╗   ██╗
    ╚══███╔╝██║  ██║██╔════╝████╗ ████║██╔════╝██║   ██║
      ███╔╝ ███████║█████╗  ██╔████╔██║███████╗██║   ██║
     ███╔╝  ██╔══██║██╔══╝  ██║╚██╔╝██║╚════██║██║   ██║
    ███████╗██║  ██║███████╗██║ ╚═╝ ██║███████║╚██████╔╝
    ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝╚══════╝ ╚═════╝ 
    
    SMS Business Application - Starter Code
    """)
    
    try:
        app = ShemsuApp()
        
        # Check if running with arguments
        if len(sys.argv) > 1:
            if sys.argv[1] == '--interactive' or sys.argv[1] == '-i':
                app.run_interactive()
            elif sys.argv[1] == '--help' or sys.argv[1] == '-h':
                print("Usage:")
                print("  python app.py                    # Show this help")
                print("  python app.py -i                 # Run in interactive mode")
                print("  python app.py --interactive      # Run in interactive mode")
                print("\nFor programmatic usage, import ShemsuApp class:")
                print("  from app import ShemsuApp")
                print("  app = ShemsuApp()")
                print("  app.send_message('+1234567890', 'Hello World!')")
            else:
                print(f"Unknown option: {sys.argv[1]}")
                print("Use --help for usage information")
        else:
            print("Use 'python app.py --help' for usage information")
            print("Use 'python app.py --interactive' to run in interactive mode")
            
    except KeyboardInterrupt:
        print("\n\nApplication interrupted by user")
        sys.exit(0)
    except Exception as e:
        logger.error(f"Application error: {str(e)}", exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    main()
