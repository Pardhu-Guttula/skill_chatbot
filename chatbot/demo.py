# open_ai/demo.py
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import os

# ... (previous code)


def get_model_response(prompt):
    # Load your dataset
    data = pd.read_csv("D:\\OPEN_AI\\New folder\\open_ai\\chatbot\\final_data.csv")

    # Load a pre-trained sentence transformer model
    model = SentenceTransformer("paraphrase-MiniLM-L6-v2")

    # Specify the output file path
    output_file_path = "D:\\OPEN_AI\\New folder\\open_ai\\chatbot\\answers.csv"
    # Clear saved information if the output file exists
    if os.path.exists(output_file_path):
        os.remove(output_file_path)
        print(f"Saved information cleared from {output_file_path}")
    else:
        print("No saved information found.")

    # Encode the prompt
    prompt_embedding = model.encode(prompt)

    # Reshape the prompt embedding to 2D array for cosine similarity calculation
    prompt_embedding = prompt_embedding.reshape(1, -1)

    # Variations of skills considered
    skill_variations = {
        "ui/ux designer": [
            "ui/ux designer",
            "ux/ui designer",
            "user interface designer",
            "user experience designer",
            "ux designer",
            "ui designer",
        ],
        "ai engineer": [
            "ai engineer",
            "artificial intelligence engineer",
            "ai developer",
        ],
        "devops engineer": ["devops engineer"],
        "data scientist": ["data scientist"],
        "cloud engineer": ["cloud engineer"],
        "ux technology": [
            "ux technology",
            "user experience technology",
            "user interface technology",
        ]
        # Add more variations for other skills
    }

    def get_skill_similarity(row):
        skill = row["Skill"]

        # Use the prompt_embedding directly, as it's already calculated
        similarity = cosine_similarity(
            prompt_embedding, model.encode(skill).reshape(1, -1)
        )[0][0]
        return similarity

    # Calculate similarity scores for skills with variations
    data["Skill_Similarity"] = data.apply(get_skill_similarity, axis=1)

    # Filter candidates based on skill similarity scores
    threshold = 0.6  # Adjust this threshold based on your needs for skills
    filtered_candidates = data[data["Skill_Similarity"] >= threshold]

    print(filtered_candidates)  # Add this line to print the filtered candidates

    if not filtered_candidates.empty:
        # Save matching candidates to a CSV file
        filtered_candidates.to_csv(output_file_path, index=False)
        output = {
            "result": "success",
            # 'message': 'Matching candidates saved to answers.csv',
            "candidates": filtered_candidates.to_dict(
                "records"
            ),  # Convert DataFrame to list of dictionaries
        }
    else:
        output = {"result": "failure", "message": None}

    print(output)  # Add this line to print the output

    return output
