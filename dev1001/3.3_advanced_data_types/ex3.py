# Sets Exercise

required_skills = {"python", "git", "problem-solving"}
candidate_skills = {"python", "java", "communication"}

# Given the above sets, write code to:
# 1. Add "communication" to required_skills if it's not already there.
required_skills.add("communication")
print(f"Added communication: {required_skills}")

# 2. Find out which skills the candidate has that are also required.
print(f"{candidate_skills & required_skills}")
print(f"{candidate_skills.intersection(required_skills)}")

# 3. Find out all unique skills possessed by either (required or candidate).
print(f"{candidate_skills | required_skills}")
print(f"{candidate_skills.union(required_skills)}")

# 4. Which skills are required but the candidate doesn't have.
print(f"{required_skills - candidate_skills}")
print(f"{required_skills.difference(candidate_skills)}")
