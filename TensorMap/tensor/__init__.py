from arcgis.learn import prepare_data, SingleShotDetector

def main():
    data = prepare_data(
        'Colorado Data',
        dataset_type='PASCAL_VOC_rectangles',
        batch_size=16
    )
    data.show_batch()
    model = SingleShotDetector(data, backbone='MobileNetV2', backend='tensorflow
    model.lr_find()
    model.fit(10, .001)
    model.show_results(thresh=0.5)
    model.save('10e')
    model.save('10e_tflite', framework="tflite")