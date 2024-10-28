# Real-Time YouTube Analytics Tool

This project is a Flask web application that allows users to fetch and analyze YouTube channel data. Users can input a YouTube channel ID to retrieve statistics about the channel and its videos.

## Features

- User-friendly interface to input YouTube channel ID.
- Fetches channel statistics, including views and likes.
- Displays a dashboard with video details from the specified channel.
- Error handling for unsuccessful data retrieval.

## Prerequisites

- Python 3.x
- Flask
- YouTube Data API v3

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up your YouTube Data API key in the `youtube_data.py` file. Ensure that you have enabled the YouTube Data API for your Google project.

5. Change the `SECRET_KEY` in `app.py` to a secure random string.

## Usage

1. Start the Flask application:

   ```bash
   python app.py
   ```

2. Open your web browser and go to `http://127.0.0.1:5000/`.

3. Navigate to the YouTube form and enter the YouTube channel ID.

4. Submit the form to view the channel's statistics and video details.

## Project Structure

```
.
├── app.py                  # Main Flask application
├── youtube_data.py         # YouTube API data fetching functions
├── templates               # Folder containing HTML templates
│   ├── home.html          # Home page template
│   ├── forms               # Folder containing form templates
│   │   └── youtube_form.html # YouTube form template
│   └── youtube_dashboard.html # Dashboard template displaying stats
├── static                  # Folder for static files (CSS, JavaScript, etc.)
└── requirements.txt        # Python dependencies
```

## Error Handling

If there is an error fetching channel data (e.g., invalid channel ID), an error page will be displayed with an appropriate message.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
