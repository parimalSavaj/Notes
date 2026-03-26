from dotenv import load_dotenv
load_dotenv()

import base64
from anthropic import Anthropic

client = Anthropic()

def chat_with_image(image_path, prompt):
    with open(image_path, "rb") as f:
        image_bytes = base64.b64encode(f.read()).decode("utf-8")

    response = client.messages.create(
        model="claude-sonnet-4-0",
        max_tokens=1000,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": "image/png",  # change if jpg
                            "data": image_bytes
                        }
                    },
                    {
                        "type": "text",
                        "text": prompt
                    }
                ]
            }
        ]
    )

    return response

# response = chat_with_image(
#     "/home/av69/me/Notes/Extra/Anthropic courses/Building with the Claude API/04 Features/images/prop1.png",
#     "What do you see in this image?"
# )
response = chat_with_image(
    "/home/av69/me/Notes/Extra/Anthropic courses/Building with the Claude API/04 Features/images/prop1.png",
    """
    Analyze the attached satellite image of a property with these specific steps:

    1. Residence identification: Locate the primary residence on the property by looking for:
    - The largest roofed structure
    - Typical residential features (driveway connection, regular geometry)
    - Distinction from other structures (garages, sheds, pools)

    2. Tree overhang analysis: Examine all trees near the primary residence:
    - Identify any trees whose canopy extends directly over any portion of the roof
    - Estimate the percentage of roof covered by overhanging branches (0-25%, 25-50%, 50-75%, 75%+)
    - Note particularly dense areas of overhang

    3. Fire risk assessment: For any overhanging trees, evaluate:
    - Potential wildfire vulnerability (ember catch points, continuous fuel paths to structure)
    - Proximity to chimneys, vents, or other roof openings if visible
    - Areas where branches create a "bridge" between wildland vegetation and the structure

    4. Defensible space identification: Assess the property's overall vegetative structure:
    - Identify if trees connect to form a continuous canopy over or near the home
    - Note any obvious fuel ladders (vegetation that can carry fire from ground to tree to roof)

    5. Fire risk rating: Based on your analysis, assign a Fire Risk Rating from 1-4:
    - Rating 1 (Low Risk): No tree branches overhanging the roof, good defensible space around the home
    - Rating 2 (Moderate Risk): Minimal overhang (<25% of roof), some separation between tree canopies
    - Rating 3 (High Risk): Significant overhang (25-50% of roof), connected tree canopies, multiple vulnerability points
    - Rating 4 (Severe Risk): Extensive overhang (>50% of roof), dense vegetation against structure

    For each item above (1-5), write one sentence summarizing your findings, with your final response being the numerical rating
    """
)

print(response)

# for image main thing is prompt!