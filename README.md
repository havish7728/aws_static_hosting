# AWS Static Website Hosting Library

A Python library to automate static website hosting on AWS using S3, with optional support for CloudFront integration. This library provides both a command-line interface (CLI) and a Python API for managing static website deployments efficiently.

## Features
- Create and configure S3 buckets for static website hosting.
- Upload and synchronize local directories with S3 buckets.
- Set custom index and error documents for the website.
- Optionally integrate with AWS CloudFront for content delivery.
- Easy-to-use CLI and Python API.

---

## Installation

Install the library using pip:

```bash
pip install aws_static_hosting
```

---

## Prerequisites

- Python 3.7 or higher.
- AWS account and access keys.
- AWS CLI configured (optional).

### Set up AWS credentials:

Generate access keys in your AWS Management Console and configure them using:

```bash
aws configure
```

---

## Usage

### **Command-Line Interface (CLI)**

The library provides a CLI for quick deployments.

#### Deploy a static website:

```bash
aws-static-hosting deploy --access-key <your-access-key> \
                          --secret-key <your-secret-key> \
                          --bucket <your-bucket-name> \
                          --directory <local-directory-path>
```

### **Python API**

You can also use the library in your Python scripts:

```python
from aws_static_hosting.hosting import StaticWebsiteHosting

# Initialize the hosting manager
hosting = StaticWebsiteHosting(
    aws_access_key="<your-access-key>",
    aws_secret_key="<your-secret-key>",
    region_name="us-east-1"
)

# Create an S3 bucket
hosting.create_bucket("my-static-website")

# Enable static website hosting
hosting.enable_static_hosting(
    bucket_name="my-static-website",
    index_document="index.html",
    error_document="error.html"
)

# Upload local files to the bucket
hosting.upload_files("my-static-website", "./website-files")
```

---

## Requirements

### Python Dependencies:
- `boto3`: AWS SDK for Python.
- `click`: For the command-line interface.

Install dependencies using:

```bash
pip install -r requirements.txt
```

### AWS Permissions:
Ensure the IAM user or role has the following permissions:
- `s3:CreateBucket`
- `s3:PutBucketWebsite`
- `s3:PutObject`
- `s3:DeleteObject`

---

## Example

Here is an example workflow to deploy a static website:

1. Create a local directory with your website files:
   ```
   /my-website/
   ├── index.html
   ├── error.html
   └── assets/
       ├── style.css
       └── script.js
   ```

2. Deploy the website:

   ```bash
   aws-static-hosting deploy --access-key YOUR_ACCESS_KEY \
                             --secret-key YOUR_SECRET_KEY \
                             --bucket my-static-website \
                             --directory ./my-website
   ```

3. Access the website via the S3 static website URL:
   ```
   http://my-static-website.s3-website-<region>.amazonaws.com
   ```

---

## Future Features
- Automatic CloudFront distribution setup.
- Support for Route 53 custom domain integration.
- More deployment customization options.

---

## Contributing

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a feature branch.
3. Submit a pull request.

---


## Author

**Havish Gadey**  
[GitHub](https://github.com/havish7728) | [Email](mailto:havish.gadey@gmail.com)
