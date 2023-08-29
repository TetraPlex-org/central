# AudioMerge
The MVP for client-side proof of concept for the com-snippet protocol is a tool that records audio from multiple devices at the same time, then merges the audio streams into a single audio file, denoising and normalizing the audio in the process.
The resulting single audio file can then be further processed.
Further processing may include the translation of the audio into text - specifically the [International Phonetic Alphabet](https://en.wikipedia.org/wiki/International_Phonetic_Alphabet), that could be used to reconstruct the original spoken words without sending the original audio file over the internet, which fits with the idea of multiple "masks" for anonymity as well as for data compression.

## Recording Audio
The first step is to record audio from multiple devices at the same time.
For this, we need a client-side application that can record audio from the microphone and save it locally.

The application runs on different devices at the same time, the user can start recording whenever they want.
The application then records audio from the microphone and saves it locally.
The user can stop recording whenever they want.
The application then stops recording and saves the audio file locally.

## Merging
The second step is to merge the audio files into a single audio file.
For this, one of the applications is designated as the **server in userland**.
The server in userland is the application that is used to merge the audio files, acting as an intermediary, aggregating and pre-computing the data before sending it to the **router in serverland**.
We don't concern ourselves with *serverland* for now, as it is not part of this PoC.

To designate the **server in userland**, the user starts the application on the device that they want to use as the server and clicks on the "designate as primary" button.
