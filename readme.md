# Easytax
![python:3.7 | 3.8](https://img.shields.io/badge/python-3.7%20%7C%203.8-blue)
![selenium: 3.141.0](https://img.shields.io/badge/selenium-3.141.0-005285)
![cv2: 4.2.0](https://img.shields.io/badge/cv2-4.2.0-6f7501)
![pytesseract: 0.3.4](https://img.shields.io/badge/pytesseract-0.3.4-green)
![build: passing](https://img.shields.io/badge/build-passing-brightgreen)

A simple automation script that logs into your kra account and files your taxes with one command
Currently works for Chrome users. Will create Firefox version soon


## Requirements

- Selenium
  ```
  pip install selenium
  ```

- chrome or firefox drivers

  1. gekodriver for firefox: [download](https://github.com/mozilla/geckodriver/releases)
  2. webdriver for chrome: [download](https://chromedriver.chromium.org/downloads)
  3. For Chrome users, download the webdriver specific to your browser. If you are on Chrome 81, get the webdriver for chrome 81.
  4. To verify your Chrome version, go to terminal and run `chrome --version` on Windows command prompt or `chromium --version` if you run Linux

- computer vision

  ```
  pip install opencv-python
  ```
- pytesseract

  ```
  pip install pytesseract
  pip install tesseract
  ```

Or simply run:
 ```pip install -r requirements.txt```


## License

This project is under the [mit](#) license

