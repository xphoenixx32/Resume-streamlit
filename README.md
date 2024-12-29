
# Streamlit Resume Application

A **web-based resume** built with [Streamlit](https://streamlit.io), showcasing professional experiences, skills, projects, and contact details in an interactive and visually appealing format.

---

## Features

- **Interactive Navigation**: Browse through various sections using a horizontal navigation menu.
- **Downloadable Resume**: Easily download the resume in PDF format.
- **Detailed Career and Education Info**: Tabs for career summary and educational background.
- **Skills Presentation**: Organized into hard and soft skills for better clarity.
- **Project Portfolio**: Showcases both work and side projects, with additional access links.
- **Contact Information**: Links to email, GitHub, and LinkedIn profiles.

---

## Sections Overview

### 1. **About**
   - Career Summary: Highlights key positions with responsibilities and achievements.
   - Education: Details academic qualifications and notable achievements.

### 2. **Skills**
   - Hard Skills: Technical expertise and tools.
   - Soft Skills: Interpersonal skills and qualities.

### 3. **Projects**
   - Side Projects: Personal projects with descriptions and access links.
   - Work Projects: Professional projects, contributions, and links (if available).

### 4. **Contact**
   - Email: Direct contact information.
   - Social Media: Links to LinkedIn and GitHub profiles.

---

## Installation and Usage

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   ```
2. **Install Dependencies**:
   Navigate to the project directory and install required libraries:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the App**:
   Launch the Streamlit app with:
   ```bash
   streamlit run app.py
   ```
4. **Access the Application**:
   Open the app in your browser at `http://localhost:8501`.

---

## Directory Structure

```plaintext
.
├── app.py               # Main Streamlit app script
├── assets/              # Assets directory (e.g., CV PDF)
├── descriptions.py      # Text data for the app (e.g., titles, descriptions)
├── print_txt.py         # Custom function for formatted text output
└── requirements.txt     # Python dependencies
```

---

## Dependencies

- **Streamlit**: For building the web app interface.
- **streamlit-option-menu**: For the navigation menu.
- **pathlib**: For handling file paths.

Install dependencies via:
```bash
pip install -r requirements.txt
```

---

## Demo

Check out the live demo of the app (if hosted) or a screenshot below:

![App Screenshot](assets/demo_screenshot.png)

---

## Future Enhancements

- **Responsive Design**: Improve layout for better mobile compatibility.
- **Dynamic Data**: Add options to dynamically update sections via a database or form input.
- **Localization**: Support multiple languages for wider accessibility.

---

## Contact

If you have any questions or suggestions, feel free to reach out via:

- **Email**: [Your Email Address]
- **LinkedIn**: [Your LinkedIn Profile](https://linkedin.com/in/your-profile)
- **GitHub**: [Your GitHub Profile](https://github.com/your-profile)

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
