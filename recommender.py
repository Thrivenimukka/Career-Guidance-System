from career_data import career_data


def recommend_careers(selected_skills):

    results = []

    selected_skills = set(selected_skills)

    for career in career_data:

        career_skills = set(career["skills"])

        matching_skills = selected_skills.intersection(career_skills)

        if len(selected_skills) > 0:
            score = (len(matching_skills) / len(selected_skills)) * 100
        else:
            score = 0

        results.append({
            "career": career["career"],
            "description": career["description"],
            "score": round(score, 2),
            "matching_skills": list(matching_skills)
        })

    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return results