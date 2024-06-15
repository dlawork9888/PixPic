# PixPic ! 
## Introduction
- pixpic으로 간편하게 픽셀화! 프로필사진을 특별하게 꾸미거나 넷상에 올리기 곤란한 사진들에 적용할 수 있습니다.
- Easily pixelate with pixpic! You can use it to uniquely decorate profile pictures or apply it to photos that are difficult to post online.

## Dependency
- 해당 모듈은 OpenCV를 필요로 합니다. 다음 명령어를 통해 설치할 수 있습니다.
- This module requires OpenCV. It can be installed using the following command:
```bash
pip install opencv-python
```

## Details

pixpic은 세 가지 모듈을 제공합니다.
- pixpic offers three modules.

1. `pixelate_image(image_path, width_dividing = 20, output_path = None)`
이미지를 축소한 후, 확대하여 픽셀화합니다.
- Shrinks the image, then enlarges it to pixelate.
- `image_path`
  - 픽셀화할 이미지의 경로를 지정합니다.
  - Specifies the path of the image to pixelate.
- `width_dividing = 20`
  - input image의 너비를 기준으로 픽셀의 크기를 설정합니다. 기본값으로 input image의 너비를 20등분한 값을 한 변의 길이로 가지는 정사각형이 한 픽셀이 됩니다.
  - Sets the pixel size based on the width of the input image. By default, the pixel size is set to a square with a side length of one-twentieth of the input image's width.
- `output_path = None`
  - 이미지가 저장될 경로를 지정합니다. 해당 경로는 저장될 파일의 이름까지 포함해야합니다. 예를 들어, `temp/temp2/pixelated.jpg`와 같이 설정될 수 있습니다.
  - Specifies the path where the image will be saved. This path must include the file name. For example, it can be set as `temp/temp2/pixelated.jpg`.

2. `pixelate_image_grayscale(image_path, width_dividing = 20, output_path = None)`
- 이미지를 회색조로 변환 후 픽셀화를 진행합니다.
- Converts the image to grayscale and then pixelates it.

3. `pixelate_image_bw(image_path, width_dividing = 20, threshold = 128, threshold_before_downsizing = False, threshold_after_pixelated = True, output_path = None)`
- 픽셀을 전부 흑 또는 백색으로 할당합니다. 
- Assigns all pixels to either black or white.
- `threshold = 128`
  - 0(흑색) 또는 255(백색)으로 나누는 임계값를 설정합니다. 기본값으로 128이 할당됩니다.
  - Sets the threshold value for dividing into 0 (black) or 255 (white). The default is 128.
- `threshold_before_downsizing = False`
  - 흑백화를 진행하고 나서 이미지를 축소합니다. 이는 이후 확대하며 픽샐화를 진행할 경우, 완전한 흑백화가 진행되지 않을 수 있습니다(확대 시 선형보간을 이용하기 때문입니다). 기본적으로 False로 설정되어있습니다. 나름 괜찮은 작품을 얻을 수 있습니다 !
  - Converts to black and white before downsizing the image. This might result in imperfect black and white pixelation when enlarged (due to linear interpolation). The default is False. You can achieve quite an interesting result!
- `threshold_after_pixelated = True`
  - 픽셀화를 진행한 후 흑백화합니다. 이는 픽셀화된 이미지의 완전한 흑백화가 가능합니다. 기본적으로 True로 설정되어있습니다.
  - Converts to black and white after pixelating. This ensures complete black and white pixelation of the image. The default is True.

- 세 함수는 모두 np.ndarray 형태로 변환된 이미지를 반환합니다. (**주의**: 반환값은 모두 OpenCV Image Type(BGR)을 따릅니다. plotting 시 cv2Color(input_image, cv2.COLOR_BGR2RGB)를 사용해주세요)
- All three functions return images in the form of np.ndarray. (**Note**: The return values follow the OpenCV Image Type (BGR). Use cv2Color(input_image, cv2.COLOR_BGR2RGB) for plotting.)

## Example

```python
import matplotlib.pyplot as plt
import pixpic

input_image_path = 'pics/mypic.jpg'

# Original pixelated image
pixelated_image_original = pixpic.pixelate_image(input_image_path, width_dividing=20, output_path=None)

# Grayscale pixelated image
pixelated_image_grayscale = pixpic.pixelate_image_grayscale(input_image_path, width_dividing=20, output_path=None)

# Black and white pixelated image with threshold before downsizing
pixelated_image_bw_threshold_before_downsizing = pixpic.pixelate_image_bw(
                                                        input_image_path, 
                                                        width_dividing=20, 
                                                        threshold=180, 
                                                        threshold_before_downsizing=True, 
                                                        threshold_after_pixelated=False, 
                                                        output_path=None
                                                    )

# Black and white pixelated image with threshold after pixelation
pixelated_image_bw_threshold_after_pixelated = pixpic.pixelate_image_bw(
                                                        input_image_path, 
                                                        width_dividing=20, 
                                                        threshold=180, 
                                                        threshold_before_downsizing=False, 
                                                        threshold_after_pixelated=True, 
                                                        output_path=None
                                                    )

# for plotting the input image
import cv2
input_image = cv2.imread(input_image_path)


# Plotting the images
plt.figure(figsize=(15, 15))


# All func returns images as CV2's image type(BGR)
# When plotting images, use => cv2Color(input_image, cv2.COLOR_BGR2RGB)

# Input
plt.subplot(1, 5, 1)
plt.imshow(cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB))
plt.title('Input Image')
plt.axis('off')

# Original
plt.subplot(1, 5, 2)
plt.imshow(cv2.cvtColor(pixelated_image_original, cv2.COLOR_BGR2RGB))
plt.title('Original Pixelated')
plt.axis('off')

# Grayscale
plt.subplot(1, 5, 3)
plt.imshow(pixelated_image_grayscale, cmap='gray')
plt.title('Grayscale Pixelated')
plt.axis('off')

# Threshold before downsizing
plt.subplot(1, 5, 4)
plt.imshow(pixelated_image_bw_threshold_before_downsizing, cmap='gray')
plt.title('BW Threshold\nBefore Downsizing\n(threshold 180)',fontsize=10)
plt.axis('off')

# Threshold after pixelated
plt.subplot(1, 5, 5)
plt.imshow(pixelated_image_bw_threshold_after_pixelated, cmap='gray')
plt.title('BW Threshold\nAfter Pixelation\n(threshold 180)', fontsize=10)
plt.axis('off')

plt.show()
```
**결과**
**Result**
<img width=1000 src='https://github.com/dlawork9888/PixPic/assets/127077818/171463c5-7035-43cd-bc16-1621a7208d9b'/>
