import math
from scipy.io.wavfile import write
from scipy.io import wavfile
import numpy as np 
import hashlib
import struct
import zlib
import io
from pathlib import Path
from PIL import Image
def noise(ile_path): 
              Fs, y = wavfile.read(ile_path)
              s=[]
              i=0
              while i<=(len(y)-44100):
                  s.append(y[i:i+44100])
                  i+=Fs
              return s 

class mylang():
   def __init__(self,string,key):
      self.string=string
      self.key=key
      self.list=[]

   def lang(self):
      
      for letter in self.string: 
         if letter=="A" or letter=="a":
             x=np.linspace(0.,1.,44100)
             data=0.02*np.sin(2*np.pi*420*x)
             for i in data:
                self.list.append(i)

         elif letter==" ":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*250*x)
            for i in data:
               self.list.append(i)

         elif letter.lower()=="b":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*440*x)
            for i in data:
               self.list.append(i)      
         elif letter.lower()=="c":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*460*x)
            for i in data:
               self.list.append(i)  

         elif letter.lower()=="d":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*480*x)
            for i in data:
               self.list.append(i)   

         elif letter.lower()=="e":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*500*x)
            for i in data:
               self.list.append(i)   

         elif letter.lower()=="f":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*520*x)
            for i in data:
               self.list.append(i)   

         elif letter.lower()=="g":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*540*x)
            for i in data:
               self.list.append(i)   

         elif letter.lower()=="h":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*560*x)
            for i in data:
               self.list.append(i)   

         elif letter.lower()=="i":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*580*x)
            for i in data:
               self.list.append(i)   

         elif letter.lower()=="j":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*600*x)
            for i in data:
               self.list.append(i)   

         elif letter.lower()=="k":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*620*x)
            for i in data:
               self.list.append(i)   

         elif letter.lower()=="l":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*640*x)
            for i in data:
               self.list.append(i)   

         elif letter.lower()=="m":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*660*x)
            for i in data:
               self.list.append(i)   

         elif letter.lower()=="n":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*680*x)
            for i in data:
               self.list.append(i)   

         elif letter.lower()=="o":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*700*x)
            for i in data:
               self.list.append(i)   

         elif letter.lower()=="p":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*720*x)
            for i in data:
               self.list.append(i)   

         elif letter.lower()=="q":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*740*x)
            for i in data:
               self.list.append(i)   

         elif letter.lower()=="r":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*760*x)
            for i in data:
               self.list.append(i)   

         elif letter.lower()=="s":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*780*x)
            for i in data:
               self.list.append(i)   

         elif letter.lower()=="t":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*800*x)
            for i in data:
               self.list.append(i)   

         elif letter.lower()=="u":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*820*x)
            for i in data:
               self.list.append(i)   

         elif letter.lower()=="v":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*840*x)
            for i in data:
               self.list.append(i)   

         elif letter.lower()=="w":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*860*x)
            for i in data:
               self.list.append(i)   

         elif letter.lower()=="x":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*880*x)
            for i in data:
               self.list.append(i)  

         elif letter.lower()=="y":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*900*x)
            for i in data:
               self.list.append(i)   

         elif letter.lower()=="z":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*920*x)
            for i in data:
               self.list.append(i) 

         elif letter=="0":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*940*x)
            for i in data:
               self.list.append(i)

         elif letter=="1":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*960*x)
            for i in data:
               self.list.append(i)

         elif letter=="2":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*980*x)
            for i in data:
               self.list.append(i)

         elif letter=="3":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*1000*x)
            for i in data:
               self.list.append(i)

         elif letter=="4":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*1020*x)
            for i in data:
               self.list.append(i)

         elif letter=="5":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*1040*x)
            for i in data:
               self.list.append(i)

         elif letter=="6":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*1060*x)
            for i in data:
               self.list.append(i)

         elif letter=="7":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*1080*x)
            for i in data:
               self.list.append(i)

         elif letter=="8":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*1100*x)
            for i in data:
               self.list.append(i)

         elif letter=="9":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*1120*x)
            for i in data:
               self.list.append(i)

         elif letter=="!":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*1140*x)
            for i in data:
               self.list.append(i)

         elif letter=='"':
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*1160*x)
            for i in data:
               self.list.append(i)

         elif letter=="#":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*1180*x)
            for i in data:
               self.list.append(i)

         elif letter=="$":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*1200*x)
            for i in data:
               self.list.append(i)

         elif letter=="%":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*1220*x)
            for i in data:
               self.list.append(i)

         elif letter=="&":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*1240*x)
            for i in data:
               self.list.append(i)

         elif letter=="'":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*1260*x)
            for i in data:
               self.list.append(i)

         elif letter=="(":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*1280*x)
            for i in data:
               self.list.append(i)

         elif letter==")":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*1300*x)
            for i in data:
               self.list.append(i)

         elif letter=="*":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*1320*x)
            for i in data:
               self.list.append(i)

         elif letter=="+":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*1340*x)
            for i in data:
               self.list.append(i)

         elif letter==",":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*1360*x)
            for i in data:
               self.list.append(i)

         elif letter=="-":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*1380*x)
            for i in data:
               self.list.append(i)

         elif letter==".":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*1400*x)
            for i in data:
               self.list.append(i)

         elif letter=="/":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*1420*x)
            for i in data:
               self.list.append(i)

         elif letter==":":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*1440*x)
            for i in data:
               self.list.append(i)

         elif letter==";":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*1460*x)
            for i in data:
               self.list.append(i)

         elif letter=="<":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*1480*x)
            for i in data:
               self.list.append(i)

         elif letter=="=":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*1500*x)
            for i in data:
               self.list.append(i)

         elif letter==">":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*1520*x)
            for i in data:
               self.list.append(i)

         elif letter=="?":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*1540*x)
            for i in data:
               self.list.append(i)

         elif letter=="@":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*1560*x)
            for i in data:
               self.list.append(i)

         elif letter=="[":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*1580*x)
            for i in data:
               self.list.append(i)

         elif letter=="\\":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*1600*x)
            for i in data:
               self.list.append(i)

         elif letter=="]":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*1620*x)
            for i in data:
               self.list.append(i)

         elif letter=="^":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*1640*x)
            for i in data:
               self.list.append(i)

         elif letter=="_":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*1660*x)
            for i in data:
               self.list.append(i)

         elif letter=="`":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*1680*x)
            for i in data:
               self.list.append(i)

         elif letter=="{":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*1700*x)
            for i in data:
               self.list.append(i)

         elif letter=="|":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*1720*x)
            for i in data:
               self.list.append(i)

         elif letter=="}":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*1740*x)
            for i in data:
               self.list.append(i)

         elif letter=="~":
            x=np.linspace(0.,1.,44100)
            data=0.02*np.sin(2*np.pi*1760*x)
            for i in data:
               self.list.append(i)
                
   def cryptic(self):
      s=noise(self.key)
      data=np.array(self.list)
      duration=len(data)/44100
      music=np.array(s[0:int(duration)])
      
      return music

   def encrypt(self):
            s=noise(self.key)
            data=np.array(self.list)
            duration=len(data)/44100
         
            music=np.array(s[0:int(duration)])
            if np.max(np.abs(music)) > 1.0:
              music = music / 32768.0
            array_a_mono_blocks = data.reshape(int(duration), 44100)
            array = np.stack([array_a_mono_blocks, array_a_mono_blocks], axis=-1)
            final_signal=  0.0001*array + music 
            write("fnal.wav",44100, final_signal.reshape(-1, 2).astype(np.float32))
            



   
MAGIC = b"MYLANG02"

# Magic, index, total parts, chunk length, chunk size,
# total compressed length, SHA-256 of original WAV
HEADER_FORMAT = ">8sIIIIQ32s"
HEADER_SIZE = struct.calcsize(HEADER_FORMAT)


def bytes_to_bits(data):
    return np.unpackbits(
        np.frombuffer(data, dtype=np.uint8)
    )


def bits_to_bytes(bits):
    if len(bits) % 8 != 0:
        raise ValueError("Bit count must be divisible by 8.")

    return np.packbits(bits).tobytes()


def image_capacity(image_path):
    with Image.open(image_path) as image:
        width, height = image.size

    # Three RGB channels, one hidden bit per channel.
    return (width * height * 3) // 8


def embed_chunk(image_path, output_path, header, chunk):
    with Image.open(image_path) as image:
        rgb = np.array(image.convert("RGB"), dtype=np.uint8)

    flat = rgb.reshape(-1)
    payload = header + chunk
    bits = bytes_to_bits(payload)

    if len(bits) > flat.size:
        raise ValueError(
            f"Image too small for {output_path.name}."
        )

    flat[:len(bits)] = (
        (flat[:len(bits)] & 254) | bits
    )

    Image.fromarray(rgb).save(output_path, format="PNG")



def embed_audio(data, image_path, output_folder):
    # Store the array in NumPy's .npy format so its shape and dtype are preserved.
    audio_array = np.asarray(data, dtype=np.float32)
    buffer = io.BytesIO()
    np.save(buffer, audio_array, allow_pickle=False)
    audio_data = buffer.getvalue()

    # Compress the serialized array and hash the uncompressed bytes.
    compressed = zlib.compress(audio_data, level=9)
    digest = hashlib.sha256(audio_data).digest()

    capacity = image_capacity(image_path)
    chunk_size = capacity - HEADER_SIZE

    if chunk_size <= 0:
        raise ValueError("The carrier image is too small.")

    total_parts = (len(compressed) + chunk_size - 1) // chunk_size

    output_folder = Path(output_folder)
    output_folder.mkdir(parents=True, exist_ok=True)

    print(f"Serialized array data: {len(audio_data):,} bytes")
    print(f"Compressed payload: {len(compressed):,} bytes")
    print(f"Capacity per image: {capacity:,} bytes")
    print(f"Images required: {total_parts}")

    for index in range(total_parts):
        start = index * chunk_size
        end = start + chunk_size
        chunk = compressed[start:end]

        header = struct.pack(
            HEADER_FORMAT,
            MAGIC,
            index,
            total_parts,
            len(chunk),
            chunk_size,
            len(compressed),
            digest,
        )

        output_path = output_folder / f"part_{index + 1:04}.png"
        embed_chunk(image_path, output_path, header, chunk)
        print(f"Created: {output_path}")

    print("\nAudio array successfully embedded across PNG images.")


def extract_chunk(image_path):
    with Image.open(image_path) as image:
        if image.format != "PNG":
            raise ValueError(f"{image_path} is not a PNG.")

        rgb = np.array(image.convert("RGB"), dtype=np.uint8)

    flat = rgb.reshape(-1)
    bits = flat & 1

    if len(bits) < HEADER_SIZE * 8:
        raise ValueError(f"{image_path} is too small.")

    header = bits_to_bytes(bits[:HEADER_SIZE * 8])

    (
        magic,
        index,
        total_parts,
        chunk_length,
        chunk_size,
        compressed_length,
        expected_hash,
    ) = struct.unpack(HEADER_FORMAT, header)

    if magic != MAGIC:
        raise ValueError(
            f"No valid MyLang payload in {image_path}."
        )

    if chunk_length > chunk_size:
        raise ValueError("Invalid chunk length.")

    total_bits = (HEADER_SIZE + chunk_length) * 8

    if total_bits > len(bits):
        raise ValueError(f"Truncated payload in {image_path}.")

    payload = bits_to_bytes(bits[:total_bits])
    chunk = payload[HEADER_SIZE:]

    return {
        "index": index,
        "total": total_parts,
        "chunk_size": chunk_size,
        "compressed_length": compressed_length,
        "hash": expected_hash,
        "chunk": chunk,
    }

def decode_audio(input_folder):
    images = list(Path(input_folder).glob("*.png"))

    if not images:
        raise FileNotFoundError("No PNG images found in the input folder.")

    chunks = {}
    expected_total = None
    expected_digest = None
    expected_compressed_length = None

    for image_path in images:
        info = extract_chunk(image_path)

        index = info["index"]
        total = info["total"]
        digest = info["hash"]
        chunk = info["chunk"]
        compressed_length = info["compressed_length"]

        if expected_total is None:
            expected_total = total
            expected_digest = digest
            expected_compressed_length = compressed_length

        if (
            total != expected_total
            or digest != expected_digest
            or compressed_length != expected_compressed_length
        ):
            raise ValueError("Images contain inconsistent payload metadata.")

        if not 0 <= index < total:
            raise ValueError(f"Invalid chunk index {index} in {image_path}.")

        if index in chunks:
            raise ValueError(f"Duplicate chunk index {index}.")

        chunks[index] = chunk

    if len(chunks) != expected_total:
        raise ValueError(
            f"Expected {expected_total} chunks, found {len(chunks)}."
        )

    # Reassemble chunks using the index stored in each PNG header.
    compressed_data = b"".join(
        chunks[index] for index in range(expected_total)
    )

    if len(compressed_data) != expected_compressed_length:
        raise ValueError("Compressed payload length mismatch.")

    # Decompress and verify the exact bytes that were originally embedded.
    try:
        audio_data = zlib.decompress(compressed_data)
    except zlib.error as exc:
        raise ValueError("Could not decompress the recovered payload.") from exc

    if hashlib.sha256(audio_data).digest() != expected_digest:
        raise ValueError("Hash mismatch: recovered data is corrupted.")

    # Restore the NumPy array, including its original shape.
    try:
        audio_array = np.load(io.BytesIO(audio_data), allow_pickle=False)
    except (ValueError, OSError) as exc:
        raise ValueError(
            "Recovered payload is not a valid NumPy array. "
            "Re-encode the PNGs with this updated version."
        ) from exc

    if audio_array.dtype != np.float32:
        raise ValueError(f"Unexpected recovered dtype: {audio_array.dtype}")

    return audio_array


def main():
  ask=input("TEXT: ")   
  file=input("cover audio file path:")
  con=mylang(ask,file)
  con.lang()
  con.encrypt()
  print("Audio file created successfully.")
  print()
  print("initializing key creation...")
  key_main(con)

def key_main(con):
    print("=== MyLang Audio Steganography ===")
   
    image = input(
                "Enter the carrier PNG image path: "
            ).strip().strip('"')

    output_folder = input(
                "Enter the output folder path: "
            ).strip().strip('"')
    data=con.cryptic()
    embed_audio(data,image, output_folder)



if __name__=="__main__":
   main()