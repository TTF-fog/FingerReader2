# import Craft class
from craft_text_detector import Craft

# set image path and export folder directory
image = './book.png' # can be filepath, PIL image or numpy array
output_dir = 'outputs/'

# create a craft instance
craft = Craft(output_dir=output_dir, crop_type="box", cuda=True)

prediction_result = craft.detect_text(image)
