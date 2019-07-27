## Installation

```
$ git clone https://github.com/darlenew/pytest-gcs.git
$ pip install .
```

## Help

```
gcs:
  --gcs-service-key=GCS_SERVICE_KEY
                        path to Google Cloud service key credentials
  --gcs-bucket=GCS_BUCKET
                        name of Google Cloud Storage bucket for storing
                        reports
  --gcs-filename=GCS_FILENAME
                        filenames are prefixed by a timestamp to uniquely
                        identify the report
```

## Usage

```
$ pytest --gcs-service-key=/path/to/credentials.json \
         --gcs-bucket=EXISTING_BUCKET_NAME \
         --gcs-filename=BASE_FILENAME
```
