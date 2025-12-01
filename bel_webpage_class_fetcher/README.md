# Introduction

load_url is a lightweight Python utility that automates webpage loading and HTML extraction using Selenium. 
It waits for a specific CSS class to appear on the page—ensuring the content is fully rendered—before saving the final HTML to a file.
This makes it ideal for scraping dynamic sites, debugging frontend rendering, or capturing snapshots of JavaScript-heavy pages. The tool supports headless mode for background usage and works seamlessly with Firefox through Geckodriver.

# Features

- Loads webpages using selenium
- Waits for the specified class to load before fetching the webpage
- saves the enitre rendered HTML to the specified file location
- Supports Headless mode so to open and read the page in an invisible NON UI browser to save on Memory and Graphic Resources


# Installation

Install using the following pip command:

'''
pip install bel_webpage_class_fetcher
'''


# Requirements

- python 3.7+
- firefox
- geckodriver
- INTERNET (!!!)
- Highly Reccomended to use Virtual Enviornment

# Usage

- import the library using 

```
from bel_webpage_class_fetcher import load_url
```

Parameters:

```
url: str -> The URL of the webpage to be loaded
wait_for_class -> the name of the class to wait for to load before downloading
output_file_name: str -> the filepath where the HTML will be stored
driver_path: str -> the path to the geckodriver (recommend full path)
headless: bool -> flag to specify wheather to opne the browser window or not
```

# Example Output

~ Imagine a fully rendered HTML page~

# Troubleshooting