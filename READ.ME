Interface-Engine for HealthAI-Harbor

Overview

The Interface-Engine is a core microservice of the HealthAI-Harbor platform.
It acts as the entry point for receiving and processing DICOM files and initiating workflows using Netflix Conductor.
The Interface-Engine ensures secure and efficient handling of medical imaging data and supports future extensions like HL7 message processing.

Features

DICOM File Handling:

Receive DICOM files over HTTP and DICOM protocols.

Extract and validate metadata from DICOM headers.

Workflow Management:

Integrate with Netflix Conductor to initiate workflows.

Send metadata extracted from files as workflow input.

File Storage:

Temporarily store DICOM files securely.

Provide file references for downstream processing.

Logging and Monitoring:

Track file uploads, processing, and workflow initiation.

Ensure visibility into system health with structured logs.

Future Features:

Support for HL7 messages for healthcare interoperability.

Enhanced monitoring and alerting.

Architecture

The Interface-Engine is built on a modular architecture with the following components:

File Receiver: Handles incoming DICOM files via HTTP or DICOM protocol.

Metadata Extractor: Parses and validates DICOM metadata.

Workflow Initiator: Communicates with Netflix Conductor to start workflows.

File Storage: Temporarily stores DICOM files in a secure location.

Logging: Implements structured logging for all operations.


Architecture

The Interface-Engine is built on a modular architecture with the following components:

File Receiver: Handles incoming DICOM files via HTTP or DICOM protocol.

Metadata Extractor: Parses and validates DICOM metadata.

Workflow Initiator: Communicates with Netflix Conductor to start workflows.

File Storage: Temporarily stores DICOM files in a secure location.

Logging: Implements structured logging for all operations

Folder Structure

interface-engine/
├── app/
│   ├── __init__.py
│   ├── main.py               # Entry point for the service
│   ├── api/
│   │   ├── __init__.py
│   │   ├── dicom_routes.py   # HTTP routes for receiving DICOM files
│   │   ├── hl7_routes.py     # HTTP routes for HL7 messages (future)
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py         # Configuration settings
│   │   ├── workflow.py       # Netflix Conductor API integration
│   │   ├── storage.py        # File storage logic
│   │   └── dicom_handler.py  # DICOM file parsing and validation
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── logger.py         # Logging configuration
│   ├── tests/
│       ├── test_dicom.py     # Test cases for DICOM handling
│       ├── test_workflow.py  # Test cases for Netflix Conductor
│       ├── test_storage.py   # Test cases for file storage
├── requirements.txt          # Dependencies (FastAPI, pydicom, requests)
├── Dockerfile                # Containerization setup
├── README.md                 # Documentation


API Endpoints

1. Upload DICOM File

Endpoint: POST /upload-dicom/

Description: Accepts DICOM files via HTTP, extracts metadata, and starts a workflow in Netflix Conductor.

Request:

{
  "file": "<DICOM file>"
}

Response:

{
  "message": "DICOM file uploaded successfully",
  "workflow_id": "<Workflow ID>"
}

2. (Future) Upload HL7 Message

Endpoint: POST /upload-hl7/

Description: Accepts HL7 messages, extracts data, and maps it to metadata for workflows.

Installation

1. Prerequisites

Python 3.8+

Docker (optional, for containerized deployment)

2. Setup

Clone the repository:

git clone https://github.com/your-repo/interface-engine.git
cd interface-engine
git clone https://github.com/your-repo/interface-engine.git
cd interface-engine

Install dependencies:
pip install -r requirements.txt

Run the service:
uvicorn app.main:app --reload

3. Docker Deployment

Build the Docker image:
docker build -t interface-engine .
Run the Docker container:
docker run -p 8000:8000 interface-engine



Configuration

Configuration options are available in app/core/config.py. Key settings include:

Netflix Conductor API URL

Temporary file storage path

Logging level

Dependencies

FastAPI: Framework for building APIs.

pydicom: Library for working with DICOM files.

requests: For making REST API calls.

uvicorn: ASGI server for running FastAPI.

Future Enhancements

Add support for MLLP to handle HL7 messages.

Enhance logging with centralized log storage (e.g., Elasticsearch).

Integrate with monitoring tools like Prometheus and Grafana.

Implement advanced retry mechanisms for workflow initiation.

Contributing

Contributions are welcome! Please open an issue or submit a pull request for bug fixes or feature enhancements.

License

This project is licensed under the MIT License.



Contact

For questions or support, contact the HealthAI-Harbor team.