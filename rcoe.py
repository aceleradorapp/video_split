import json
from moviepy.editor import VideoFileClip, concatenate_videoclips

def open_file_ply(arquivo, name_dir="UNNAMED_DIR"):    
    with open(f'{name_dir}/{arquivo}') as data:
        return json.load(data)


def process_video(data_video, name_dir="UNNAMED_DIR"): 
    nome_video = f'{name_dir}/{data_video["nameVideo"]}'   
    clip_total = VideoFileClip(nome_video, audio=False)
    clips = [clip_total.subclip(data_info['videoInit'], data_info['videoFinal']) for data_info in data_video['data']]
    list_drt = [dr.duration for dr in clips]
    return (clips, list_drt)
    

def cut_format(clips, f_default:str, concatenate=False, name_dir="UNNAMED_DIR"):    
    match f_default:
        case 'video':
            _= [clip.write_videofile(f'{name_dir}/cut_videos/video_{i+1}.mp4') for i, clip in enumerate(clips)]
        case 'imagens':
            _= [clip.write_images_sequence(f'{name_dir}/cut_videos/img_%01d.png') for clip in clips]
        case 'giff':
           _= [clip.write_gif(f'{name_dir}/cut_videos/gif_{i+1}.gif') for i, clip in enumerate(clips)]
    
    if concatenate:
        final = concatenate_videoclips(clips)
        final.write_videofile(f'{name_dir}/novo_video.mp4')


def create_new_file_scp(database, list_drt, name_dir="UNNAMED_DIR"):
    with open(f'{name_dir}/{database["nameVideo"][:-4]}.scp', 'w', encoding='utf-8') as outfile:        
        time_pointer = 0.0
        for df, ld in zip(database['data'], list_drt):
            df['videoInit'], df['videoFinal'] = (time_pointer , (ld + time_pointer))
            time_pointer += ld

        json.dump(database, outfile, indent=4)  


if __name__ == "__main__":
    date_video = open_file_ply('Aula 01 word ver01.ply')
    clips, list_drt = process_video(date_video)
    create_new_file_scp(date_video, list_drt)

    #cut_format(clips)