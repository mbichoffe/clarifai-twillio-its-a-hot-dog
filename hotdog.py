from clarifai.rest import ClarifaiApp, Image as ClImage

app = ClarifaiApp()

def hotdog_or_nothotdog(image_url):
    model = app.models.get('food-items-v1.0')
    image = ClImage(url=image_url)
    response_data = model.predict([image])


    concepts = response_data['outputs'][0]['data']['concepts']

    concept_names = [concept['name'] for concept in concepts]

    if 'hot dog' in concept_names:
        return "It's a hot dog!"

    return "It's not a hot dog."
