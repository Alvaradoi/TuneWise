import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


def get_spotify_data():
    # Set up credentials (Replace with your own client ID and client secret)
    client_id = "ca1fc94bd5a44b2ba8e66367802a5285"
    client_secret = "99b261787d1940aaa4915208e8cec5c1"

    # Initialize Spotipy with user credentails
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

    # Search for a playlist (Replace with your desired search query)
    results = sp.search(q='Your Search Query', limit=20, type='playlist')
    playlists = results['playlists']['items']

    # List out the playlists found
    for idx, playlist in enumerate(playlists):
        print(f"{idx + 1}. {playlist['name']}")


def main():
    print("Welcome to SpotiWise!")

    # Initial menu for user to decide what they want to do
    print("1. Search Spotify Playlists")
    print("2. Analyze Playlist")
    # Add more options as your project grows

    choice = input("Please enter the number of your choice: ")

    if choice == '1':
        get_spotify_data()
    elif choice == '2':
        print("This feature is under development.")
        # Replace with function that analyzes a playlist
    else:
        print("Invalid choice. Exiting.")


if __name__ == "__main__":
    main()
