# Currency Converter GUI

A simple graphical user interface (GUI) application for converting currencies using real-time exchange rates.

## Features

- **Real-time Exchange Rates**: Fetches live currency rates from the Open Exchange Rates API.
- **User-Friendly Interface**: Built with Tkinter for an intuitive experience.
- **Currency Selection**: Dropdown menus with searchable currency lists.
- **Swap Functionality**: Easily swap between "from" and "to" currencies.
- **Animated Results**: Visual feedback with color animations upon conversion.
- **Error Handling**: Displays error messages for invalid inputs or API failures.

## Requirements

- Python 3.12 or higher
- Tkinter (included with Python on most systems)
- Requests library
- Internet connection for fetching exchange rates

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Saisidd05/Rise-3.0-Tasks.git
   cd Rise-3.0-Tasks/Task\ 1
   ```

2. **Set up a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install requests
   ```

4. **Install Tkinter** (if not already installed):
   - On Ubuntu/Debian: `sudo apt install python3-tk`
   - On macOS: Usually included with Python
   - On Windows: Included with Python installer

## Usage

Run the application:
```bash
python currency_converter_gui.py
```

### How to Use:
1. Enter the amount to convert in the input field.
2. Select the source currency from the "From Currency" dropdown.
3. Select the target currency from the "To Currency" dropdown.
4. Click the "CONVERT" button.
5. View the result in the result box below.

### Additional Features:
- **Search Currencies**: Type in the dropdown to filter currencies.
- **Swap Currencies**: Click the "🔁 SWAP" button to exchange from/to currencies.

## API Information

The application uses the [Open Exchange Rates API](https://open.er-api.com/) for currency data. No API key is required for basic usage.

## Compatibility

- **Operating Systems**: Windows, macOS, Linux
- **Python Versions**: 3.6+
- **Notes**: 
  - On Linux, the `winsound` module (used for beep sounds on Windows) has been removed to ensure cross-platform compatibility.
  - Requires a graphical display environment. In headless servers, use Xvfb for virtual display.

## Troubleshooting

- **"No module named 'tkinter'"**: Install Tkinter as mentioned in the installation steps.
- **"No module named 'requests'"**: Install the requests library with `pip install requests`.
- **Display errors**: Ensure you're running on a system with a graphical desktop or use Xvfb in headless environments.
- **API errors**: Check your internet connection and try again later.

## License

This project is part of the Rise-3.0-Tasks repository. See the main repository for licensing information.
