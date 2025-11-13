from configparser import ConfigParser

if __name__ == "__main__":
    # Use ConfigParser library to create configuration file
    config = ConfigParser()

    # Create configurations for "prepare_dataset.py" 
    config['prepare_dataset'] = {
        
        # Input data directory
        'LIDC_DICOM_PATH': './LIDC-IDRI', ## Change Path To Systems's LIDC Dataset Directory
        
        # Cancerous images output data directory
        # For masks
        'MASK_PATH':'./data/Mask', ## Change Path To Respective  Directory
        # For images
        'IMAGE_PATH':'./data/Image', ## Change Path To Respective  Directory

        # Clean images output data directory 
        # For images
        'CLEAN_PATH_IMAGE':'./data/Clean/Image',
        # For masks
        'CLEAN_PATH_MASK':'./data/Clean/Mask',

        # CSV file location for annotations and other releveant informationm, like nodule information, malignancy, train test split
        'META_PATH': './data/Meta/',

        # Mask Threshold is the np.sum(MASK) threshold. Some Masks are too small. We remove these small images, masks as they might act as outliers
        # The threshold 8 was decided by empirical evaluation.
        'Mask_Threshold':8
    }


    # Create configurations for pylidc library
    config['pylidc'] = {

        # Confidence level determines the overlap between the 4 doctors who have made annotation
        'confidence_level': 0.5,
        
        # 512 determines the size of the image
        'padding_size': 512
    }

    # Create the configuration file in lung.conf
    with open('./lung.conf', 'w') as f:
          config.write(f)
