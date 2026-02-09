# Shemsu SMS Application 📱

A simple, easy-to-use SMS application starter code for your SMS business. Perfect for beginners who want to start an SMS business!

## Features ✨

- **Easy to Use**: Simple API for sending SMS messages
- **Multiple Providers**: Support for Twilio, Vonage, or Mock mode for testing
- **Interactive Mode**: User-friendly command-line interface
- **Programmatic API**: Use as a library in your own applications
- **Well Documented**: Comprehensive examples and documentation
- **Extensible**: Easy to add new features and providers

## Quick Start 🚀

### 1. Installation

```bash
# Clone the repository (if not already done)
git clone https://github.com/0026R0051-636/Shemsu.git
cd Shemsu

# Install dependencies
pip install -r requirements.txt
```

### 2. Configuration

```bash
# Copy the example environment file
cp .env.example .env

# Edit .env with your SMS provider credentials (optional for testing)
# For testing, the default 'mock' provider works without any credentials
```

### 3. Run the Application

#### Interactive Mode
```bash
python app.py --interactive
```

#### Run Examples
```bash
python example.py
```

#### Programmatic Usage
```python
from app import ShemsuApp

app = ShemsuApp()
app.send_message("+1234567890", "Hello from Shemsu!")
```

## Usage Examples 📖

### Sending a Single Message

```python
from app import ShemsuApp

app = ShemsuApp()
success = app.send_message(
    to_number="+1234567890",
    message="Hello! This is a test message."
)

if success:
    print("Message sent successfully!")
```

### Sending Bulk Messages

```python
from app import ShemsuApp

app = ShemsuApp()

recipients = ["+1234567890", "+0987654321", "+1111111111"]
message = "Special offer just for you!"

for recipient in recipients:
    app.send_message(recipient, message)
```

### Validating Phone Numbers

```python
from app import ShemsuApp

app = ShemsuApp()

if app.sms_service.validate_phone_number("+1234567890"):
    print("Valid phone number!")
```

## Configuration ⚙️

The application supports multiple SMS providers:

### Mock Provider (Default - For Testing)
```ini
SMS_PROVIDER=mock
```
No credentials needed. Perfect for testing!

### Twilio
```ini
SMS_PROVIDER=twilio
TWILIO_ACCOUNT_SID=your_account_sid
TWILIO_AUTH_TOKEN=your_auth_token
TWILIO_PHONE_NUMBER=+1234567890
```

### Vonage (formerly Nexmo)
```ini
SMS_PROVIDER=vonage
VONAGE_API_KEY=your_api_key
VONAGE_API_SECRET=your_api_secret
VONAGE_PHONE_NUMBER=+1234567890
```

## Project Structure 📁

```
Shemsu/
├── app.py              # Main application entry point
├── sms_service.py      # SMS service with provider implementations
├── config.py           # Configuration management
├── example.py          # Usage examples
├── requirements.txt    # Python dependencies
├── .env.example        # Example environment configuration
├── .gitignore          # Git ignore file
└── README.md           # This file
```

## Getting Started with SMS Business 💼

### For Beginners

1. **Choose an SMS Provider**: 
   - [Twilio](https://www.twilio.com/) - Popular, easy to use
   - [Vonage](https://www.vonage.com/) - Competitive pricing
   
2. **Sign Up**: Create an account with your chosen provider

3. **Get Credentials**: Obtain your API credentials from the provider dashboard

4. **Configure Shemsu**: Add your credentials to the `.env` file

5. **Start Testing**: Use the mock provider first to test your workflow

6. **Go Live**: Switch to your real provider when ready!

### Next Steps

- Add a database to store message history
- Create a web interface using Flask or Django
- Add scheduling functionality for automated messages
- Implement message templates
- Add analytics and reporting
- Build a customer management system

## Requirements 📋

- Python 3.8 or higher
- pip (Python package manager)
- (Optional) SMS provider account (Twilio, Vonage, etc.)

## Support 🆘

For questions or issues:
1. Check the example.py file for usage examples
2. Review the code comments in each file
3. Consult your SMS provider's documentation
4. Open an issue on GitHub

## License 📄

This is starter code for your SMS business. Feel free to modify and use it as needed!

## Contributing 🤝

Contributions are welcome! Feel free to submit pull requests or open issues.

---

**Happy SMS Sending! 📨**
