let net;

async function simple_app() {
    // Load the model.
    net = await async function () {
        console.log('Loading the mobilenet model..');

        var _net = await mobilenet.load();
        console.log('Sucessfully loaded model');

        console.log("endpoints" + _net.endpoints)



        return _net;
    }();

    // Make a prediction through the model on our image.
    const imgEl = document.getElementById('img');
    const result = await net.classify(imgEl);
    console.log(result);


    // raw_data = net.infer(imgEl)
    // console.log(raw_data.toString());

    // raw_data = net.infer(imgEl, 'conv_preds')
    raw_data = net.infer(imgEl, 'conv_pw_13')
    // console.log(raw_data.toString());


    const mnet = await tf.loadModel(
        'https://storage.googleapis.com/tfjs-models/tfjs/mobilenet_v1_0.25_224/model.json');

    // Return a model that outputs an internal activation.
    const layer = mnet.getLayer('conv_pw_13_bn');
    newNet = tf.model({inputs: [layer.input], outputs: mnet.outputs});
    // newNet = tf.model({inputs: mnet.inputs, outputs: mnet.outputs});

    // const result_from_raw = await newNet.classify(raw_data);
    // console.log(result_from_raw);

}


simple_app();