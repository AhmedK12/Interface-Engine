from fastapi import FastAPI, UploadFile, HTTPException
from app.core.dicom_handler import process_dicom
from app.core.workflow import start_workflow

app = FastAPI()


@app.post("/upload-dicom/")
async def upload_dicom(file: UploadFile):
    if not file.filename.endswith(".dcm"):
        raise HTTPException(status_code=400, detail="Invalid file format. Only DICOM files are allowed.")

    # Process DICOM file
    metadata = process_dicom(file.file)

    # Start workflow
    workflow_id = start_workflow(metadata)

    return {"message": "DICOM file uploaded successfully", "workflow_id": workflow_id}
