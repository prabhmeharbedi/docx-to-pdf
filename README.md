
# DOCX to PDF Converter

A user-friendly web application for converting `.docx` files to password-protected PDF documents. Built with Flask and Dockerized for seamless deployment, this application supports both local use and cloud deployment.

---

## Table of Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
  - [Access the App Online](#1-access-the-app-online)
  - [Run Locally](#2-run-locally)
    - [Without Docker](#run-locally-without-docker)
    - [Using Docker](#run-locally-using-docker)
- [Usage](#usage)
- [Deployment](#deployment)
- [Docker Image](#docker-image)
- [Folder Structure](#folder-structure)
- [Known Issues](#known-issues)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Features
- Upload `.docx` files and convert them into PDF files.
- Optional password protection for enhanced security.
- Intuitive and responsive web interface.
- Deployed and live at: [https://docx-to-pdf-1-ooea.onrender.com](https://docx-to-pdf-1-ooea.onrender.com).
- Dockerized for portability and scalability: [Docker Hub Repository](https://hub.docker.com/r/prabhmeharbedi/docx-to-pdf).

---

## Tech Stack
- **Backend:** Flask
- **Frontend:** HTML, CSS
- **Containerization:** Docker
- **Deployment:** Render.com

---

## Getting Started

### 1. Access the App Online
Visit the live application at: [https://docx-to-pdf-1-ooea.onrender.com](https://docx-to-pdf-1-ooea.onrender.com).

### 2. Run Locally

#### Prerequisites:
- Python 3.9 or higher
- Docker (optional, for containerized deployment)

#### Run Locally Without Docker
1. Clone the repository:
   ```bash
   git clone https://github.com/<your-github-username>/docx-to-pdf-converter.git
   cd docx-to-pdf-converter
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Start the Flask app:
   ```bash
   python main.py
   ```
4. Open in your browser:
   [http://127.0.0.1:5000](http://127.0.0.1:5000)

#### Run Locally Using Docker
1. Pull the Docker image:
   ```bash
   docker pull prabhmeharbedi/docx-to-pdf
   ```
2. Run the Docker container:
   ```bash
   docker run -d -p 8080:5000 prabhmeharbedi/docx-to-pdf
   ```
3. Open in your browser:
   [http://127.0.0.1:8080](http://127.0.0.1:8080)

---

## Usage
1. Upload a `.docx` file via the web interface.
2. (Optional) Add a password to protect the generated PDF.
3. Click **Convert** to download your password-protected PDF.

---

## Deployment
This project is deployed on Render.com and can be accessed at: [https://docx-to-pdf-1-ooea.onrender.com](https://docx-to-pdf-1-ooea.onrender.com).

For deploying with Docker:
1. Build the Docker image:
   ```bash
   docker build -t docx-to-pdf .
   ```
2. Push the image to Docker Hub:
   ```bash
   docker push <your-dockerhub-username>/docx-to-pdf
   ```
3. Deploy using your preferred cloud provider.

---

## Docker Image
The Docker image is available at: [Docker Hub](https://hub.docker.com/r/prabhmeharbedi/docx-to-pdf).

To pull the image:
```bash
docker pull prabhmeharbedi/docx-to-pdf
```

---

## Folder Structure
```
docx-to-pdf-converter/
├── templates/
│   └── index.html       # Frontend HTML file
├── static/
│   └── css/
│       └── style.css    # Styling for the web app
├── uploads/             # Folder to store uploaded files (runtime)
├── main.py              # Flask app entry point
├── requirements.txt     # Python dependencies
├── Dockerfile           # Docker instructions
├── run.sh               # Script to build and run the container
└── README.md            # Documentation
```

---

## Known Issues
- The app does not support `.doc` files (only `.docx` is supported).
- PDF formatting depends on the complexity of the `.docx` file.

---

## Contributing
Contributions are welcome! To contribute:
1. Fork this repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add some feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact
For questions or support:
- **Developer:** Prabhmehar
- **Email:** prabhmehar2509@gmail.com
- **Docker Hub:** [prabhmeharbedi](https://hub.docker.com/r/prabhmeharbedi/docx-to-pdf)

--- 

Feel free to share suggestions or report issues via GitHub!
