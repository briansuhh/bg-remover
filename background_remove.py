import requests
import os

# make a list of all pics inside the folder
input_folder = 'pictures/'
image_files = os.listdir(input_folder)

i = 1
for picture in image_files:
    # create a path to the picture
    image_path = os.path.join(input_folder, picture)

    # create a post request to the bg remover api
    response = requests.post(
        'https://api.remove.bg/v1.0/removebg',
        headers={'X-Api-Key': 'HMZgt5VbKo9JoK964HxEoEnD'},
        files={'image_file': open(image_path, 'rb')}
    )

    # check if the request is successful
    if response.status_code == 200:
        # make the result folder
        output_folder = 'results/'
        os.makedirs(output_folder, exist_ok=True)
        os.chdir(output_folder)

        with open(f'removebgresult{i}.jpg', 'wb') as f:
            f.write(response.content)
        print("Imaged processed and saved")
    else:
        print(f"Error: {response.status_code} - {response.text}")
    i+=1
    os.chdir('..')