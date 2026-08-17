skill = [input() for _ in range(5)]
skill_record = tuple(skill)

first_three = skill_record[:3]
last_two = skill_record[-2:]
alternate_skills = skill_record[::2]
reversed_skills = skill_record[::-1]

print(f"Skill Record: {skill_record}")
print(f"First Three: {first_three}")
print(f"Last Two: {last_two}")
print(f"Alternate Skills: {alternate_skills}")
print(f"Reversed Skills: {reversed_skills}")