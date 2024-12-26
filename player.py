import pyglet

class AudioPlayer:
    def __init__(self):
        self.player = pyglet.media.Player()
        self.source = None
        self.is_loaded = False

    def load(self, filepath):
        """Load an audio file."""
        try:
            self.source = pyglet.media.load(filepath)
            self.player.queue(self.source)
            self.is_loaded = True
        except Exception as e:
            print(f"Error loading file: {e}")
    
    def play(self):
        """Play the loaded audio."""
        if self.is_loaded:
            self.player.play()
        else:
            print("No audio loaded.")
    
    def stop(self):
        """Stop the audio playback."""
        if self.player.playing:
            self.player.pause()
            
    def rewind(self):
        """Rewind the audio to the start."""
        if self.is_loaded:
            self.player.seek(0)  # Rewinds to the start (0 seconds)
            self.player.play()   # Optionally, immediately start playing after rewinding
        else:
            print("No audio loaded.")
    
    def set_volume(self, volume):
        """Set the volume (0.0 to 1.0)."""
        if 0.0 <= volume <= 1.0:
            self.player.volume = volume
        else:
            print("Volume must be between 0.0 and 1.0.")

# Usage Example:
if __name__ == "__main__":
    player = AudioPlayer()

    # Load an audio file
    player.load('music.mp3')  # Replace with your file path (MP3, OGG, or WAV)

    # Play the audio
    player.play()

    # Set volume to 0.5
    player.set_volume(0.5)

    # Stop the audio after a delay (e.g., 5 seconds)
    pyglet.clock.schedule_once(lambda dt: player.stop(), 5)

    # Keep the application running so the sound can play
    pyglet.app.run()
