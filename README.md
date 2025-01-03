# Assignment

## Introduction
This project is designed to scrape trending topics from Twitter using Selenium and display them on a web interface built with Flask.

## Objectives
- Scrape trending topics from Twitter.
- Display the scraped data on a web page.
- Store the scraped data in a MongoDB database.

## Requirements
- Python 3.x
- Chrome WebDriver
- MongoDB

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/yourrepository.git
    ```
2. Navigate to the project directory:
    ```bash
    cd yourrepository
    ```
3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Set up environment variables in the `.env` file:
    ```properties
    TWITTER_USERNAME=your_twitter_username
    TWITTER_PASSWORD=your_twitter_password
    PROXYMESH_URL=your_proxymesh_url
    ```
2. Run the Flask application:
    ```bash
    python src/web/app.py
    ```
3. Open your web browser and navigate to `http://127.0.0.1:5000`.

## Contributing
1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## License
This project is licensed under the MIT License.
