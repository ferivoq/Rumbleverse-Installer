# Rumbleverse Download API

This repository contains the source code for the Rumbleverse Download API, an Express.js application designed to serve downloadable builds of Rumbleverse. The API provides an easy-to-use interface for listing and downloading different versions of the game.

## Features

- **Static File Serving:** The API serves zip files containing different builds of Rumbleverse.
- **Version Listing:** It dynamically lists available versions based on the files present in the `versions` directory.
- **Cross-Origin Resource Sharing (CORS):** Enabled CORS to allow requests from different domains.
- **Docker Support:** Includes a Dockerfile for easy deployment and containerization.

## Setup

1. **Prerequisites:**
    - Node.js
    - NPM (Node Package Manager)
    - Docker (optional for containerized deployment)

2. **Installation:**
    - Clone the repository.
    - Run `npm install` to install the required Node.js packages.

3. **Adding Builds:**
    - Place your Rumbleverse build files in the `versions` directory. For downloading builds join into our Discord Server. https://discord.gg/HU3YUaFcAG
    - Ensure each build is compressed as a `.zip` file.

4. **Configuration:**
    - Modify the domain in the `getVersionsData` function to point to your own domain.
    - Example: Replace `https://rvapi.ferivoq.me/versions/${encodeURIComponent(file)}` with your domain.

5. **Docker Setup (Optional):**
    - Build the Docker image using `docker build -t rumbleverse-api .`
    - Run the container using `docker run -p 4000:4000 rumbleverse-api`

6. **Running the API:**
    - Start the server using `npm run dev` or with your preferred process manager.
    - Access the API at `http://localhost:4000`.

## API Endpoints

- `GET /api`: Returns a JSON object listing all available Rumbleverse versions with download links.
- `GET /`: A simple endpoint that returns the text 'Rumbleverse Download API'.
- Static files are served under `/versions`.

## Dockerfile

A Dockerfile is included for building a Docker image of the API. This allows for easy deployment and scaling.

## Contribution

Contributions to the project are welcome. Please ensure you follow the existing code style and include proper documentation for your changes.

---

Note: This documentation assumes basic familiarity with Node.js, Express.js, and Docker. Ensure you update the domain in the API as per your deployment needs.

