## remove-image-nexus-private
I want remove image with tag build-number but i want delete just image befor 3 last and delete other 
such as : 
image:build-1 
image:build-2
image:build-3 
image:build-4 
image:build-5 
image:build-6
image:build-7
i want delete image:buid-{1-4} and keep image:build-{5-7}
first: Get the list of images in the repository
```
response = requests.get(f"{nexus_url}/service/rest/v1/search?repository={repository_name}&format=docker",
                        auth=(username, password))
response.raise_for_status()
images = response.json()["items"]
```
```
{
  "items" : [ {
    "downloadUrl" : "https://nexus.compony.com/repository/docker-hosted/v2/-/blobs/sha256:b30e445b9bcbf794a628e4dd31c3089f8a40949d0b9bacc95b928",
    "path" : "v2/-/blobs/sha256:b30e445b9bcbf794a628e4dd31cb999588105c3089f8a40949d0b9bacc95b928",
    "id" : "bmlrLWRvY2tlci1ob6NGIzNzg2NTM1OTFjNjcyMjliMWUyMzRiNDY1NzZkODY",
    "repository" : "docker-hosted",
    "format" : "docker",
    "checksum" : {
      "sha1" : "9126f24bc375ddaf10fd5c9792c17217174f77d1",
      "sha256" : "b30e445b9bcbf794a628e4dd31cb999588105c3089f8a40949d0b9bacc95b928"
    },
    "contentType" : "application/vnd.docker.image.rootfs.diff.tar.gzip",
    "lastModified" : "2023-02-13T08:48:04.935+00:00",
    "lastDownloaded" : null,
    "uploader" : "docker",
    "uploaderIp" : "[2a01:4f8:1c1e:da8c::1]",
    "fileSize" : 1260,
    "blobCreated" : "2023-02-13T08:48:04.935+00:00",
    "lastDownloaded" : "2023-07-04T07:06:59.366+00:00"
  }
```
after that 
# Sort the images by creation date, in descending order
```
images = sorted(images, key=lambda i: i["created"], reverse=True)
```
finally delete:
```
for image in images[3:]:
    image_digest = image["digest"]
    response = requests.delete(f"{nexus_url}/repository/{repository_name}/docker/{image_digest}",
                               auth=(username, password))
    response.raise_for_status()
    print(f"Deleted image {image_digest}")
```
This code first filters the list of images to include only those that have a tag containing the build_number_tag string. 
Then, it sorts the filtered images by creation date, in descending order, and deletes all images except for the latest 3.
Note that the build_number_tag variable is used to filter the images by their tag. 
You can modify this variable to match the tag format used in your images.
