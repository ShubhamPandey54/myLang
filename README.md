MyLang

<p align="center">
  <strong>Where language becomes sound.</strong>
  <br/>
  An experimental Python project exploring frequency-based text encoding through audio.
</p><p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Audio%20Processing-DSP-168B80?style=flat-square" alt="Audio Processing"/>
</p>How It Works

MyLang converts text into audio by assigning frequencies to individual characters and generating one-second sine waves. The resulting signal is mixed with carrier audio, which is reconstructed from data stored across a folder of PNG images.

The receiver uses the encoded audio and PNG folder to reconstruct the key audio and recover the original message.

Text → Frequencies → Sine Waves
                          ↓
                   Audio Mixing
                          ↓
                    Encoded Audio

PNG Folder → Key Audio → Message Recovery

Getting Started

git clone https://github.com/ShubhamPandey54/myLang.git
cd myLang

Install the required dependencies according to your Python environment, then run the encoding or decoding script.

Security Model

MyLang uses a separate PNG-based key-reconstruction process for message recovery. This is an experimental approach to audio encoding and data concealment, not a guarantee of cryptographic security.

Status

MyLang is a work in progress. Encoding, reconstruction, and decoding capabilities are under development.

---

<p align="center">
  <sub>Text, transformed into sound.</sub>
</p>