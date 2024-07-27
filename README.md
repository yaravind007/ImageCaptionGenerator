# Image Caption Generator

A Streamlit app that uses Google's Gemini 1.5-Flash model to generate captions for uploaded images.

## Table of Contents

* [Introduction](#introduction)
* [Features](#features)
* [Installation](#installation)
* [Usage](#usage)
* [Contributing](#contributing)
* [License](#license)

## Introduction

This application utilizes Google's Gemini 1.5-Flash model to generate captions for uploaded images. Simply upload an image, and the model will provide a descriptive caption. Additionally, the caption can be converted to speech and played back to you.

## Features

* Upload an image and generate a caption using the Gemini 1.5-Flash model.
* Convert the caption to speech and play it back.
* Abstract section that describes the application and its purpose.
* About Me section that provides information about the developer.
* Feedback section that allows users to provide feedback and suggestions.

## Installation

To run the application, follow these steps:

1. **Install dependencies:**

    ```bash
    pip install streamlit google-generativeai pillow gtts streamlit-option-menu
    ```

2. **Set up Google Cloud API key:**

    You will need to set up a Google Cloud account and obtain an API key for the Gemini 1.5-Flash model. Follow the instructions on the [Google Cloud website](https://cloud.google.com/) to obtain your API key. Create a `.env` file in the root directory of the project and add your API key:

    ```env
    GOOGLE_API_KEY=your_google_api_key_here
    ```

## Usage

To run the Streamlit application, use the following command:

```bash
streamlit run app.py
Contributing
If you would like to contribute to this project, please fork the repository and submit a pull request. Your contributions are welcome!

License
This project is licensed under the MIT License. See the LICENSE file for details.

The MIT License (MIT)
Copyright © 2024 <Aravind Kumar Yedida>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.