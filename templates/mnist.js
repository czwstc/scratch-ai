class MNIST {

    getInfo() {
        return {
            id: 'mnist',
            name: 'MINST',
            blocks: [
                {
                    opcode: 'label',
                    blockType: Scratch.BlockType.REPORTER,
                    text: 'recognise image [IMAGE] (label)',
                    arguments: {
                        IMAGE: {
                            type: Scratch.ArgumentType.STRING,
                            defaultValue: 'image'
                        }
                    }
                },
            ],
        };
    }

    label({ IMAGE }) {
        return new Promise(resolve => getImageClassificationResponse(IMAGE, resolve));
    }
}

function getImageClassificationResponse(imagedata, callback) {
    if (imagedata === '' || imagedata === 'image') {
        return callback('You need to put an image block in here');
    }

    var url = new URL('{{url_root}}' + 'mnist');

    var options = {
        headers : {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        },
        method : 'POST',
        body : JSON.stringify({
            data : imagedata,
        })
    };

    fetch(url, options).then((response) => {
        if (response.status === 200 || response.status === 400) {
            response.json().then((result) => {
                if (response.status === 200 && result) 
                    return callback(result.class || result.error);
                callback('Unknown');
            });
        }
        else {
            console.log("response:", response);
            callback('Unknown');
        }
    })
    .catch((err) => {
        console.log("err:", err);
        callback('Unknown');
    });
}

Scratch.extensions.register(new MNIST());