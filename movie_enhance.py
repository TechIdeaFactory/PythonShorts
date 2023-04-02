# pip install moviepy
from moviepy.editor import *


def video_enhance(
    movie_in: str = "movie_in.mp4",
    movie_out: str = "movie_out.mp4",
) -> None:
    clip = VideoFileClip(movie_in)
    # Get 5 seconds clip
    clip1 = clip.subclip(0, 5)

    # Apply effects to clip
    clip1_slow = clip1.fx(
        vfx.speedx, 0.5
    )
    clip1_reverse = clip1.fx(
        vfx.time_mirror
    )
    clip1_reverse_fast = (
        clip1_reverse.fx(
            vfx.speedx, 4.0
        )
    )

    # Concatenate forward and reverse clips
    clip1_final = (
        concatenate_videoclips(
            [clip1, clip1_reverse_fast]
        )
    )

    # rotate clip1_final by 90 degree for clip2
    clip2 = clip1_final.rotate(90)

    # rotate clip1_final by 180 degree for clip3
    clip3 = clip1_final.rotate(180)

    # rotate clip1 by 270 degree for clip4
    clip4 = clip1_final.rotate(270)

    # list of clips
    clips = [
        [clip1_final, clip2],
        [clip3, clip4],
    ]

    # stack clips
    final = clips_array(clips)

    final.write_videofile(movie_out)


video_enhance(movie_in="skateboard.mp4")
