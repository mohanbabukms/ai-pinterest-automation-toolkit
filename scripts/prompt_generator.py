def generate_prompt(topic):
    prompt = f"""
Create a professional Pinterest poster about {topic}.

Requirements:
- High quality
- 2:3 aspect ratio
- Premium typography
- Pinterest optimized
"""

    return prompt


if __name__ == "__main__":
    print(generate_prompt("Luxury Birthday"))
