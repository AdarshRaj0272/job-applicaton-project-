def shortlisting(age, experience, min_age, min_experience):

    if age >= min_age and experience >= min_experience:

        return True

    else:

        return False





min_age = int(input("Enter the minimum age: "))

min_experience = int(input("Enter the minimum years of experience: "))





num_candidates = int(input("Enter the number of candidates: "))



shortlisted = []

rejected = []



for I in range(num_candidates):

    print(f"\nCandidate {I + 1}:")

    name = input("Enter candidate's name: ")

    age = int(input("Enter candidate's age: "))

    experience = int(input("Enter candidate's years of experience: "))



    

    if shortlisting(age, experience, min_age, min_experience):

        shortlisted.append(name)

    else:

        rejected.append(name)





print("\nShortlisted Candidates:")

if shortlisted:

    for name in shortlisted:

        print(f"- {name}")

else:

    print("None")



print("\nRejected Candidates:")

if rejected:

    for name in rejected:

        print(f"- {name}")

else:

    print("None")