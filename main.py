import mpv
import os
import time
import random

def draw_visualizer(length=20):
    # Membuat bar visualizer acak agar terlihat bergerak
    chars = [" ", "▂", "▃", "▄", "▅", "▆", "▇", "█"]
    bar = "".join(random.choice(chars) for _ in range(length))
    return f"\r\033[32m{bar}\033[0m" # Warna hijau

def main():
    try:
        player = mpv.MPV(video=False, ytdl=False)
        player.volume = 50 
    except:
        print("[!] MPV Error.")
        return

    songs = [f for f in os.listdir('.') if f.endswith(('.mp3', '.MP3'))]
    if not songs:
        print("[!] Tidak ada lagu.")
        return

    os.system('clear')
    print("\033[95m" + "="*35)
    print("      FMusik-B VISUALIZER")
    print("="*35 + "\033[0m")
    
    for i, song in enumerate(songs, 1):
        print(f"\033[94m[{i}]\033[0m {song}")

    try:
        pilih = int(input("\nNomor lagu: ")) - 1
        current_song = songs[pilih]
        player.play(current_song)
        
        print(f"\n[▶] Playing: \033[1m{current_song}\033[0m")
        print("\nKontrol: [p]Pause [+]Vol+ [-]Vol- [q]Quit")
        
        # Loop Visualizer
        while player.playback_abort != 'die':
            if not player.pause:
                # Menampilkan bar yang bergerak
                print(f"{draw_visualizer(30)}  Vol: {player.volume}%", end="", flush=True)
            
            # Kita gunakan non-blocking input sederhana
            # Jika ingin input tanpa enter, butuh library tambahan, 
            # untuk sekarang kita simulasi gerakan visualizer sebentar
            time.sleep(0.2)
            
            # Catatan: Di Termux, input() akan menghentikan loop visualizer.
            # Jadi kita minta input hanya jika user menekan enter atau butuh command.
            if player.pause:
                cmd = input("\n[PAUSED] Masukkan perintah: ").lower()
                if cmd == 'p': player.pause = False
                elif cmd == 'q': break
            
    except KeyboardInterrupt:
        player.stop()
    except:
        print("\n[!] Error.")

if __name__ == "__main__":
    main()
