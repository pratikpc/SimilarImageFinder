import cv2

def DHashFromPath(image_path: str, hashSize: int=8) -> str:
    def DHash(image, hashSize=8) -> str:
        if image is None:
            return None
        # Convert to Gray Scale
        gray_scale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # resize the input image, adding a single column (width) so we
        # can compute the horizontal gradient
        resized    = cv2.resize(gray_scale, (hashSize + 1, hashSize))
        # compute the (relative) horizontal gradient between adjacent
        # column pixels
        diff = resized[:, 1:] > resized[:, :-1]
        flattened = diff.flatten()
        hash = ''.join(str(int(x)) for x in flattened)
        return hash
    image = cv2.imread(image_path)
    return DHash(image)
