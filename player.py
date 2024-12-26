import pygame

class Player:
    def __init__(self):
        # Initialize the pygame mixer
        pygame.mixer.init()
        self.is_playing = False
        self.is_paused = False
        self.current_track = None
        self.volume = 1.0  # Full volume by default

    def load(self, track_path):
        """Load a music track."""
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
        pygame.mixer.music.load(track_path)
        self.current_track = track_path

    def play(self):
        """Play the loaded track."""
        if not self.is_playing:
            pygame.mixer.music.play(-1)  # -1 means loop indefinitely
            self.is_playing = True
            self.is_paused = False

    def pause(self):
        """Pause the music."""
        if self.is_playing and not self.is_paused:
            pygame.mixer.music.pause()
            self.is_paused = True

    def unpause(self):
        """Unpause the music."""
        if self.is_paused:
            pygame.mixer.music.unpause()
            self.is_paused = False

    def stop(self):
        """Stop the music."""
        if self.is_playing:
            pygame.mixer.music.stop()
            self.is_playing = False
            self.is_paused = False

    def set_volume(self, volume):
        """Set the volume (0.0 to 1.0)."""
        self.volume = volume
        pygame.mixer.music.set_volume(self.volume)

    def get_volume(self):
        """Get the current volume."""
        return self.volume

    def is_playing(self):
        """Check if the music is currently playing."""
        return self.is_playing


# Usage example
if __name__ == "__main__":
    player = Player()
    player.load('music.mp3')  # Replace with your music file path
    player.play()

    # Here, you can control the player using methods like:
    # player.pause(), player.unpause(), player.stop(), player.set_volume(0.5), etc.
