# 🧪 Practice HackerEarth – Selenium Automation Project

## 📌 Overview

This project is a simple automation exercise built with **Python** and **Selenium WebDriver**.
It navigates through the test website:

👉 https://the-internet.hackerearth.com/

The goal is to simulate user interactions and validate key UI elements such as redirects, headers, and HTTP status codes.

---

## 🚀 Features

* Navigate to the main page
* Click on the **Redirect Link**
* Validate page title after redirection
* Navigate to **Status Codes**
* Extract available HTTP status codes (200, 301, 404, 500)
* Open the **500 status code page**
* Validate the displayed message

---

## 🛠️ Technologies Used

* Python 3.x
* Selenium WebDriver
* ChromeDriver

---

## 📂 Project Structure

```
project/
│
├── main.py   # Main automation script
└── README.md # Project documentation
```

---

## ⚙️ Installation

1. Clone the repository:

```bash
git clone <your-repo-url>
cd <project-folder>
```

2. Install dependencies:

```bash
pip install selenium
```

3. Download ChromeDriver:

* Make sure it matches your Chrome version
* Add it to your PATH or place it in the project directory

---

## ▶️ How to Run

```bash
python main.py
```

---

## 🔍 What the Script Does

### 1. Redirect Validation

* Clicks on **Redirect Link**
* Waits for the "Redirection" header
* Returns the page title

### 2. Status Codes Extraction

* Clicks on redirect button
* Navigates to **Status Codes page**
* Extracts all available codes into a list

### 3. 500 Status Code Validation

* Finds the "500" link dynamically
* Navigates to the page
* Extracts and returns the message:

  > "This page returned a 500 status code."

---

## 🧠 Key Concepts Demonstrated

* Explicit waits (`WebDriverWait`)
* Element location strategies (CSS Selector, XPath, ID)
* Dynamic element handling
* Navigation and state validation
* Basic test flow structure

---

## ⚠️ Known Limitations

* No test framework integration (e.g., pytest)
* No assertions (uses print statements instead)
* No error handling for missing elements
* Hardcoded browser (Chrome only)

---

## 💡 Suggested Improvements

* Integrate with **pytest**
* Add assertions instead of prints
* Implement **Page Object Model (POM)**
* Add logging
* Parameterize browser selection
* Improve error handling

---

## 🎯 Learning Purpose

This project is designed to:

* Practice Selenium fundamentals
* Understand DOM interaction
* Build a foundation for QA Automation roles

---

## 👨‍💻 Author

Sergio Romero Pérez

---

## 📄 License

This project is for educational purposes.
