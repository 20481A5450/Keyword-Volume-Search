YouTube Keyword Search Volume Web Application
YouTube Keyword Search Volume

Overview:
The YouTube Keyword Search Volume Web Application is a feature-rich web tool that allows users to search for YouTube videos based on keywords, view search results, explore video details, and discover related videos. It utilizes the YouTube API to fetch relevant data and provides a user-friendly interface for seamless interaction.

Features:
Keyword Search: Users can enter a keyword in the search box to find YouTube videos related to the keyword.
Search Results: Displayed search results include video titles and video IDs.
Approximate Search Volume: The application provides an estimated search volume for the entered keyword.
Graph: A line chart using Chart.js displays the keyword search count over the past 12 months (placeholder data).
Video Details: For the first video in the search results, detailed information such as title, description, published date, channel title, view count, like count, dislike count, and comment count are shown.
Related Videos: The application displays related videos with their titles and video links.
Styling: A visually appealing user interface with CSS styling for a pleasant user experience.
Getting Started
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/youtube-keyword-search.git
Install required dependencies:

bash
Copy code
pip install Flask google-api-python-client chart.js
Set up your YouTube API Key:

Go to the Google Cloud Console.
Create a new project.
Enable the YouTube Data API v3 for your project.
Create an API key and note it down.
Configure the application:

Open app.py and replace 'YOUR_YOUTUBE_API_KEY' with your actual YouTube API key.
Run the application:

bash
Copy code
python app.py
Access the web application at http://localhost:5000 in your web browser.

Usage
Enter a keyword in the search box and click "Get Search Volume."
Explore the search results, approximate search volume, and related videos.
View video details and the line chart showing search count over the past 12 months.
Screenshots
Search Results
Video Details
Related Videos

Technologies Used
Flask
Google API Python Client
Chart.js
Credits
Developed by SHAIK.ZOHAIB

License
This project is licensed under the MIT License.

Feel free to customize the README to include any additional information or sections that are relevant to your project. Make sure to update the placeholders like SHAIK.ZOHAIB mail:shaikzohaibgec@gmail.com and provide accurate instructions for setup and usage.
