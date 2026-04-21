from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.audio import SoundLoader
import os

class FMusikApp(App):
    def build(self):
        self.track = None
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # Header
        self.label = Label(text="FMusik-B PRO v1.0", font_size='24sp')
        layout.add_widget(self.label)
        
        # Tombol Play
        btn_play = Button(text="PLAY LAGU TEST", size_hint=(1, 0.2), background_color=(0, 1, 0, 1))
        btn_play.bind(on_press=self.play_music)
        layout.add_widget(btn_play)
        
        # Tombol Stop
        btn_stop = Button(text="STOP", size_hint=(1, 0.2), background_color=(1, 0, 0, 1))
        btn_stop.bind(on_press=self.stop_music)
        layout.add_widget(btn_stop)
        
        return layout

    def play_music(self, instance):
        # Mencari file mp3 pertama yang ada di folder
        songs = [f for f in os.listdir('.') if f.endswith('.mp3')]
        if songs:
            if self.track: self.track.stop()
            self.track = SoundLoader.load(songs[0])
            if self.track:
                self.track.play()
                self.label.text = f"Memutar: {songs[0]}"
        else:
            self.label.text = "Gak ada file MP3, Bro!"

    def stop_music(self, instance):
        if self.track:
            self.track.stop()
            self.label.text = "Musik Berhenti"

if __name__ == '__main__':
    FMusikApp().run()
