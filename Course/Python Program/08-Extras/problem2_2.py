# Develop a Club Membership Management System in Python with a menu-driven
# interface. The system should efficiently manage the memberships of two clubs: the
# Math Club and the Science Club. Each club has its own set of initial members. Use
# sets. Make it Menu driven.
# Tasksto be implemented:
# 1. Display the initial memberships of both the Math Club and the Science Club.
# 2. Add a new member to the Math Club and display the updated membership.
# 3. Remove a member from the Science Club and display the updated
# membership.
# 4. Discard a member from the Math Club and display the updated membership.
# 5. Find and display the members who belong to at least one club.
# 6. Find and display the members who belong to both the Math Club and the
# Science Club.
# 7. Find and display the members exclusive to each club.
# 8. Check if the Math Club is a subset of at least one club and display the result.
# 9. Check if the Math Club and the Science Club are disjoint (have no members in
# common) and display the result.
# 10. Exit the program.
# Implement a Python program that fulfills the requirements mentioned above. Use
# functions to encapsulate each task and create a menu-driven interface that allows
# the user to interact with the system.

def display_memberships(math_club, science_club):
    print("Math Club Members:", math_club)
    print("Science Club Members:", science_club)
    print()

def add_member(math_club):
    new_member = input("Enter the name of the new member to add to the Math Club: ")
    math_club.add(new_member)
    print(f"{new_member} has been added to the Math Club.\n")

def remove_member(science_club):
    member_to_remove = input("Enter the name of the member to remove from the Science Club: ")
    if member_to_remove in science_club:
        science_club.remove(member_to_remove)
        print(f"{member_to_remove} has been removed from the Science Club.\n")
    else:
        print(f"{member_to_remove} is not a member of the Science Club.\n")

def discard_member(math_club):
    member_to_discard = input("Enter the name of the member to discard from the Math Club: ")
    math_club.discard(member_to_discard)
    print(f"{member_to_discard} has been discarded from the Math Club (if they were a member).\n")

def members_in_at_least_one_club(math_club, science_club):
    all_members = math_club.union(science_club)
    print("Members in at least one club:", all_members)
    print()

def members_in_both_clubs(math_club, science_club):
    common_members = math_club.intersection(science_club)
    print("Members in both clubs:", common_members)
    print()

def exclusive_members(math_club, science_club):
    exclusive_math = math_club - science_club
    exclusive_science = science_club - math_club
    print("Members exclusive to Math Club:", exclusive_math)
    print("Members exclusive to Science Club:", exclusive_science)
    print()

def check_subset(math_club, science_club):
    is_subset = math_club.issubset(science_club)
    print("Is Math Club a subset of Science Club?", is_subset)
    print()

def check_disjoint(math_club, science_club):
    are_disjoint = math_club.isdisjoint(science_club)
    print("Are Math Club and Science Club disjoint?", are_disjoint)
    print()

def main():
    # Initial memberships
    math_club = {"Alice", "Bob", "Charlie"}
    science_club = {"David", "Eve", "Frank", "Alice"}

    while True:
        print("Club Membership Management System")
        print("1. Display Initial Memberships")
        print("2. Add Member to Math Club")
        print("3. Remove Member from Science Club")
        print("4. Discard Member from Math Club")
        print("5. Find Members in At Least One Club")
        print("6. Find Members in Both Clubs")
        print("7. Find Exclusive Members")
        print("8. Check if Math Club is a Subset of Science Club")
        print("9. Check if Clubs are Disjoint")
        print("10. Exit")
        
        choice = input("Enter your choice (1-10): ")
        
        if choice == '1':
            display_memberships(math_club, science_club)
        elif choice == '2':
            add_member(math_club)
        elif choice == '3':
            remove_member(science_club)
        elif choice == '4':
            discard_member(math_club)
        elif choice == '5':
            members_in_at_least_one_club(math_club, science_club)
        elif choice == '6':
            members_in_both_clubs(math_club, science_club)
        elif choice == '7':
            exclusive_members(math_club, science_club)
        elif choice == '8':
            check_subset(math_club, science_club)
        elif choice == '9':
            check_disjoint(math_club, science_club)
        elif choice == '10':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()