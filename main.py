import requests
import pprint

def get_random_dog_image():
    base_url = "https://dog.ceo/api"
    response = requests.get(f"{base_url}/breeds/image/random")
    data = response.json()
    pprint.pprint(data)

def get_list_of_breeds():
    base_url = "https://dog.ceo/api"
    response = requests.get(f"{base_url}/breeds/list")
    data = response.json()
    pprint.pprint(data)

def get_random_dog_image_by_breed(breed):
    base_url = "https://dog.ceo/api"
    response = requests.get(f"{base_url}/breed/{breed}/images/random")
    data = response.json()
    pprint.pprint(data)

def get_list_of_sub_breeds(breed):
    base_url = "https://dog.ceo/api"
    response = requests.get(f"{base_url}/breed/{breed}/list")
    data = response.json()
    pprint.pprint(data)

def get_random_dog_image_by_sub_breed(breed, sub_breed):
    base_url = "https://dog.ceo/api"
    response = requests.get(f"{base_url}/breed/{breed}/{sub_breed}/images/random")
    data = response.json()
    pprint.pprint(data)

if __name__ == '__main__':
    print("Рандомное изображение собаки:")
    get_random_dog_image()
    print("\nСписок пород:")
    get_list_of_breeds()
    print("\nРандомное изображение собаки по породе:")
    get_random_dog_image_by_breed("bulldog")
    print("\nСписок подпород:")
    get_list_of_sub_breeds("hound")
    print("\nРандомное изображение собаки по подпороде:")
    get_random_dog_image_by_sub_breed("hound", "afghan")
