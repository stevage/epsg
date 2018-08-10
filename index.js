// minimally adapted from https://raw.githubusercontent.com/yuletide/node-proj4js-defs/master/epsg.js
var defs = require('./crs-defs.json');

// add urn definitions, because why the hell not.
Object.keys(defs).forEach(key => {
    defs['urn:ogc:def:crs:' + key.replace(':', '::')] = defs[key];
});

//http://geojson.org/geojson-spec.html#named-crs
defs['urn:ogc:def:crs:OGC:1.3:CRS84'] = defs['EPSG:4326'];

module.exports = defs;
