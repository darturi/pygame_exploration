import librosa
import numpy as np
import matplotlib.pyplot as plt

def moving_average(arr, w):
    return np.convolve(arr, np.ones(w), 'valid') / w


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


def scale_to_canvas(canvas_width, arr, sprite_width):
    maximum = max(arr)
    scalar = ((canvas_width // 2) - (sprite_width // 2)) // maximum
    return [scalar * i for i in arr]


def scaled_for_pos(scaled, canvas_width):
    return [(canvas_width // 2) - i for i in scaled]


def create_scaled_neg(pos_scaled, canvas_width):
    return [canvas_width - i for i in pos_scaled]


def get_scaled_pos_neg(audio_path, canvas_width, sprite_width, conv_degree=10000, FPS=60):
    raw_set = get_sprite_path(audio_path, conv_degree, FPS)
    raw_scaled = scale_to_canvas(canvas_width, raw_set, sprite_width)
    pos_scaled = scaled_for_pos(raw_scaled, canvas_width)
    neg_scaled = create_scaled_neg(pos_scaled, canvas_width)
    return pos_scaled, neg_scaled

if __name__ == "__main__":
    audio_path = "assets/violin.wav"
    # x = get_sprite_path(audio_path)

    x, y = get_scaled_pos_neg(audio_path, 400, 40)

    plt.figure(figsize=(14, 5))
    plt.plot(x)
    plt.show()

    plt.figure(figsize=(14, 5))
    plt.plot(y)
    plt.show()
