# pip install moviepy
from moviepy.editor import *


def video_freeze(
    movie_in: str = "movie_in.mp4",
    movie_out: str = "movie_out.mp4",
) -> None:

    # Load the video clip
    clip = VideoFileClip(movie_in)

    # Freeze the video frame at 3 seconds
    freeze_time = 3
    freeze_duration = 2
    freeze_frame = clip.to_ImageClip(
        freeze_time
    ).set_duration(freeze_duration)

    # Add text to the frozen frame
    text = "Freeze"
    text_clip = (
        TextClip(
            text,
            fontsize=250,
            color="white",
            bg_color="black",
        )
        .set_duration(freeze_duration)
        .set_pos("top")
    )
    text_clip = text_clip.set_opacity(
        0.6
    )

    # Create a composite video clip
    # of the frozen frame and text
    frozen_clip = CompositeVideoClip(
        [freeze_frame, text_clip]
    )

    # Concatenate the original clip
    # with the frozen clip and the
    # rest of the video
    final_clip = concatenate_videoclips(
        [
            clip.subclip(
                0, freeze_time
            ),
            frozen_clip,
            clip.subclip(
                freeze_time,
                clip.end,
            ),
        ]
    )

    # Export the final video
    final_clip.write_videofile(
        movie_out
    )


video_freeze(movie_in="bmx.mp4")
