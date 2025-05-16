GCP bucket test
09-Mar-2025

python -m venv .venv
source .venv/bin/activate

pip install google-cloud-storage
pip install --upgrade pip


gcloud storage buckets list


Final end-to-end example
example02.py