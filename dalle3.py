from openai import OpenAI
import support

support.set_env_vars_from_json('env_vars.json')

def save_dalle3_img(prompt):
  file_path = f"images/{support.timestamp()}.jpg"

  client = OpenAI()
  print("Generating dalle3 image...")
  response = client.images.generate(
    model="dall-e-3",
    prompt=prompt,
    size="1024x1024",
    quality="standard",
    n=1
  )

  image_url = response.data[0].url
  support.download_image(image_url, file_path)
  print(f"Saved image: {file_path}")

if __name__ == '__main__':
  prompt = input("Enter image prompt: ")
  save_dalle3_img(prompt)