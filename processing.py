import os
import sys
import torch
from argparse import ArgumentParser
from Audio2Video import Audio2Video

parser = ArgumentParser()  
parser.add_argument("--input_image_path", default="test_resource/musk.jpg", help=".")
parser.add_argument("--input_audio_path", default="test_resource/audio.wav", help=".")
parser.add_argument("--output_video_path", default="output.mp4", help=".")
args = parser.parse_args()

a2v = Audio2Video()
a2v.generate(input_image_path=args.input_image_path, 
				input_audio_path=args.input_audio_path, 
				output_video_path=args.output_video_path)


