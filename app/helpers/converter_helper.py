# ffmpeg basic command 
class Convert: 
  @classmethod 
  def wav_to_mp3(cls, avi_file, mp3_file):
    result ="ffmpeg -i original_video.avi -vn -ar 44100 -ac 2 -ab 192k -f mp3 output_sound.mp3" 
    return result
  
  @classmethod
  def avi_to_mpg(cls, avi_file, mpg_file): 
    result = "ffmpeg -i original_video.avi final_video.mpg" 
    return result 
  
  @classmethod 
  def mpg_to_avi(cls, mpg_file,aiv_file): 
    ffmpeg -i original_video.mpg final_video.avi
    return True 
  
  @classmethod
  def avi_to_flv (cls, avi_file, flv_file): 
    ffmpeg -i original_video.avi -ab 56 -ar 44100 -b 200 -r 15 -s 320x240 -f flv final_video.flv
    return True 
  
  @classmethod 
  def avi_to_dv (cls, avi_file, dv_file_path): 
    ffmpeg -i original_video.avi -s pal -r pal -aspect 4:3 -ar 48000 -ac 2 final_video.dv
    return True 


