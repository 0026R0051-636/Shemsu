"""
Example usage of Shemsu SMS Application.

This script demonstrates how to use the Shemsu SMS app programmatically.
"""
from app import ShemsuApp


def example_send_single_message():
    """Example: Send a single SMS message."""
    print("\n" + "=" * 60)
    print("Example 1: Sending a single SMS message")
    print("=" * 60)
    
    # Create an instance of the app
    app = ShemsuApp()
    
    # Send a message
    to_number = "+1234567890"  # Replace with actual phone number
    message = "Hello from Shemsu SMS! This is a test message."
    
    success = app.send_message(to_number, message)
    
    if success:
        print(f"✓ Successfully sent message to {to_number}")
    else:
        print(f"✗ Failed to send message to {to_number}")


def example_send_bulk_messages():
    """Example: Send messages to multiple recipients."""
    print("\n" + "=" * 60)
    print("Example 2: Sending bulk SMS messages")
    print("=" * 60)
    
    # Create an instance of the app
    app = ShemsuApp()
    
    # List of recipients
    recipients = [
        "+1234567890",
        "+0987654321",
        "+1111111111"
    ]
    
    message = "Bulk message: Special offer just for you!"
    
    success_count = 0
    for recipient in recipients:
        if app.send_message(recipient, message):
            success_count += 1
    
    print(f"\n✓ Successfully sent {success_count}/{len(recipients)} messages")


def example_validate_phone_numbers():
    """Example: Validate phone numbers before sending."""
    print("\n" + "=" * 60)
    print("Example 3: Validating phone numbers")
    print("=" * 60)
    
    app = ShemsuApp()
    
    test_numbers = [
        "+1234567890",      # Valid
        "1234567890",       # Valid (without +)
        "+123",             # Invalid (too short)
        "invalid",          # Invalid
        "",                 # Invalid (empty)
    ]
    
    for number in test_numbers:
        is_valid = app.sms_service.validate_phone_number(number)
        status = "✓ Valid" if is_valid else "✗ Invalid"
        print(f"{status}: {number}")


def main():
    """Run all examples."""
    print("\n" + "=" * 60)
    print("SHEMSU SMS APPLICATION - USAGE EXAMPLES")
    print("=" * 60)
    print("\nNOTE: These examples use the 'mock' provider by default.")
    print("To use a real SMS provider, update your .env file.")
    print("See .env.example for configuration options.")
    
    # Run examples
    example_send_single_message()
    example_send_bulk_messages()
    example_validate_phone_numbers()
    
    print("\n" + "=" * 60)
    print("Examples completed!")
    print("=" * 60)
    print("\nNext steps:")
    print("1. Copy .env.example to .env")
    print("2. Configure your SMS provider credentials in .env")
    print("3. Install provider SDK: pip install twilio  (or pip install vonage)")
    print("4. Update SMS_PROVIDER in .env to 'twilio' or 'vonage'")
    print("5. Start sending real SMS messages!")


if __name__ == "__main__":
    main()
