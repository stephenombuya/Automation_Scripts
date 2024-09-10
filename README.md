# Automation_Scripts

## Refresh URL with Selenium

This Python script uses Selenium to open a YouTube URL in a Chrome browser, waits for 10 seconds, and then refreshes the page. It can be adapted for any website by changing the `url` variable.

## Prerequisites

Before running the script, ensure you have the following installed:

- **Python** (Version 3.x)
- **Selenium** library
- **webdriver-manager** library

## Installation

1. **Clone or download the repository**:

   ```
   git clone https://github.com/stephenombuya/Automation_Scripts.git
   cd Automation.py
   ```

2. **Install the required Python packages**:

Use pip to install Selenium and webdriver-manager.

```
pip install selenium 
```

```
pip install webdriver-manager
```

3. **Install Chrome browser**:

Ensure that Google Chrome is installed on your system, as this script uses Chrome as the browser.


## Usage

1. **Run the script**:

To run the script, execute the following command in your terminal:

```
python Automation.py
```

2. **What the script does**:

The script opens the YouTube homepage in a Chrome browser.
It waits for 10 seconds before refreshing the page.

3. **Modify the URL**:

To open a different URL, simply change the value of the `url` variable in the script:

```
url = "https://www.example.com/"
```

## Troubleshooting

* Ensure Chrome is installed and up-to-date.
* If ChromeDriver installation fails, manually download the appropriate version for your Chrome from ChromeDriver.

