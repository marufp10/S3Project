import boto3

def list_s3_buckets():
    """Fetch and list all AWS S3 buckets in your account."""
    s3 = boto3.client('s3')  # Initialize S3 client
    response = s3.list_buckets()  # Get list of buckets
    
    bucket_names = [bucket["Name"] for bucket in response.get("Buckets", [])]
    
    if not bucket_names:
        print("No S3 buckets found!")
        return
    
    print("Your S3 Buckets:")
    for bucket in bucket_names:
        print(f"- {bucket}")
    
    # Save bucket names to a file
    with open("buckets.txt", "w") as file:
        file.write("\n".join(bucket_names))
    
    print("\n✅ Bucket names saved to 'buckets.txt'")

if __name__ == "__main__":
    list_s3_buckets()


    # Run the script again to see the output.
