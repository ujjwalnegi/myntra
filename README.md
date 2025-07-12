Myntra Automation Testing (Selenium + Pytest)
This project is a test automation framework for key user journeys on [Myntra.com](https://www.myntra.com), developed using **Python**, **Selenium**, and **Pytest**.
It covers:
- Product search and filtering
- Product selection and add to cart
- Validations on UI elements

Tools & Technologies
- Python
- Selenium WebDriver
- Pytest
- Page Object Model
- HTML test reports using pytest-html
- Jenkins for CI integration

- Steps to run the script
```bash
git clone https://github.com/ujjwalnegi/myntra.git
cd myntra
pip install -r requirements.txt
pytest --html=reports/report.html
