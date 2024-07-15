## EasyTax: Automating Tax Filing in Kenya

### Abstract
Filing taxes can be a complex and time-consuming task for individuals and businesses alike. This project presents a simple automation script designed to streamline the tax filing process for users of the Kenya Revenue Authority (KRA) online portal. The script, developed using Selenium for web automation and integrating computer vision techniques, allows users to log into their KRA account and file their taxes with a single command. Initially created for Chrome users, the script aims to simplify the tax filing process, reduce errors, and save time. The readme of this project also discusses the global challenges of tax filing and the potential benefits of automation in this domain.

### Introduction
Filing taxes is often a challenging task, characterized by complex regulations, lengthy forms, and the need for precise documentation. In Kenya, as in many other parts of the world, taxpayers face significant difficulties in navigating the tax filing process. This paper introduces an automation script that addresses these challenges by automating the login and filing procedures on the KRA website.

### Global Challenges in Tax Filing
The difficulty of filing taxes is a global issue, with taxpayers facing various hurdles, including understanding tax laws, managing documentation, and meeting deadlines. According to a study by the World Bank, tax compliance costs are a significant burden for individuals and businesses worldwide . In Kenya, the complexity of the KRA online portal further complicates the tax filing process, leading to frequent errors and delays .

### Methodology
The proposed solution leverages web automation and computer vision technologies to simplify tax filing. The script was developed in Python using the Selenium library for browser automation and the OpenCV and Pytesseract libraries for image processing and text recognition.

#### Requirements
1. **Selenium**: A powerful tool for controlling web browsers through programs and performing browser automation.
    - Installation: `pip install selenium`
2. **Chrome or Firefox WebDrivers**: These drivers enable Selenium to interact with the browsers.
    - Chrome WebDriver: Download from the [official website](https://sites.google.com/a/chromium.org/chromedriver/).
    - Firefox Geckodriver: Download from the [official website](https://github.com/mozilla/geckodriver/releases).
    - Verify Chrome version: `chrome --version` (Windows) or `chromium --version` (Linux)
3. **Computer Vision Libraries**:
    - OpenCV: `pip install opencv-python`
    - Pytesseract: `pip install pytesseract` and `pip install tesseract`

To simplify the setup, users can install all required packages using:
```bash
pip install -r requirements.txt
```

### Implementation
The automation script is designed to perform the following tasks:
1. **Login**: Automates the login process to the KRA online portal by entering the user's credentials and navigating through the authentication steps.
2. **Form Filling**: Automatically fills in the required tax forms using stored user data.
3. **Submission**: Submits the completed forms and logs out of the account.

The initial version of the script was tailored for Chrome users, with plans to extend support to Firefox.

### Results
The script was tested with several user accounts and demonstrated significant time savings and reduction in filing errors. Users reported a smoother and more efficient tax filing experience.

### Discussion
The development of this automation script highlights the potential of technology to simplify complex bureaucratic processes. By reducing the manual effort required for tax filing, the script allows users to focus on more productive tasks and ensures greater accuracy in their submissions.

### Conclusion
This paper presented a simple yet effective solution for automating the tax filing process on the KRA online portal. By leveraging web automation and computer vision technologies, the script addresses common challenges faced by taxpayers in Kenya. Future work will involve extending the script's compatibility to Firefox and other browsers and incorporating additional features to handle more complex filing scenarios.

### References
1. World Bank. (2016). Paying Taxes 2016: The Global Picture. Retrieved from [World Bank](https://www.worldbank.org/en/research/publication/paying-taxes-2016).
2. Kenya Revenue Authority. (2020). Taxpayer Services. Retrieved from [KRA](https://www.kra.go.ke/en/taxpayer-service).
