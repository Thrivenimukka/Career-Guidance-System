import streamlit as st
import pandas as pd

from recommender import recommend_careers


# Page configuration
st.set_page_config(
    page_title="Career Guidance System",
    page_icon="🎓",
    layout="wide"
)


# Title
st.title("🎓 Career Guidance System")

st.write(
    "Find suitable career options based on your skills and interests."
)

st.divider()


# Student information
st.header("👩‍🎓 Student Information")

name = st.text_input("Enter your name")

branch = st.selectbox(
    "Select your branch",
    [
        "Data Science",
        "Computer Science",
        "Information Technology",
        "Electronics",
        "Other"
    ]
)


# Skills
st.header("💡 Select Your Skills")

skills = [
    "Python",
    "Java",
    "Machine Learning",
    "Deep Learning",
    "Artificial Intelligence",
    "Statistics",
    "Mathematics",
    "Data Analysis",
    "Data Visualization",
    "Excel",
    "Programming",
    "Problem Solving",
    "Communication",
    "Database",
    "Business"
]


selected_skills = st.multiselect(
    "Choose the skills you are interested in:",
    skills
)


# Career recommendation button
if st.button("🔍 Get Career Recommendations"):

    if not name:
        st.warning("Please enter your name.")

    elif len(selected_skills) == 0:
        st.warning("Please select at least one skill.")

    else:

        results = recommend_careers(selected_skills)

        st.success(
            f"Hello {name}! Here are your recommended careers."
        )

        st.write(
            f"**Branch:** {branch}"
        )

        st.divider()

        st.header("🏆 Recommended Careers")

        # Display top 5 careers
        for i, result in enumerate(results[:5], start=1):

            st.subheader(
                f"{i}. {result['career']}"
            )

            st.write(
                result["description"]
            )

            st.write(
                f"**Match Score:** {result['score']}%"
            )

            if result["matching_skills"]:

                st.write(
                    "**Matching Skills:** "
                    + ", ".join(result["matching_skills"])
                )

            st.divider()


        # DataFrame
        st.header("📊 Career Match Summary")

        table_data = []

        for result in results:

            table_data.append({
                "Career": result["career"],
                "Match Score (%)": result["score"]
            })

        df = pd.DataFrame(table_data)

        st.dataframe(
            df,
            use_container_width=True
        )