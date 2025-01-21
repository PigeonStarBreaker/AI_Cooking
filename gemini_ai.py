import google.generativeai as genai
import json

genai.configure(api_key="API_KEY HERE")
model = genai.GenerativeModel("gemini-1.5-flash")
# response = model.generate_content("Explain how AI works")
ingredients_user = [
    ["chicken", "carrot", "radish"],  # User 5 ingredients

]
def gemini_food_recommendation(ingredients_list):
    """
    This function recommends food based on user-provided ingredients.

    Steps:
    1. Convert the input ingredients to a JSON format.
    2. Prepare a Gemini Prompt for generating food recommendations.
    3. Call the Gemini API and process the response.
    """

    # Create JSON structure for ingredients and recommendations
    json_data = [{"ingredients": ingredients} for ingredients in ingredients_list]

    # Convert JSON structure to string for embedding in the prompt
    json_str = json.dumps(json_data, indent=4)

    # Gemini Prompt
    # prompt = f"""
    # You are a food critic, skilled at recommending dishes based on available ingredients.
    # Your task is to process the user's input (ingredients) and provide suitable dish recommendations as well as suggesting the recipe.
    # The user input is in a JSON format between three backticks below.
    # Update the "recommended_food" field in the JSON with your suggestions.
    # Update the "recipe" field with the recipe for the recommended food.
    #
    # Instructions:
    # - Only return the updated JSON code as output.
    # - If the user input violates API policies, set "recommended_food" to "No food suggestion available".
    #
    # ```z
    # {json_str}
    # ```
    # """
    prompt = f"""
       You are a food critic, skilled at recommending dishes based on available ingredients. 
       Your task is to process the user's input (ingredients) and provide suitable dish recommendations as well as suggesting the recipe.
       The user input is in a JSON format between three backticks below. 
       Return only one recommended recipe 
       Return instructions on how to cook the recipe
       Response should follow the following example
       
       Recommended Dish: Fruit Salad with Honey-Lime Dressing
       Ingredients:
       1 medium apple (e.g., Honeycrisp or Fuji), cored and diced
       1 ripe banana, peeled and sliced
       1 orange, peeled and segmented
       1 cup grapes (red or green), halved if large
       2 tablespoons honey
       1 tablespoon lime juice
       Optional:  a pinch of cinnamon
       
       Instructions:
       1. Prepare the fruit:  Wash all fruits thoroughly. Core and dice the apple to prevent browning. Peel and slice the banana.  Peel and segment the orange. Halve the grapes if they are large.
       2. Combine the fruit: Gently combine all the prepared fruits in a medium-sized bowl. Be careful not to overmix, as this can bruise the fruit.
       3. Make the dressing: In a small bowl, whisk together the honey and lime juice.  If desired, add a pinch of cinnamon for extra warmth.
       4. Dress the salad: Pour the honey-lime dressing over the fruit salad and toss gently to coat.
       5. Serve: Serve immediately or chill for later.  The fruit salad is best enjoyed fresh.

       ```z
       {json_str}
       ```
       """

    # print("Generated Prompt:\n", prompt)  # For debugging purposes

    # Simulate API Call
    response = model.generate_content(prompt)
    # time.sleep(5)  # Simulate API latency

    return response.text
# print(gemini_food_recommendation(ingredients_user))