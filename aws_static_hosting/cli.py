import click
from aws_static_hosting.hosting import StaticWebsiteHosting

@click.group()
def cli():
    """AWS Static Website Hosting CLI"""
    pass

@cli.command()
@click.option('--access-key', prompt=True, help='AWS Access Key')
@click.option('--secret-key', prompt=True, help='AWS Secret Key')
@click.option('--bucket', prompt=True, help='S3 Bucket Name')
@click.option('--directory', prompt=True, help='Local Directory Path')
def deploy(access_key, secret_key, bucket, directory):
    """Deploy a static website to AWS S3"""
    hosting = StaticWebsiteHosting(access_key, secret_key)
    hosting.create_bucket(bucket)
    hosting.enable_static_hosting(bucket)
    hosting.upload_files(bucket, directory)

if __name__ == "__main__":
    cli()
