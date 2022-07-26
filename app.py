"""
# Google Docstring Format #

função responsável por cortar os videos em determinada sequência,
para se guiar ele utiliza um arquivo '.ply' com os minutos e segundos e informações do vídeo. No momento
em que os videos forem cortados um novo arquivo .json será gerado com as novas informações dos pequenos videos.
"""
import json
import sys
from moviepy.editor import (VideoFileClip)


def open_file_ply(file):
    """_summary_

    Args:
        file (_type_): _description_
    Returns:

    """
    pass

def cut_video(data, *args_format, time=0, type_video="type", name_dir="UNNAMED_DIR"):
    """_summary_

    Args:
        data (_type_): _description_
        time (int, optional): _description_. Defaults to 0.
        type_video (str, optional): _description_. Defaults to "type".
        name_dir (str, optional): _description_. Defaults to "UNNAMED_DIR".
    
    Returns:
        [
            f"video_01_{type_video}":{"time_ini":0.01, "time_fin":0.10}, 
            f"video_02_{type_video}":{"time_ini":0.11,"time_fin":0.55},
        ]

    """
    ...

def create_new_file_ply(file_list):
    """_summary_
    Args:
        file_list (_type_): _description_
    """
    pass

