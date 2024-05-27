# Exe News Fetcher

## Overview

Exe News Fetcher is a Streamlit-based web application that allows users to fetch and summarize the latest news on topics of their choice. Simply input a topic, and Exe will generate relevant search queries, fetch recent news articles, and display them. Additionally, Exe offers the ability to summarize the articles for a quick overview.

## Features

- **User-Friendly Interface**: Easy-to-use input field for entering topics.
- **Recent News Fetching**: Retrieves the latest news articles from the past week.
- **Summarization**: Provides brief summaries of the fetched articles (feature commented out in code).
- **Adaptive Design**: Ensures visibility and usability in both light and dark modes.

## Installation

### Prerequisites

- Python 3.7 or higher
- Streamlit
- exa_py
- together

### Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/exe-news-fetcher.git
    cd exe-news-fetcher
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Run the application:
    ```sh
    streamlit run app.py
    ```

## Usage

1. Open the web application in your browser.
2. Enter a topic in the input field and press Enter.
3. View the top 5 news articles related to the entered topic.
4. (Optional) Summarize the articles by uncommenting the summarization feature in the code.

## Code Structure

- **app.py**: Main file containing the Streamlit application code.

## Customization

To customize the application:

1. Modify the `SYSTEM_MESSAGE` and other variables to change the behavior of the assistant.
2. Adjust the `start_published_date` parameter in `exa.search_and_contents` to change the date range of fetched articles.
3. Uncomment and modify the summarization section to enable article summaries.

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue to discuss changes.
