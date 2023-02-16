import librosa
import numpy as np
import matplotlib.pyplot as plt


def moving_average(x, w):
    return np.convolve(x, np.ones(w), 'valid') / w


def segmented_avg(arr, seg_len, length):
    final_list = []
    prev_index = 0
    for i in range(length):
        if i % seg_len == 0 and i != 0:
            final_list.append(np.mean(arr[prev_index:i]))
            prev_index = i + 1

    return final_list[1:]


def get_sprite_path(audio_path, conv_degree=10000, FPS=60):
    # x = song data, sr = sample rate
    x, sr = librosa.load(audio_path, sr=None)

    # get song duration
    duration = librosa.get_duration(y=x, sr=sr)

    # Define total frames
    total_frames = duration * FPS

    # Positive values
    positive_values = x[x > 0]

    # get segment length
    pos_len = positive_values.shape[0]
    seg_len = pos_len // (total_frames - 1)

    # get moving averges for both
    pos_moving = moving_average(positive_values, conv_degree)
    pos_seg = segmented_avg(pos_moving, seg_len, pos_len)
    return pos_seg


def get_negative_set(pos_set):
    return [-1 * i for i in pos_set]


audio_path = "assets/violin.wav"
x = get_sprite_path(audio_path)

plt.figure(figsize=(14, 5))
plt.plot(x)
plt.show()

plt.figure(figsize=(14, 5))
plt.plot(get_negative_set(x))
plt.show()