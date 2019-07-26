import pytest
import datetime
import os
import sys

from gcp import GCSBucket


now = datetime.datetime.now()


def pytest_addoption(parser):
    group = parser.getgroup('gcs')
    group.addoption(
        "--gcs-service-key",
        action="store",
        default=None,
        help="path to Google Cloud service key credentials"
    )
    group.addoption(
        "--gcs-bucket",
        action="store",
        default=None,
        help="name of Google Cloud Storage bucket for storing reports"
    )
    group.addoption(
        "--gcs-filename",
        action="store",
        default="report",
        help="filenames are prefixed by a timestamp to uniquely identify the report"
    )


# this hook function needs to run before pytest-html pytest_configure, 
# which creates the HTMLReport
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    global now

    bucket = config.getoption('gcs_bucket')
    key = config.getoption('gcs_service_key')
    filename = config.getoption('gcs_filename')

    _gcs_required = [key, bucket]
    if any(_gcs_required):
        if not all(_gcs_required):
            pytest.exit("ERROR: gcs plugin requires: --gcs-service-key and --gcs-bucket")    

        # if no local html filename was specified, set a default
        if not config.getoption('htmlpath'):
            timestamp = now.strftime("%Y%m%dT%H%M%S") 
            vars(config.option)['htmlpath'] = f'{timestamp}_{filename}.html'
        # include the CSS in the report so it will render properly
        vars(config.option)['self_contained_html'] = True


def pytest_sessionfinish(session, exitstatus):
    global now

    bucket = session.config.getoption('gcs_bucket')
    key = session.config.getoption('gcs_service_key')
    if bucket:
        htmlpath = session.config.getoption('htmlpath')
        src = htmlpath
        year, month, day = f"{now.year:04}", f"{now.month:02}", f"{now.day:02}"
        dst = f'{year}/{month}/{day}/{htmlpath}'
        print(f"\nUploading {src} to https://storage.cloud.google.com/{bucket}/{dst}")
        bucket = GCSBucket(key, bucket)
        bucket.upload(src, dst)

        os.unlink(src)
