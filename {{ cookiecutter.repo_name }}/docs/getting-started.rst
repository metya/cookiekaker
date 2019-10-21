Getting started
===============

This is where you describe how to get set up on a clean install



Syncing data to S3
^^^^^^^^^^^^^^^^^^

* `make sync_data_to_s3` will use `aws s3 sync` to recursively sync files in `data/` up to `s3://{{ cookiecutter.s3_bucket }}/data/`.
* `make sync_data_from_s3` will use `aws s3 sync` to recursively sync files from `s3://{{ cookiecutter.s3_bucket }}/data/` to `data/`.
* `make sync_data_to_minio` will use `rclone --size-only sync {{ cookiecutter.minio }}/data/ data/ --stats-one-line -P --stats 2s`

