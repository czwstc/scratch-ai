class LED {
    constructor (runtime) {
        this.runtime = runtime;
    }

    getInfo () {
        return {
            id: 'led',
            name: 'LED',
            blocks: [
                {
                    opcode: 'ledControl',
                    blockType: Scratch.BlockType.COMMAND,
                    text: 'led [INDEX] [STATUS]',
                    arguments: {
                        INDEX: {
                            type: Scratch.ArgumentType.STRING,
                            defaultValue: "1",
                            menu: 'indexes'
                        },
                        STATUS: {
                            type: Scratch.ArgumentType.STRING,
                            defaultValue: "0",
                            menu: 'statuses'
                        }
                    }
                }
            ],
            menus: {
                indexes: [
                    { value : '1', text : '1'},
                    { value : '2', text : '2' },
                    { value : '3', text : '3' },
                ],
                statuses: [
                    { value : '0', text : 'off'},
                    { value : '1', text : 'on' },
                ]
            }
        };
    }

    ledControl({ INDEX, STATUS }) {
        return new Promise(resolve => sendLedCommand(INDEX, STATUS, resolve));
    }
}

function sendLedCommand(index, status, callback) {
    var url = new URL('{{url_root}}' + 'led');
    url.searchParams.append('index', index);
    url.searchParams.append('status', status);
    fetch(url).then((response) => {
        //console.log("sendLedCommand response:", response);
        return callback("done");
    })
}

Scratch.extensions.register(new LED());