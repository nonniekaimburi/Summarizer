# Document Summarizer

Document Summarizer is a web application that provides automatic text summarization and audio transcription using OpenAI's GPT-4.0-turbo model. The application also supports QR code scanning to fetch documents for summarization.

## Features

- Text Summarization: Enter or paste text to get a concise summary.
- Audio Transcription and Summarization: Upload an audio clip to get its transcription followed by a summary.
- QR Code Scanning: Scan QR codes to retrieve documents or text for summarization.

## Getting Started

### Prerequisites

- Python >= 3.6
- Flask
- OpenAI Python client
- JavaScript QR Code scanner library (if applicable)

### Setting up Environment Variables

Ensure you set up the `OPENAI_API_KEY` in your environment:

```bash
export OPENAI_API_KEY='your_api_key_here'
