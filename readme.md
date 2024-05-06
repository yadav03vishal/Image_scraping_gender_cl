# Project Title

This project consists of two Python scripts: `scrape.py` and `analyze_gender.py`.

## scrape.py

This script uses Selenium WebDriver to scrape images of men's t-shirts from the Myntra website. It scrolls through the webpage, collects the images, and saves them in a directory named 'myntra_images'.

### How to Run

1. Install the required packages: `selenium`, `urllib`, and `os`.
2. Run the script: `python scrape.py`.

## analyze_gender.py

This script uses the DeepFace library to analyze the scraped images. It determines the gender associated with each image and saves the results in a CSV file named 'gender_results.csv'.

### How to Run

1. Install the required packages: `deepface`, `cv2`, `os`, and `pandas`.
2. Run the script: `python analyze_gender.py`.

## Requirements

- Python 3.6 or above
- Selenium WebDriver
- DeepFace
- OpenCV (cv2)
- pandas

## Author

VISHAL


