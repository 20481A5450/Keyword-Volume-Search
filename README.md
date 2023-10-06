# YouTube Keyword Search Volume Web Application

## Overview
The YouTube Keyword Search Volume Web Application is a powerful and user-friendly tool designed to streamline the process of searching for YouTube videos based on keywords. This application leverages the YouTube API to provide comprehensive search results, video details, and related content in an intuitive and visually appealing interface.

## Features
- **Keyword Search:** Easily find YouTube videos by entering a keyword in the search box.
- **Search Results:** Quickly access video titles and video IDs for the entered keyword.
- **Approximate Search Volume:** Get an estimate of the search volume for the specified keyword.
- **Graph:** A dynamic line chart built with Chart.js displays keyword search counts over the past 12 months, offering valuable insights into search trends.
- **Video Details:** For the top video in the search results, access detailed information, including title, description, publication date, channel title, view count, like count, dislike count, and comment count.
- **Related Videos:** Discover related videos with their titles and direct video links.
- **Styling:** Enjoy a visually pleasing user interface with CSS styling for an enhanced user experience.

## Getting Started
1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/youtube-keyword-search.git
   ```

2. **Install required dependencies:**
   ```bash
   pip install Flask google-api-python-client chart.js
   ```

3. **Set up your YouTube API Key:**
   - Go to the [Google Cloud Console](https://console.cloud.google.com/).
   - Create a new project.
   - Enable the YouTube Data API v3 for your project.
   - Create an API key and make a note of it.

4. **Configure the application:**
   - Open `app.py` and replace `'YOUR_YOUTUBE_API_KEY'` with your actual YouTube API key.

5. **Run the application:**
   ```bash
   python app.py
   ```

6. **Access the web application:**
   Visit [http://localhost:5000](http://localhost:5000) in your web browser.

## Usage
1. Enter a keyword in the search box and click "Get Search Volume."
2. Explore the search results, approximate search volume, and related videos.
3. View video details and the line chart showing search count over the past 12 months.

## Screenshots
![Search Results](screenshots/search-results.png)
![Video Details](screenshots/video-details.png)
![Related Videos](screenshots/related-videos.png)

## Technologies Used
- Flask
- Google API Python Client
- Chart.js

## Credits
Developed by Shaik.Zohaib (mailto:shaikzohaibgec@gmail.com)

## License
This project is licensed under the MIT License.

Feel free to customize this README to suit your project's needs, and don't forget to include actual screenshots and provide accurate instructions for setup and usage. A well-structured README can greatly enhance the visibility and usability of your project.

