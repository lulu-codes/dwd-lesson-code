# profile_updater.py
user_name = "Alex"
user_city = "New York"
years_experience = 3.5 # Can be a float
project_count = 15

# Current basic output
# print("User:", user_name)
# print("Location:", user_city)
# print("Experience (Years):", years_experience)
# print("Projects Completed:", project_count)

print(f'{user_name} from {user_city} has {years_experience:.1f} years of experience and completed {project_count} projects.')

years_experience = 5 # update value of variable
print(f'{user_name} from {user_city} has {years_experience:.1f} years of experience and completed {project_count} projects.')
# Get the value of years_experience, add 1 to it, store result in years_experience
# years_experience = years_experience + 1 # this overrides previous variables
years_experience_plus_1 = years_experience + 1 # this preserves the original variable but adds a new variable to store the original variable + 1
print(f'{user_name} from {user_city} has {years_experience_plus_1:.1f} years of experience and completed {project_count} projects.')


years_experience = years_experience + 1
print(years_experience)

x, y = 5, 10 # multiple assignment
print(x, y)
