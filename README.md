# **Automation_Scripts**
A collection of Python scripts and tools designed to automate various tasks, improve productivity, and simplify repetitive actions. Each script is well-documented and serves a specific purpose, ranging from data visualization to smart home control.

---

## **Repository Structure**
### Folders:
   1. **Facebook Bot**
      - Automate interactions and actions on Facebook. Includes a basic setup and app.py.

   2. **Instagram Bot**
      - A script for automating Instagram tasks such as posting, commenting, or following.

   3. **Twitter Bot**
      - Automate Twitter tasks, including posting tweets and managing followers.

### **Standalone Scripts:**
   1. `currency_converter.py`
      - Converts currencies using live exchange rates from online APIs.

   2. `data_visualizer.py`
      - Creates interactive data visualizations using libraries like Matplotlib or Plotly.

   3. `email_sender.py`
      - Automates email sending using SMTP protocols. Supports attachments.

   4. `file_organizer.py`
      - Organizes files in a directory by categories such as file type.

   5. `pdf_merger.py`
      - Merges multiple PDF files into a single document.

   6. `screenshot_capture.py`
      - Captures screenshots of your desktop or a specific application window.

   7. `smart_home_control.py`
      - Integrates with IoT devices to control smart home functions like lights or thermostats.

   8. `system_health_check.py`
      - Monitors system performance metrics like CPU usage, memory, and disk space.

   9. `url_refresher.py`
      - Refreshes a given URL using Selenium WebDriver, with configurable wait times.

   10. `web_scraper.py`
      - Scrapes web pages for data using BeautifulSoup or Selenium.

   11. `word_merger.py`
      - Merges multiple Word documents into a single file.

---


## **Setup Instructions**
### Prerequisites
   - Python 3.x
   - Required libraries:
      - Selenium
      - BeautifulSoup
      - Matplotlib / Plotly (for data visualization)
      - PyPDF2 (for PDF merging)
      - smtplib (for email automation)
      - Any other specific libraries listed in individual script headers.


### Installation
   1. Clone the repository:

      ```bash
      git clone https://github.com/stephenombuya/Automation_Scripts/tree/main
      cd Automation_Scripts
      ```

   2. Install dependencies:

      ```
      pip install -r requirements.txt
      ```
      

### Script-Specific Setup
Some scripts may require additional setup (e.g., API keys for bots, SMTP credentials for `email_sender.py`, or ChromeDriver for Selenium). Refer to the script comments for details.

---

## **General Usage**
   1. Navigate to the script directory:

      ```bash
      cd <script_name>
      ```

   2. Run the script:

     ``` php
      python <script_name>.py
      ```
      
   3. Modify the configuration variables as needed in each script to customize behavior (e.g., URL for `url_refresher.py` or directory path for `file_organizer.py`).

---


## **Troubleshooting**
   - Ensure all dependencies are installed.
   - Check for updated versions of ChromeDriver or other required tools.
   - Follow the specific error message recommendations.

For issues or suggestions, feel free to create an issue in the GitHub repository.

---
