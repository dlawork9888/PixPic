# PixPic ! 
## Introduction
- pixpic으로 간편하게 픽셀화! 프로필사진 혹은 넷상에 올리기 곤란한 사진들에 적용할 수 있습니다.

## Dependency
- 해당 모듈은 OpenCV를 필요로 합니다. 다음 명령어를 통해 설치할 수 있습니다.
```bash
pip install opencv-python
```

## Details
pixpic은 세 가지 모듈을 제공합니다.
`pixelate_image(image_path, width_dividing = 20, output_path = None)`


`pixelate_image_grayscale(image_path, width_dividing = 20, output_path = None)'


`pixelate_image_bw(image_path, width_dividing = 20, threshold = 128, threshold_before_downsizing = False, threshold_after_pixelated = True, output_path = None)`
