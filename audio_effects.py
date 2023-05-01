# pip install pydub

from pydub import AudioSegment


def audio_effects(
    file_in: str = "audio_in.mp3",
    file_out: str = "audio_out.mp3",
) -> None:

    # load audio from file
    audio = AudioSegment.from_mp3(
        file_in
    )
    # slice audio into chunks
    # first 2000ms
    first = audio[:2000]
    # 2000ms to 4000ms
    middle = audio[2000:4000]
    # last 2000ms
    last = audio[-2000:]

    # set new playback rate to
    # speed up audio by 200%
    new_rate_fast = int(
        audio.frame_rate * 2.0
    )

    # apply playback rate change
    fast_audio = middle._spawn(
        middle.raw_data,
        overrides={
            "frame_rate": new_rate_fast
        },
    )

    # set new playback rate to slow
    # down audio by 50%
    new_rate_slow = int(
        audio.frame_rate * 0.5
    )

    # apply playback rate change
    slow_audio = last._spawn(
        last.raw_data,
        overrides={
            "frame_rate": new_rate_slow
        },
    )

    # Export to mp3
    final_audio = (
        first + fast_audio + slow_audio
    )
    final_audio.export(
        file_out, format="mp3"
    )


audio_effects("test_audio.mp3")
