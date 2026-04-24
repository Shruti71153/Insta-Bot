from instabot import Bot

# Function to display the menu
def display_menu():
    print("Menu:")
    print("1. Login")
    print("2. Follow")
    print("3. Upload Photo")
    print("4. Unfollow")
    print("5. Send Message")
    print("6. Get Followers")
    print("7. Get Following")
    print("8. Exit")

# Main function
def main():
    bot = Bot()
    logged_in = False
    
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == "1":
            if not logged_in:
                username = input("Enter your Instagram username: ")
                password = input("Enter your Instagram password: ")
                bot.login(username=username, password=password)
                logged_in = True
            else:
                print("You are already logged in.")
        
        elif choice == "2":
            if logged_in:
                username_to_follow = input("Enter the username you want to follow: ")
                bot.follow(username_to_follow)
            else:
                print("Please login first.")
        
        elif choice == "3":
            if logged_in:
                image_path = input("Enter the path to the image you want to upload: ")
                caption = input("Enter the caption for the photo: ")
                bot.upload_photo(image_path, caption=caption)
            else:
                print("Please login first.")
        
        elif choice == "4":
            if logged_in:
                username_to_unfollow = input("Enter the username you want to unfollow: ")
                bot.unfollow(username_to_unfollow)
            else:
                print("Please login first.")
        
        elif choice == "5":
            if logged_in:
                recipient = input("Enter the recipient's username: ")
                message = input("Enter the message: ")
                bot.send_message(message, [recipient])
            else:
                print("Please login first.")
        
        elif choice == "6":
            if logged_in:
                username_to_check = input("Enter the username to get followers: ")
                followers = bot.get_user_followers(username_to_check)
                for follower in followers:
                    print(bot.get_user_info(follower))
            else:
                print("Please login first.")
        
        elif choice == "7":
            if logged_in:
                username_to_check = input("Enter the username to get following: ")
                following = bot.get_user_following(username_to_check)
                for followeing in following:
                    print(bot.get_user_info(following))
            else:
                print("Please login first.")
        
        elif choice == "8":
            print("Exiting program.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
