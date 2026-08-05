def generate_hashtags(topic):
    return [
        "#Pinterest",
        "#AI",
        "#Design",
        "#Marketing",
        "#Automation",
        f"#{topic.replace(' ', '')}"
    ]


if __name__ == "__main__":
    print(generate_hashtags("Luxury Birthday"))
