import cv2
import os

def pixelate_image(image_path, width_dividing = 20, output_path = None):
    image = cv2.imread(image_path)
    print('image loaded')

    height, width = image.shape[:2]
    print(f'original height, width: {height, width}')

    pixel_size = width // width_dividing
    print(f'pixel width: {pixel_size}')
    print(f'pixel height: {height//int(height / pixel_size)}')
    # pixelate 
    # downsizing to (width_dividing, int(height / pixel_size), then upsize to (width, height)
    temp = cv2.resize(image, (width_dividing, int(height / pixel_size)), interpolation=cv2.INTER_LINEAR)
    pixelated_image = cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST) 
    
    # save pic
    # if output path exists
    if output_path:
        cv2.imwrite(output_path, pixelated_image)
        print(f'pixelated image saved to {output_path}')
    # if output path does not exist
    else:
        # save to folder original pic exists  
        base, ext = os.path.splitext(image_path)
        print(f'original pic path: {image_path}')
        output_path = f"{base}_pixelated{ext}"
        print(f'output: {output_path}')
        if os.path.exists(output_path):
            print(f'File {output_path} exists, it will be overwritten.')
        cv2.imwrite(output_path, pixelated_image)
        print(f'pixelated image saved to {output_path}')
        
    return pixelated_image

def pixelate_image_grayscale(image_path, width_dividing = 20, output_path = None):
    image = cv2.imread(image_path)
    print('image loaded')
    
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    print('image converted to gray scale')
    
    height, width = image.shape[:2]
    print(f'original height, width: {height, width}')

    pixel_size = width // width_dividing
    print(f'pixel width: {pixel_size}')
    print(f'pixel height: {height//int(height / pixel_size)}')
    # pixelate 
    # downsizing to (width_dividing, int(height / pixel_size), then upsize to (width, height)
    temp = cv2.resize(image, (width_dividing, int(height / pixel_size)), interpolation=cv2.INTER_LINEAR)
    pixelated_image = cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST) 
    
    # save pic
    # if output path exists
    if output_path:
        cv2.imwrite(output_path, pixelated_image)
        print(f'pixelated image saved to {output_path}')
    # if output path does not exist
    else:
        # save to folder original pic exists  
        base, ext = os.path.splitext(image_path)
        print(f'original pic path: {image_path}')
        output_path = f"{base}_pixelated_grayscale{ext}"
        print(f'output: {output_path}')
        if os.path.exists(output_path):
            print(f'File {output_path} exists, it will be overwritten.')
        cv2.imwrite(output_path, pixelated_image)
        print(f'pixelated image saved to {output_path}')
        
    return pixelated_image # np nd arr

def pixelate_image_bw(image_path, width_dividing = 20, threshold = 128, threshold_before_downsizing = False, threshold_after_pixelated = True, output_path = None):
    image = cv2.imread(image_path)
    print('image loaded')
    
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    print('image converted to gray scale applying threshold')

    if threshold_before_downsizing:
        _, image = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY)
        print('image converted to black white ver ')
    
    height, width = image.shape[:2]
    print(f'original height, width: {height, width}')

    pixel_size = width // width_dividing
    print(f'pixel width: {pixel_size}')
    print(f'pixel height: {height//int(height / pixel_size)}')
    # pixelate 
    # downsizing to (width_dividing, int(height / pixel_size), then upsize to (width, height)
    temp = cv2.resize(image, (width_dividing, int(height / pixel_size)), interpolation=cv2.INTER_LINEAR)
    pixelated_image = cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST) 
    if threshold_after_pixelated:
        _, pixelated_image = cv2.threshold(pixelated_image, threshold, 255, cv2.THRESH_BINARY)
        print('threshold applyed to the pixelated image')
        
    # save pic
    # if output path exists
    if output_path:
        cv2.imwrite(output_path, pixelated_image)
        print(f'pixelated image saved to {output_path}')
    # if output path does not exist
    else:
        # save to folder original pic exists  
        base, ext = os.path.splitext(image_path)
        print(f'original pic path: {image_path}')
        output_path = f"{base}_pixelated_bw{ext}"
        print(f'output: {output_path}')
        if os.path.exists(output_path):
            print(f'{output_path} already exists, it will be overwritten.')
        cv2.imwrite(output_path, pixelated_image)
        print(f'pixelated image saved to {output_path}')
        
    return pixelated_image # np nd arr

