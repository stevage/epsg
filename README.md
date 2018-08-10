## EPSG definitions for Proj4JS

This library is just a convenient container of as many EPSG definitions of possible. For when "just make it work" is more important than saving bytes.

Usage:

```
var epsg = require('epsg')
console.log(epsg['EPSG:3857']);

// +proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0 +k=1.0 +units=m +nadgrids=@null +wktext  +no_defs
```

You can access the `crs-defs.json` file directly if that's useful, for instance with the `reproject` library:

```
reproject --crs-defs=node_modules/epsg/crs-defs.json ...
```