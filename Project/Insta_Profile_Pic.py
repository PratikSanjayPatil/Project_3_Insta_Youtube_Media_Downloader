import instaloader

def download_profile_picture(username):
    # Create an instance of Instaloader
    loader = instaloader.Instaloader()

    try:
        
        profile = instaloader.Profile.from_username(loader.context, username)

        # Download the profile picture
        loader.download_profilepic(profile)

        print("Profile picture downloaded successfully!")

    except instaloader.exceptions.ProfileNotExistsException:
        print(username,"Instagram profile does not exist.")

# Provide the Instagram username for which you want to download the profile picture
username = input("Enter Username: ")

# Call the function to download the profile picture
download_profile_picture(username)