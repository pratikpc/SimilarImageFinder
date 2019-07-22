import os
import typing
from Files import SaveToCSVDataset, ReadFromCSVDataset
from ImageType import ImageType, ImageIterable

def SelectIf(elements: typing.Iterable, Predicate: typing.Callable[[typing.Any],bool]) -> typing.Iterable:
    for elem in elements:
         if Predicate(elem):
             yield elem

def IsMimeTypeImage(image_path: str) -> bool:
    def MimeTypeCheck(filename: str, accepted_exts: typing.List[str]) -> bool:
        def FileExtension(filename: str) -> str:
            return os.path.splitext(filename)[1].lstrip('.')
        extension = FileExtension(filename)
        return any(accepted_ext.lower() == extension.lower() for accepted_ext in accepted_exts)
    return MimeTypeCheck(image_path, ["png","jpg","jpeg","gif"])

def AllImagesInDir(image_dir: str) -> typing.List[str]:
    def AllFilesInDirectory(dir: str) -> typing.Iterable[str]:
        for path in os.listdir(dir):
            yield os.path.abspath(os.path.join(dir, path))
    return SelectIf(AllFilesInDirectory(image_dir), IsMimeTypeImage)

def GenerateImages(image_paths: typing.Iterable[str]) -> ImageIterable:
    for image_path in image_paths:
        image = ImageType(image_path)
        # Remove Unhashed Images
        if image is not None:
            yield image

def GenerateDatasetOfImages(image_dir: str, csv_dir: str):
    image_paths = AllImagesInDir(image_dir)
    images = GenerateImages(image_paths)
    SaveToCSVDataset(csv_dir, images)

def StillHasNotSearched(images: ImageIterable):
    return not images[-1].Searched

def FindAllUniqueImages(images : list):
    def IsDuplicate(image : ImageType, currentImage : ImageType):
        if image == currentImage:
            print("Duplicate", currentImage.Path, image.Path)
            return True
        return False
    while images and StillHasNotSearched(images):
        images[0].Searched  = True
        currentImage = images[0]
        images = images[1:]
        images = [ image for image in images if not IsDuplicate(image, currentImage)]
    return images


if __name__ == "__main__":
    #GenerateDatasetOfImages("images","data.csv")
    Images = list(ReadFromCSVDataset("data.csv", ImageType))
    ImagesUnique = FindAllUniqueImages(Images.copy())
    # print(set(ImagesUnique))