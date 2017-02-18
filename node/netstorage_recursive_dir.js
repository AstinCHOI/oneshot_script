const Netstorage = require('netstorageapi')
const Sync = require('sync');

const config = {
      hostname: 'hostname',
      keyName: 'keyname',
      key: 'key',
      cpCode: 'cpcode',
      ssl: false
}

const ns = new Netstorage(config);

function recursive(dir, callback) {  
  ns.dir(dir, (err, response, body) => {
    
    if (err) {
      process.nextTick(function() {
        if (body.stat.file != undefined) {
          body.stat.file.forEach( function (item) {
            if (item.type == 'file') {
              console.log(body.stat.attribs.directory + '/' + item.name)
              
            } else if (item.type == 'dir') {
              console.log(body.stat.attribs.directory + '/' + item.name)
              Sync(function() {
                hello.sync(null, body.stat.attribs.directory + '/' + item.name)
              })
            }
          })
        }
      })
    }

    if (response && response.statusCode == 200) {
      process.nextTick(function() {
        if (body.stat.file != undefined) {
          body.stat.file.forEach( function (item) {
            if (item.type == 'file') {
              console.log(body.stat.attribs.directory + '/' + item.name)
              
            } else if (item.type == 'dir') {
              console.log(body.stat.attribs.directory + '/' + item.name)
              Sync(function() {
                hello.sync(null, body.stat.attribs.directory + '/' + item.name)
              })
            }
          })
        }
      })
    }
  });
}

Sync(function() {
  recursive.sync(null, "/" + config.cpCode);
})


  