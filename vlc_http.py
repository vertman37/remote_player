import subprocess

# Command to run VLC in HTTP mode
vlc_command = [
    "cvlc",  # or "vlc" depending on your setup
    "--intf", "http",  # Enable the HTTP interface
    "--http-host", "0.0.0.0",  # Bind to localhost
    "--http-port", "8080",  # Set the HTTP port (default is 8080)
    "--http-password", "pw"  # Set a password for the HTTP interface (optional)
]

# Run the VLC command
subprocess.run(vlc_command)
