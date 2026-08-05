def seo(title):
    return {
        "title": title,
        "description": f"Pinterest content for {title}",
        "keywords": [
            "Pinterest",
            "AI",
            "Marketing",
            title
        ]
    }

if __name__ == "__main__":
    print(seo("Birthday Poster"))
