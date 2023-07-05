import requests
import datetime

# Set the Nexus repository information
nexus_url = "http://nexus.example.com"
repository_name = "my-repo"
username = "my-username"
password = "my-password"
build_number_tag = "build-"

# Get the list of images in the repository
response = requests.get(f"{nexus_url}/service/rest/v1/search?repository={repository_name}&format=docker",
                        auth=(username, password))
response.raise_for_status()
images = response.json()["items"]

# Filter the images by tag
images = [image for image in images if build_number_tag in image["name"]]

# Sort the images by creation date, in descending order
images = sorted(images, key=lambda i: i["created"], reverse=True)

# Delete the older images, except for the latest 3
for image in images[3:]:
    image_digest = image["digest"]
    response = requests.delete(f"{nexus_url}/repository/{repository_name}/docker/{image_digest}",
                               auth=(username, password))
    response.raise_for_status()
    print(f"Deleted image {image_digest}")
